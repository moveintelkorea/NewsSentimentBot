import os
import json
from openai import OpenAI
from config import WATCH_STOCKS, OPENAI_MODEL
from crawler import fetch_news

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

CLASSIFY_SYSTEM = """당신은 주식 뉴스 감정 분석 전문가입니다.
뉴스 제목과 요약을 보고 해당 종목에 미치는 실질적인 투자 영향을 판단하세요.
반드시 JSON 형식으로만 응답하세요.

[판단 기준]
- 긍정: 실적 개선, 신사업 수주, 목표주가 상향, 외국인/기관 순매수, 신제품 출시 성공
- 부정: 주가 하락, 실적 악화, 소송/제재, 대규모 손실, 경쟁심화, 수요 감소
- 중립: 단순 현황 보도, 타 종목 언급 중 간접 등장, 인사/조직 변경, 불분명한 내용
- 주의: '주가 방어', '빚투 규제', '차익실현' 같은 표현은 부정 신호로 해석
- 주의: 자사주 매입/소각은 실적 호조 동반 시 긍정, 주가 방어 목적이면 중립~부정"""

CLASSIFY_USER = """종목명: {stock_name}
뉴스 제목: {title}
뉴스 요약: {description}

이 뉴스가 {stock_name} 종목에 미치는 투자 영향을 판단하고 아래 JSON으로만 응답하세요:
{{
  "label": "긍정" 또는 "중립" 또는 "부정",
  "reason": "판단 근거 한 줄 (투자 맥락 기준)"
}}"""

LABEL_SCORE = {"긍정": 1.0, "중립": 0.0, "부정": -1.0}


def _classify_article(stock_name: str, title: str, description: str) -> dict:
    """뉴스 1개를 긍정/중립/부정으로 분류."""
    prompt = CLASSIFY_USER.format(
        stock_name=stock_name,
        title=title,
        description=description,
    )
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": CLASSIFY_SYSTEM},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        response_format={"type": "json_object"},
    )
    result = json.loads(response.choices[0].message.content)
    label = result.get("label", "중립")
    return {
        "label": label,
        "score": LABEL_SCORE.get(label, 0.0),
        "reason": result.get("reason", ""),
    }


def _aggregate(classified: list[dict]) -> dict:
    """개별 분류 결과를 종합해 최종 점수와 감정 산출."""
    if not classified:
        return {"score": 0.0, "sentiment": "중립", "pos": 0, "neu": 0, "neg": 0}

    scores = [c["score"] for c in classified]
    avg = sum(scores) / len(scores)

    pos = sum(1 for c in classified if c["label"] == "긍정")
    neu = sum(1 for c in classified if c["label"] == "중립")
    neg = sum(1 for c in classified if c["label"] == "부정")

    if avg >= 0.3:
        sentiment = "긍정"
    elif avg <= -0.3:
        sentiment = "부정"
    else:
        sentiment = "중립"

    return {"score": round(avg, 2), "sentiment": sentiment, "pos": pos, "neu": neu, "neg": neg}


def run_analysis() -> dict:
    """전체 감시 종목 감정 분석 실행 후 긍정/부정 Top 10 반환."""
    results = []

    for stock in WATCH_STOCKS:
        try:
            news_list = fetch_news(stock["name"], stock.get("aliases", []))
            if not news_list:
                print(f"  뉴스 없음 (제외): {stock['name']}")
                continue

            classified = []
            for news in news_list:
                try:
                    c = _classify_article(stock["name"], news["title"], news["description"])
                    classified.append({**c, "title": news["title"]})
                except Exception as e:
                    print(f"    분류 실패: {news['title'][:30]}... - {e}")

            if not classified:
                continue

            agg = _aggregate(classified)
            results.append({
                "name": stock["name"],
                "ticker": stock["ticker"],
                "score": agg["score"],
                "sentiment": agg["sentiment"],
                "pos": agg["pos"],
                "neu": agg["neu"],
                "neg": agg["neg"],
                "news_count": len(classified),
                "news": [
                    {"title": c["title"], "label": c["label"], "reason": c["reason"]}
                    for c in classified
                ],
            })
            print(
                f"  완료: {stock['name']:12s} ({agg['score']:+.2f}) "
                f"긍정{agg['pos']} 중립{agg['neu']} 부정{agg['neg']} / {len(classified)}건"
            )
        except Exception as e:
            print(f"  실패: {stock['name']} - {e}")

    results.sort(key=lambda x: x["score"], reverse=True)

    return {
        "positive_top10": results[:10],
        "negative_top10": results[-10:][::-1],
    }
