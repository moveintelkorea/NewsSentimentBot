import os
import asyncio
from datetime import date, timedelta
import telegram


def _get_bot() -> telegram.Bot:
    return telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])


def _chat_id() -> str:
    return os.environ["TELEGRAM_CHAT_ID"]


def _score_bar(score: float) -> str:
    if score >= 0.6:
        return "🟢🟢🟢"
    elif score >= 0.3:
        return "🟢🟢"
    elif score >= 0:
        return "🟢"
    elif score >= -0.3:
        return "🔴"
    elif score >= -0.6:
        return "🔴🔴"
    else:
        return "🔴🔴🔴"


def _change_icon(change_pct: float | None) -> str:
    if change_pct is None:
        return "❓"
    return "✅" if change_pct >= 0 else "❌"


async def _send(text: str) -> None:
    bot = _get_bot()
    await bot.send_message(chat_id=_chat_id(), text=text, parse_mode="HTML")


def send_sentiment_report(top10: dict) -> None:
    """오후 9시 감정 분석 리포트 발송."""
    today = date.today().strftime("%Y-%m-%d")

    pos_lines = "\n".join(
        f"{i+1}. {s['name']}  <b>{s['score']:+.2f}</b>  {_score_bar(s['score'])}"
        for i, s in enumerate(top10["positive_top10"])
    )
    neg_lines = "\n".join(
        f"{i+1}. {s['name']}  <b>{s['score']:+.2f}</b>  {_score_bar(s['score'])}"
        for i, s in enumerate(top10["negative_top10"])
    )

    text = (
        f"📊 <b>주식 뉴스 감정 분석 리포트</b>\n"
        f"📅 {today}\n"
        f"─────────────────────────\n\n"
        f"😊 <b>긍정 뉴스 Top 10</b>\n{pos_lines}\n\n"
        f"😟 <b>부정 뉴스 Top 10</b>\n{neg_lines}"
    )
    asyncio.run(_send(text))


def send_price_report(positive_results: list, negative_results: list, base_date: str) -> None:
    """오후 3시 10분 주가 변화율 리포트 발송."""
    today = date.today().strftime("%Y-%m-%d")

    def fmt_line(i, s):
        change = s["change_pct"]
        change_str = f"{change:+.2f}%" if change is not None else "조회불가"
        icon = _change_icon(change)
        return f"{i+1}. {s['name']}  <b>{change_str}</b>  {icon}"

    pos_lines = "\n".join(fmt_line(i, s) for i, s in enumerate(positive_results))
    neg_lines = "\n".join(fmt_line(i, s) for i, s in enumerate(negative_results))

    pos_hit = sum(1 for s in positive_results if s["change_pct"] is not None and s["change_pct"] >= 0)
    neg_hit = sum(1 for s in negative_results if s["change_pct"] is not None and s["change_pct"] < 0)

    text = (
        f"📈 <b>어제 예측 → 오늘 결과</b>\n"
        f"📅 어제 {base_date} 분석 기준\n"
        f"─────────────────────────\n\n"
        f"😊 <b>긍정 예측 종목 결과</b>\n{pos_lines}\n\n"
        f"😟 <b>부정 예측 종목 결과</b>\n{neg_lines}\n\n"
        f"🎯 예측 적중률: 긍정 {pos_hit}/10  부정 {neg_hit}/10"
    )
    asyncio.run(_send(text))
