import yfinance as yf


def get_price_changes(stocks: list[dict]) -> list[dict]:
    """종목 리스트의 당일 주가 변화율을 조회합니다."""
    results = []

    for stock in stocks:
        try:
            ticker = yf.Ticker(stock["ticker"])
            hist = ticker.history(period="2d")

            if len(hist) < 2:
                change_pct = 0.0
            else:
                prev_close = hist["Close"].iloc[-2]
                today_close = hist["Close"].iloc[-1]
                change_pct = (today_close - prev_close) / prev_close * 100

            results.append({
                "name": stock["name"],
                "ticker": stock["ticker"],
                "change_pct": round(change_pct, 2),
                "score": stock.get("score", 0),
            })
        except Exception as e:
            print(f"  주가 조회 실패: {stock['name']} - {e}")
            results.append({
                "name": stock["name"],
                "ticker": stock["ticker"],
                "change_pct": None,
                "score": stock.get("score", 0),
            })

    return results
