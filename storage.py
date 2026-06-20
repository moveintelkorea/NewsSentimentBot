import json
import os
from datetime import date

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "top10.json")
NEWS_FILE = os.path.join(DATA_DIR, "news_source.json")


def save_top10(data: dict) -> None:
    os.makedirs(DATA_DIR, exist_ok=True)

    # 뉴스 소스만 별도 저장
    all_stocks = data["positive_top10"] + data["negative_top10"]
    news_source = {
        "date": str(date.today()),
        "stocks": [
            {"name": s["name"], "ticker": s["ticker"], "score": s["score"], "news": s.get("news", [])}
            for s in all_stocks
        ],
    }
    with open(NEWS_FILE, "w", encoding="utf-8") as f:
        json.dump(news_source, f, ensure_ascii=False, indent=2)

    # top10.json에는 news 필드 제외하고 저장
    def strip_news(stocks):
        return [{k: v for k, v in s.items() if k != "news"} for s in stocks]

    payload = {
        "date": str(date.today()),
        "positive_top10": strip_news(data["positive_top10"]),
        "negative_top10": strip_news(data["negative_top10"]),
    }
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def load_top10() -> dict | None:
    if not os.path.exists(DATA_FILE):
        return None
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
