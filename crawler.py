import os
import re
import requests
from config import NEWS_BATCH_SIZE, NEWS_MAX_PER_STOCK


def _strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def _normalize(text: str) -> str:
    """비교용 정규화: 앞뒤 공백 제거 + 내부 공백 제거 + 소문자 변환."""
    return text.strip().replace(" ", "").lower()


def _title_matches(title: str, stock_name: str, aliases: list[str]) -> bool:
    """
    뉴스 제목에 종목명이 포함되어 있는지 판단.
    - 공백 차이 무시 (strip + 내부 공백 제거)
    - 대소문자 무시
    - aliases(별칭)도 함께 검사
    - 종목명이 2글자 이하(KT 등)는 단어 경계 조건 추가해 오탐 방지
    """
    norm_title = _normalize(title)
    candidates = [stock_name] + (aliases or [])

    for name in candidates:
        norm_name = _normalize(name)
        if not norm_name:
            continue

        if len(norm_name) <= 2:
            # 짧은 이름은 단독 토큰으로만 매칭 (예: "KT" → "KT증권" 오탐 방지)
            pattern = r'(?<![가-힣a-z0-9])' + re.escape(norm_name) + r'(?![가-힣a-z0-9])'
            if re.search(pattern, norm_title):
                return True
        else:
            if norm_name in norm_title:
                return True

    return False


def fetch_news(stock_name: str, aliases: list[str] = None) -> list[dict]:
    """
    네이버 뉴스 검색 API로 종목 관련 뉴스를 수집.
    - 10개씩 배치 호출
    - 배치 내 제목에 종목명이 하나도 없으면 중단
    - 제목에 종목명이 포함된 뉴스만 수집
    - 최대 NEWS_MAX_PER_STOCK개까지 수집
    """
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": os.environ["NAVER_CLIENT_ID"],
        "X-Naver-Client-Secret": os.environ["NAVER_CLIENT_SECRET"],
    }

    collected = []
    start = 1

    while len(collected) < NEWS_MAX_PER_STOCK:
        params = {
            "query": f"{stock_name} 주식",
            "display": NEWS_BATCH_SIZE,
            "start": start,
            "sort": "date",
        }

        resp = requests.get(url, headers=headers, params=params, timeout=10)
        resp.raise_for_status()

        items = resp.json().get("items", [])
        if not items:
            break

        batch_matched = []
        for item in items:
            title = _strip_html(item["title"])
            description = _strip_html(item["description"])
            if _title_matches(title, stock_name, aliases):
                batch_matched.append({"title": title, "description": description})

        # 배치 내에 종목명이 포함된 제목이 하나도 없으면 중단
        if not batch_matched:
            break

        collected.extend(batch_matched)
        start += NEWS_BATCH_SIZE

    return collected[:NEWS_MAX_PER_STOCK]
