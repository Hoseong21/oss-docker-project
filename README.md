# 실습 4 - FastAPI 과제

## 제출자 정보

| 항목 | 내용 |
|------|------|
| 학번 | 2021603038 |
| 이름 | 송호성 |
| 소속 | 광운대학교 수학과 (정보융합학부 복수전공) |

## 과제 소개

JSON 파일 기반 수강기록 관리 REST API 서버입니다.
FastAPI를 사용해 GET / POST 엔드포인트를 구현하고, Postman으로 동작을 검증합니다.

## 실행 방법

### 요구 사항

- Python 3.9+
- FastAPI
- Uvicorn

### 설치 및 실행

```bash
# 저장소 클론
git clone https://github.com/Hoseong21/oss-fastapi-project.git
cd oss-fastapi-project

# 가상환경 생성 및 활성화 (권장)
python -m venv venv
source venv/bin/activate  # macOS/Linux

# 의존성 설치
pip install -r requirements.txt

# FastAPI 서버 실행
python main.py
```