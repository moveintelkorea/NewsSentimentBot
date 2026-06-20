from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from analyzer import run_analysis
from stock import get_price_changes
from storage import save_top10, load_top10
from bot import send_sentiment_report, send_price_report


def job_sentiment_report():
    """21:00 — 뉴스 감정 분석 후 텔레그램 발송."""
    print("[21:00] 뉴스 감정 분석 시작...")
    top10 = run_analysis()
    save_top10(top10)
    send_sentiment_report(top10)
    print("[21:00] 발송 완료")


def job_price_report():
    """15:10 — 어제 Top 10 주가 변화율 조회 후 텔레그램 발송."""
    print("[15:10] 주가 변화율 조회 시작...")
    data = load_top10()
    if data is None:
        print("[15:10] 저장된 Top 10 데이터 없음, 건너뜀")
        return

    base_date = data.get("date", "")
    pos_results = get_price_changes(data["positive_top10"])
    neg_results = get_price_changes(data["negative_top10"])
    send_price_report(pos_results, neg_results, base_date)
    print("[15:10] 발송 완료")


def start():
    scheduler = BlockingScheduler(timezone="Asia/Seoul")

    scheduler.add_job(
        job_sentiment_report,
        CronTrigger(hour=21, minute=0, timezone="Asia/Seoul"),
        id="sentiment_report",
    )
    scheduler.add_job(
        job_price_report,
        CronTrigger(hour=15, minute=10, timezone="Asia/Seoul"),
        id="price_report",
    )

    print("스케줄러 시작 (21:00 감정 분석 / 15:10 주가 변화율)")
    scheduler.start()
