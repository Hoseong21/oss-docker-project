"""
FastAPI 수강기록 관리 API
실행: python main.py
"""

import json
import uvicorn
from fastapi import FastAPI
from model import Course

app = FastAPI(title="수강기록 API")

@app.get("/courses")
async def get_courses():
    """전체 수강기록 반환"""
    with open("courses.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


@app.post("/courses")
async def add_course(course: Course):
    """새 수강기록 추가"""
    # 1. 기존 파일 읽기
    with open("courses.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 2. 새 과목 추가
    data.append(course.model_dump())
    
    # 3. 파일에 다시 저장
    with open("courses.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return {"message": "수강기록이 추가되었습니다.", "course": course.model_dump()}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)