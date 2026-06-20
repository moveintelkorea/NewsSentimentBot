import sys
from dotenv import load_dotenv

load_dotenv()

from scheduler import start, job_sentiment_report, job_price_report


if __name__ == "__main__":
    # 인자 없이 실행하면 스케줄러 시작
    # python main.py sentiment  → 감정 분석 즉시 실행 (테스트용)
    # python main.py price      → 주가 변화율 즉시 실행 (테스트용)
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "sentiment":
            job_sentiment_report()
        elif cmd == "price":
            job_price_report()
        else:
            print(f"알 수 없는 명령: {cmd}")
            print("사용법: python main.py [sentiment|price]")
    else:
        start()
