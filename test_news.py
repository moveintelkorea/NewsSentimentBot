"""
뉴스 수집 테스트 스크립트
- 저장된 news_source.json 확인
- 또는 특정 종목 실시간 뉴스 수집 테스트
사용법:
  python test_news.py              → 저장된 뉴스 소스 출력
  python test_news.py 삼성전자     → 해당 종목 실시간 뉴스 수집
"""

import sys
import json
from dotenv import load_dotenv

load_dotenv()

from crawler import fetch_news
from storage import NEWS_FILE


def show_saved_news():
    try:
        with open(NEWS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ news_source.json 없음. 먼저 'python main.py sentiment' 실행하세요.")
        return

    print(f"\n📰 저장된 뉴스 소스 ({data['date']})\n")
    print(f"총 {len(data['stocks'])}개 종목\n")
    print("=" * 60)

    for stock in data["stocks"]:
        score = stock["score"]
        icon = "😊" if score >= 0 else "😟"
        print(f"\n{icon} {stock['name']}  ({score:+.2f})")
        print("-" * 40)
        for i, news in enumerate(stock["news"], 1):
            print(f"  [{i}] {news['title']}")
            if news.get("description"):
                print(f"      {news['description'][:60]}...")


def show_live_news(stock_name: str):
    print(f"\n🔍 '{stock_name}' 실시간 뉴스 수집 중...\n")
    news_list = fetch_news(stock_name, count=5)

    if not news_list:
        print("뉴스 없음")
        return

    print(f"총 {len(news_list)}개 뉴스\n")
    print("=" * 60)
    for i, news in enumerate(news_list, 1):
        print(f"\n[{i}] {news['title']}")
        print(f"    {news['description']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        show_live_news(sys.argv[1])
    else:
        show_saved_news()
