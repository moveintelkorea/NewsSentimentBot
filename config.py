# 시총 높은 순 (코스피/코스닥 상위 250개)
# aliases: 뉴스 제목에서 다르게 표기될 수 있는 이름 목록
WATCH_STOCKS = [
    # ── 반도체/전자 ──────────────────────────────────────────
    {"name": "삼성전자",        "ticker": "005930.KS", "aliases": ["삼전"]},
    {"name": "SK하이닉스",      "ticker": "000660.KS", "aliases": ["하이닉스", "닉스"]},
    {"name": "삼성전기",        "ticker": "009150.KS", "aliases": []},
    {"name": "LG이노텍",        "ticker": "011070.KS", "aliases": []},
    {"name": "DB하이텍",        "ticker": "000990.KS", "aliases": []},
    {"name": "한미반도체",      "ticker": "042700.KS", "aliases": []},
    {"name": "리노공업",        "ticker": "058470.KS", "aliases": []},
    {"name": "HPSP",            "ticker": "403870.KQ", "aliases": []},
    {"name": "이수페타시스",    "ticker": "007660.KS", "aliases": []},
    {"name": "티씨케이",        "ticker": "064760.KQ", "aliases": []},
    {"name": "원익IPS",         "ticker": "240810.KQ", "aliases": []},
    {"name": "피에스케이",      "ticker": "319660.KQ", "aliases": ["PSK"]},
    {"name": "주성엔지니어링",  "ticker": "036930.KQ", "aliases": []},
    {"name": "솔브레인",        "ticker": "357780.KS", "aliases": []},
    {"name": "동진쎄미켐",      "ticker": "005290.KS", "aliases": []},
    {"name": "SK스퀘어",        "ticker": "402340.KS", "aliases": []},

    # ── 2차전지/소재 ─────────────────────────────────────────
    {"name": "LG에너지솔루션",  "ticker": "373220.KS", "aliases": ["LG엔솔", "엔솔"]},
    {"name": "삼성SDI",         "ticker": "006400.KS", "aliases": ["삼성에스디아이"]},
    {"name": "LG화학",          "ticker": "051910.KS", "aliases": []},
    {"name": "에코프로비엠",    "ticker": "247540.KQ", "aliases": ["에코프로BM"]},
    {"name": "에코프로",        "ticker": "086520.KQ", "aliases": []},
    {"name": "포스코퓨처엠",    "ticker": "003670.KS", "aliases": ["포스코케미칼", "POSCO퓨처엠"]},
    {"name": "엘앤에프",        "ticker": "066970.KQ", "aliases": []},
    {"name": "코스모신소재",    "ticker": "005070.KS", "aliases": []},
    {"name": "엔켐",            "ticker": "348370.KQ", "aliases": []},
    {"name": "천보",            "ticker": "278280.KQ", "aliases": []},
    {"name": "에코프로에이치엔","ticker": "383310.KQ", "aliases": ["에코프로HN"]},

    # ── 자동차/부품 ──────────────────────────────────────────
    {"name": "현대차",          "ticker": "005380.KS", "aliases": ["현대자동차"]},
    {"name": "기아",            "ticker": "000270.KS", "aliases": ["기아차", "기아자동차"]},
    {"name": "현대모비스",      "ticker": "012330.KS", "aliases": []},
    {"name": "현대위아",        "ticker": "011210.KS", "aliases": []},
    {"name": "현대글로비스",    "ticker": "086280.KS", "aliases": []},
    {"name": "HL만도",          "ticker": "204320.KS", "aliases": ["만도"]},
    {"name": "한온시스템",      "ticker": "018880.KS", "aliases": []},
    {"name": "성우하이텍",      "ticker": "015750.KS", "aliases": []},

    # ── 철강/소재 ────────────────────────────────────────────
    {"name": "POSCO홀딩스",     "ticker": "005490.KS", "aliases": ["포스코", "POSCO"]},
    {"name": "현대제철",        "ticker": "004020.KS", "aliases": []},
    {"name": "고려아연",        "ticker": "010130.KS", "aliases": []},
    {"name": "풍산",            "ticker": "103140.KS", "aliases": []},
    {"name": "세아베스틸지주",  "ticker": "001430.KS", "aliases": ["세아베스틸"]},
    {"name": "동국제강",        "ticker": "460860.KS", "aliases": []},

    # ── 화학/에너지 ──────────────────────────────────────────
    {"name": "롯데케미칼",      "ticker": "011170.KS", "aliases": ["롯데화학"]},
    {"name": "금호석유",        "ticker": "011780.KS", "aliases": ["금호석유화학"]},
    {"name": "OCI홀딩스",       "ticker": "456040.KS", "aliases": ["OCI"]},
    {"name": "효성첨단소재",    "ticker": "298050.KS", "aliases": []},
    {"name": "효성티앤씨",      "ticker": "298020.KS", "aliases": []},
    {"name": "SK케미칼",        "ticker": "285130.KS", "aliases": []},
    {"name": "한화솔루션",      "ticker": "009830.KS", "aliases": ["한화큐셀"]},
    {"name": "S-Oil",           "ticker": "010950.KS", "aliases": ["에스오일"]},
    {"name": "SK이노베이션",    "ticker": "096770.KS", "aliases": ["SK이노"]},

    # ── 에너지/유틸리티 ──────────────────────────────────────
    {"name": "한국전력",        "ticker": "015760.KS", "aliases": ["한전", "한국전력공사"]},
    {"name": "한국가스공사",    "ticker": "036460.KS", "aliases": ["가스공사", "코가스"]},
    {"name": "한국지역난방공사","ticker": "071320.KS", "aliases": ["지역난방"]},

    # ── 금융/보험/증권 ───────────────────────────────────────
    {"name": "KB금융",          "ticker": "105560.KS", "aliases": ["KB금융지주", "국민은행"]},
    {"name": "신한지주",        "ticker": "055550.KS", "aliases": ["신한금융", "신한은행"]},
    {"name": "하나금융지주",    "ticker": "086790.KS", "aliases": ["하나금융", "하나은행"]},
    {"name": "우리금융지주",    "ticker": "316140.KS", "aliases": ["우리금융", "우리은행"]},
    {"name": "기업은행",        "ticker": "024110.KS", "aliases": ["IBK기업은행"]},
    {"name": "삼성생명",        "ticker": "032830.KS", "aliases": []},
    {"name": "삼성화재",        "ticker": "000810.KS", "aliases": []},
    {"name": "DB손해보험",      "ticker": "005830.KS", "aliases": ["DB손보"]},
    {"name": "현대해상",        "ticker": "001450.KS", "aliases": []},
    {"name": "메리츠화재",      "ticker": "000060.KS", "aliases": []},
    {"name": "미래에셋증권",    "ticker": "006800.KS", "aliases": []},
    {"name": "삼성증권",        "ticker": "016360.KS", "aliases": []},
    {"name": "키움증권",        "ticker": "039490.KS", "aliases": []},
    {"name": "한국투자증권",    "ticker": "030210.KS", "aliases": ["한국금융지주"]},
    {"name": "NH투자증권",      "ticker": "005940.KS", "aliases": []},
    {"name": "메리츠금융지주",  "ticker": "138040.KS", "aliases": ["메리츠금융"]},

    # ── IT/인터넷/통신 ───────────────────────────────────────
    {"name": "NAVER",           "ticker": "035420.KS", "aliases": ["네이버"]},
    {"name": "카카오",          "ticker": "035720.KS", "aliases": []},
    {"name": "카카오뱅크",      "ticker": "323410.KS", "aliases": []},
    {"name": "카카오페이",      "ticker": "377300.KS", "aliases": []},
    {"name": "카카오게임즈",    "ticker": "293490.KQ", "aliases": []},
    {"name": "SK텔레콤",        "ticker": "017670.KS", "aliases": ["SKT", "에스케이텔레콤"]},
    {"name": "KT",              "ticker": "030200.KS", "aliases": ["케이티"]},
    {"name": "LG유플러스",      "ticker": "032640.KS", "aliases": ["LGU+", "유플러스"]},
    {"name": "KT&G",            "ticker": "033780.KS", "aliases": []},

    # ── 게임 ─────────────────────────────────────────────────
    {"name": "크래프톤",        "ticker": "259960.KS", "aliases": []},
    {"name": "넷마블",          "ticker": "251270.KS", "aliases": []},
    {"name": "엔씨소프트",      "ticker": "036570.KS", "aliases": ["엔씨", "NC소프트"]},
    {"name": "펄어비스",        "ticker": "263750.KQ", "aliases": []},
    {"name": "컴투스",          "ticker": "078340.KQ", "aliases": []},
    {"name": "위메이드",        "ticker": "112040.KQ", "aliases": []},
    {"name": "NHN",             "ticker": "181710.KQ", "aliases": []},
    {"name": "더블유게임즈",    "ticker": "192080.KQ", "aliases": ["W게임즈"]},
    {"name": "웹젠",            "ticker": "069080.KQ", "aliases": []},

    # ── 바이오/제약 ──────────────────────────────────────────
    {"name": "삼성바이오로직스","ticker": "207940.KS", "aliases": ["삼성바이오"]},
    {"name": "셀트리온",        "ticker": "068270.KS", "aliases": []},
    {"name": "유한양행",        "ticker": "000100.KS", "aliases": []},
    {"name": "한미약품",        "ticker": "128940.KS", "aliases": []},
    {"name": "종근당",          "ticker": "185750.KS", "aliases": []},
    {"name": "대웅제약",        "ticker": "069620.KS", "aliases": []},
    {"name": "녹십자",          "ticker": "006280.KS", "aliases": ["GC녹십자"]},
    {"name": "동아에스티",      "ticker": "170900.KS", "aliases": []},
    {"name": "보령",            "ticker": "003850.KS", "aliases": ["보령제약"]},
    {"name": "일동제약",        "ticker": "249420.KS", "aliases": []},
    {"name": "알테오젠",        "ticker": "196170.KQ", "aliases": []},
    {"name": "리가켐바이오",    "ticker": "141080.KQ", "aliases": ["레고켐바이오"]},
    {"name": "휴젤",            "ticker": "145020.KQ", "aliases": []},
    {"name": "클래시스",        "ticker": "214150.KQ", "aliases": []},
    {"name": "파마리서치",      "ticker": "214450.KQ", "aliases": []},
    {"name": "에이비엘바이오",  "ticker": "298380.KQ", "aliases": ["ABL바이오"]},
    {"name": "메드팩토",        "ticker": "235980.KQ", "aliases": []},
    {"name": "오스코텍",        "ticker": "039200.KQ", "aliases": []},
    {"name": "바이오니아",      "ticker": "064550.KQ", "aliases": []},
    {"name": "씨젠",            "ticker": "096530.KQ", "aliases": []},
    {"name": "에스디바이오센서","ticker": "137310.KQ", "aliases": ["SD바이오센서"]},
    {"name": "인바디",          "ticker": "041830.KQ", "aliases": []},
    {"name": "제이시스메디칼",  "ticker": "287410.KQ", "aliases": []},
    {"name": "한국콜마",        "ticker": "161890.KS", "aliases": []},
    {"name": "코스맥스",        "ticker": "192820.KS", "aliases": []},

    # ── 뷰티/소비재 ──────────────────────────────────────────
    {"name": "아모레퍼시픽",    "ticker": "090430.KS", "aliases": ["아모레"]},
    {"name": "LG생활건강",      "ticker": "051900.KS", "aliases": []},

    # ── 유통/식음료 ──────────────────────────────────────────
    {"name": "이마트",          "ticker": "139480.KS", "aliases": []},
    {"name": "신세계",          "ticker": "004170.KS", "aliases": []},
    {"name": "현대백화점",      "ticker": "069960.KS", "aliases": []},
    {"name": "롯데쇼핑",        "ticker": "023530.KS", "aliases": []},
    {"name": "CJ제일제당",      "ticker": "097950.KS", "aliases": ["CJ제당"]},
    {"name": "오리온",          "ticker": "271560.KS", "aliases": []},
    {"name": "농심",            "ticker": "004370.KS", "aliases": []},
    {"name": "하이트진로",      "ticker": "000080.KS", "aliases": []},
    {"name": "오비맥주",        "ticker": "009150.KS", "aliases": []},
    {"name": "빙그레",          "ticker": "005180.KS", "aliases": []},
    {"name": "CJ",              "ticker": "001040.KS", "aliases": []},

    # ── 건설/건자재 ──────────────────────────────────────────
    {"name": "현대건설",        "ticker": "000720.KS", "aliases": []},
    {"name": "GS건설",          "ticker": "006360.KS", "aliases": []},
    {"name": "대우건설",        "ticker": "047040.KS", "aliases": []},
    {"name": "DL이앤씨",        "ticker": "375500.KS", "aliases": ["대림산업"]},
    {"name": "HDC현대산업개발", "ticker": "294870.KS", "aliases": ["현대산업개발"]},
    {"name": "삼성엔지니어링",  "ticker": "028050.KS", "aliases": []},
    {"name": "GS",              "ticker": "078930.KS", "aliases": ["GS칼텍스"]},

    # ── 항공/해운/물류 ───────────────────────────────────────
    {"name": "대한항공",        "ticker": "003490.KS", "aliases": []},
    {"name": "HMM",             "ticker": "011200.KS", "aliases": ["현대상선"]},
    {"name": "팬오션",          "ticker": "028670.KS", "aliases": []},
    {"name": "CJ대한통운",      "ticker": "000120.KS", "aliases": []},
    {"name": "한진칼",          "ticker": "180640.KS", "aliases": []},

    # ── 조선/기계 ────────────────────────────────────────────
    {"name": "HD현대중공업",    "ticker": "329180.KS", "aliases": ["현대중공업"]},
    {"name": "HD한국조선해양",  "ticker": "009540.KS", "aliases": ["한국조선해양"]},
    {"name": "삼성중공업",      "ticker": "010140.KS", "aliases": []},
    {"name": "한화오션",        "ticker": "042660.KS", "aliases": ["대우조선해양"]},
    {"name": "두산밥캣",        "ticker": "241560.KS", "aliases": []},
    {"name": "두산에너빌리티",  "ticker": "034020.KS", "aliases": ["두산중공업"]},
    {"name": "HD현대",          "ticker": "267250.KS", "aliases": []},

    # ── 방산/우주 ────────────────────────────────────────────
    {"name": "한화에어로스페이스","ticker": "012450.KS","aliases": ["한화에어로"]},
    {"name": "한국항공우주",    "ticker": "047810.KS", "aliases": ["KAI"]},
    {"name": "한화시스템",      "ticker": "272210.KS", "aliases": []},
    {"name": "LIG넥스원",       "ticker": "079550.KS", "aliases": []},
    {"name": "현대로템",        "ticker": "064350.KS", "aliases": []},
    {"name": "빅텍",            "ticker": "065450.KQ", "aliases": []},

    # ── 전기/전력 ────────────────────────────────────────────
    {"name": "LS일렉트릭",      "ticker": "010120.KS", "aliases": []},
    {"name": "효성중공업",      "ticker": "298040.KS", "aliases": []},
    {"name": "HD현대일렉트릭",  "ticker": "267260.KS", "aliases": ["현대일렉트릭"]},
    {"name": "LS",              "ticker": "006260.KS", "aliases": []},
    {"name": "제룡전기",        "ticker": "033100.KQ", "aliases": []},
    {"name": "일진전기",        "ticker": "103590.KS", "aliases": []},

    # ── 디스플레이 ───────────────────────────────────────────
    {"name": "LG디스플레이",    "ticker": "034220.KS", "aliases": ["LGD"]},
    {"name": "삼성디스플레이",  "ticker": "없음",       "aliases": []},  # 비상장 제외용 placeholder
    {"name": "덕산네오룩스",    "ticker": "213420.KQ", "aliases": []},
    {"name": "이녹스첨단소재",  "ticker": "272290.KQ", "aliases": []},

    # ── 부동산/리츠 ──────────────────────────────────────────
    {"name": "SK리츠",          "ticker": "395400.KS", "aliases": []},
    {"name": "맥쿼리인프라",    "ticker": "088980.KS", "aliases": []},

    # ── 엔터/미디어 ──────────────────────────────────────────
    {"name": "HYBE",            "ticker": "352820.KS", "aliases": ["하이브"]},
    {"name": "SM엔터테인먼트",  "ticker": "041510.KQ", "aliases": ["SM엔터", "에스엠"]},
    {"name": "JYP Ent.",        "ticker": "035900.KQ", "aliases": ["JYP", "제이와이피"]},
    {"name": "YG엔터테인먼트",  "ticker": "122870.KQ", "aliases": ["YG엔터", "와이지"]},
    {"name": "CJ ENM",          "ticker": "035760.KQ", "aliases": ["CJ이엔엠"]},
    {"name": "스튜디오드래곤",  "ticker": "253450.KQ", "aliases": []},
    {"name": "콘텐트리중앙",    "ticker": "036420.KS", "aliases": ["중앙미디어"]},

    # ── 플랫폼/핀테크 ────────────────────────────────────────
    {"name": "토스뱅크",        "ticker": "없음",       "aliases": []},  # 비상장
    {"name": "케이뱅크",        "ticker": "없음",       "aliases": []},  # 비상장
    {"name": "비바리퍼블리카",  "ticker": "없음",       "aliases": ["토스"]},  # 비상장

    # ── 클라우드/AI/소프트웨어 ───────────────────────────────
    {"name": "더존비즈온",      "ticker": "012510.KS", "aliases": []},
    {"name": "카카오엔터프라이즈","ticker": "없음",     "aliases": []},
    {"name": "삼성SDS",         "ticker": "018260.KS", "aliases": []},
    {"name": "LG CNS",          "ticker": "064350.KS", "aliases": []},
    {"name": "현대오토에버",    "ticker": "307950.KS", "aliases": []},
    {"name": "SK C&C",          "ticker": "034730.KS", "aliases": []},

    # ── 교육 ─────────────────────────────────────────────────
    {"name": "메가스터디교육",  "ticker": "215200.KQ", "aliases": ["메가스터디"]},
    {"name": "이투스",          "ticker": "096240.KQ", "aliases": []},

    # ── 기타 주요 종목 ───────────────────────────────────────
    {"name": "삼성물산",        "ticker": "028260.KS", "aliases": []},
    {"name": "SK텔레시스",      "ticker": "036630.KQ", "aliases": []},
    {"name": "LG",              "ticker": "003550.KS", "aliases": ["LG지주"]},
    {"name": "SK",              "ticker": "034730.KS", "aliases": ["SK지주"]},
    {"name": "롯데지주",        "ticker": "004990.KS", "aliases": []},
    {"name": "한화",            "ticker": "000880.KS", "aliases": ["한화지주"]},
    {"name": "두산",            "ticker": "000150.KS", "aliases": ["두산지주"]},
    {"name": "CJ올리브영",      "ticker": "없음",       "aliases": []},  # 비상장
    {"name": "HD현대마린솔루션","ticker": "443060.KS", "aliases": []},
    {"name": "에스엠코어",      "ticker": "007820.KQ", "aliases": []},
    {"name": "이오테크닉스",    "ticker": "039030.KQ", "aliases": []},
    {"name": "파크시스템스",    "ticker": "140860.KQ", "aliases": []},
    {"name": "레이크머티리얼즈","ticker": "281740.KQ", "aliases": []},
    {"name": "하나머티리얼즈",  "ticker": "166090.KQ", "aliases": []},
    {"name": "ISC",             "ticker": "095340.KQ", "aliases": []},
    {"name": "RFHIC",           "ticker": "218410.KQ", "aliases": []},
    {"name": "에이팩트",        "ticker": "200710.KQ", "aliases": []},
    {"name": "레인보우로보틱스","ticker": "277810.KQ", "aliases": ["레인보우"]},
    {"name": "유진테크",        "ticker": "084370.KQ", "aliases": []},
    {"name": "원익홀딩스",      "ticker": "030530.KQ", "aliases": []},
    {"name": "한솔케미칼",      "ticker": "014680.KS", "aliases": []},
    {"name": "SKC",             "ticker": "011790.KS", "aliases": []},
    {"name": "롯데에너지머티리얼즈","ticker": "020150.KS","aliases": ["일진머티리얼즈"]},
    {"name": "코윈테크",        "ticker": "282880.KQ", "aliases": []},
    {"name": "나라엠앤디",      "ticker": "051490.KQ", "aliases": []},
    {"name": "엠씨넥스",        "ticker": "097520.KQ", "aliases": []},
    {"name": "대성하이텍",      "ticker": "130580.KQ", "aliases": []},
    {"name": "에스에프에이",    "ticker": "056190.KQ", "aliases": ["SFA"]},
    {"name": "에스티아이",      "ticker": "039440.KQ", "aliases": []},
    {"name": "디이엔티",        "ticker": "079810.KQ", "aliases": []},
    {"name": "더에이치엔에이",  "ticker": "150900.KQ", "aliases": []},
    {"name": "에이치에너지",    "ticker": "102940.KQ", "aliases": []},
    {"name": "씨아이에스",      "ticker": "222080.KQ", "aliases": ["CIS"]},
    {"name": "피엔티",          "ticker": "137400.KQ", "aliases": ["PNT"]},
    {"name": "하나기술",        "ticker": "299030.KQ", "aliases": []},
    {"name": "엔에스",          "ticker": "217820.KQ", "aliases": []},
    {"name": "대보마그네틱",    "ticker": "290670.KQ", "aliases": []},
    {"name": "나인테크",        "ticker": "267320.KQ", "aliases": []},
    {"name": "대화제약",        "ticker": "067080.KQ", "aliases": []},
    {"name": "일양약품",        "ticker": "007570.KS", "aliases": []},
    {"name": "동화약품",        "ticker": "000020.KS", "aliases": []},
    {"name": "부광약품",        "ticker": "003000.KS", "aliases": []},
    {"name": "광동제약",        "ticker": "009290.KS", "aliases": []},
    {"name": "JW중외제약",      "ticker": "001060.KS", "aliases": []},
    {"name": "동국제약",        "ticker": "086450.KQ", "aliases": []},
    {"name": "휴온스",          "ticker": "243070.KQ", "aliases": []},
    {"name": "메디톡스",        "ticker": "086900.KQ", "aliases": []},
    {"name": "압타바이오",      "ticker": "293780.KQ", "aliases": []},
    {"name": "지트리비앤티",    "ticker": "115450.KQ", "aliases": []},
    {"name": "오스템임플란트",  "ticker": "048260.KQ", "aliases": ["오스템"]},
    {"name": "덴티움",          "ticker": "145720.KQ", "aliases": []},
    {"name": "디오",            "ticker": "039840.KQ", "aliases": []},
    {"name": "제이엘케이",      "ticker": "322510.KQ", "aliases": ["JLK"]},
    {"name": "뷰노",            "ticker": "338220.KQ", "aliases": []},
    {"name": "루닛",            "ticker": "328130.KQ", "aliases": []},
    {"name": "딥노이드",        "ticker": "315640.KQ", "aliases": []},
]

# 비상장 등 ticker가 없는 종목 제외
WATCH_STOCKS = [s for s in WATCH_STOCKS if s["ticker"] != "없음"]

# 뉴스 배치 크기 (1회 API 호출당 수집 개수)
NEWS_BATCH_SIZE = 10

# 종목당 최대 수집 뉴스 개수
NEWS_MAX_PER_STOCK = 100

# OpenAI 모델
OPENAI_MODEL = "gpt-4o-mini"
