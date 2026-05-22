# 실습 5 - Docker 과제

## 제출자 정보

| 항목 | 내용 |
|------|------|
| 학번 | 2021603038 |
| 이름 | 송호성 |
| 소속 | 광운대학교 수학과 (정보융합학부 복수전공) |

## 과제 소개

FastAPI 수강기록 관리 API를 Docker 컨테이너로 빌드하여 AWS EC2 환경에 배포합니다.  
외부 80번 포트와 컨테이너 내부 8000번 포트를 매핑하여 브라우저에서 접속 가능하도록 구성합니다.

## 실행 방법

### 요구 사항

- Docker

### 설치 및 실행

```bash
# 저장소 클론
git clone https://github.com/Hoseong21/oss-docker-project.git
cd oss-docker-project

# Docker 이미지 빌드
sudo docker build -t fastapi-courses .

# 컨테이너 실행 (외부 80 → 내부 8000 매핑, 자동 재시작 설정)
sudo docker run -d \
  --name fastapi-app \
  -p 80:8000 \
  --restart=always \
  fastapi-courses

# 컨테이너 실행 확인
sudo docker ps
```

### 접속

브라우저에서 `http://[EC2 퍼블릭 IP]/courses` 로 접속