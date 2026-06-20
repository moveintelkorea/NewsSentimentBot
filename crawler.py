import os
import re
import asyncio
import aiohttp
from config import NEWS_BATCH_SIZE, NEWS_MAX_PER_STOCK


def _strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def _normalize(text: str) -> str:
    return text.strip().replace(" ", "").lower()


def _title_matches(title: str, stock_name: str, aliases: list[str]) -> bool:
    norm_title = _normalize(title)
    candidates = [stock_name] + (aliases or [])

    for name in candidates:
        norm_name = _normalize(name)
        if not norm_name:
            continue
        if len(norm_name) <= 2:
            pattern = r'(?<![가-힣a-z0-9])' + re.escape(norm_name) + r'(?![가-힣a-z0-9])'
            if re.search(pattern, norm_title):
                return True
        else:
            if norm_name in norm_title:
                return True
    return False


async def fetch_news_async(
    session: aiohttp.ClientSession,
    stock_name: str,
    aliases: list[str] = None,
) -> list[dict]:
    """비동기로 네이버 뉴스 수집."""
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

        async with session.get(url, headers=headers, params=params) as resp:
            resp.raise_for_status()
            data = await resp.json()

        items = data.get("items", [])
        if not items:
            break

        batch_matched = []
        for item in items:
            title = _strip_html(item["title"])
            description = _strip_html(item["description"])
            if _title_matches(title, stock_name, aliases):
                batch_matched.append({"title": title, "description": description})

        if not batch_matched:
            break

        collected.extend(batch_matched)
        start += NEWS_BATCH_SIZE

    return collected[:NEWS_MAX_PER_STOCK]


# 동기 인터페이스 (테스트용)
def fetch_news(stock_name: str, aliases: list[str] = None) -> list[dict]:
    async def _run():
        async with aiohttp.ClientSession() as session:
            return await fetch_news_async(session, stock_name, aliases)
    return asyncio.run(_run())
