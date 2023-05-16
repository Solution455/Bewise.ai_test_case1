import requests
from fastapi import FastAPI

from db import get_question_by_id, get_question_by_text, save_question
from requests_serializer import RequestBody

app = FastAPI()


@app.post("/quiz")
def get_quiz_questions(request_body: RequestBody):
    """
    функция обработчик POST запросов для обращения к апи квиза, возвращает ответ в формате JSON
    :param request_body:
    :return JSON::
    """
    question = get_question_by_id(request_body.questions_num)
    if question:
        return {
            "id": question.id,
            "question_text": question.question_text,
            "answer_text": question.answer_text,
            "created_at": question.created_at
        }

    response = requests.get(f"https://jservice.io/api/random?count={request_body.questions_num}")
    data = response.json()

    for item in data:
        existing_question = get_question_by_text(item["question"])
        if existing_question:
            continue

        question = save_question(
            question_text=item["question"],
            answer_text=item["answer"]
        )

        return {
            "id": question.id,
            "question_text": question.question_text,
            "answer_text": question.answer_text,
            "created_at": question.created_at
        }

    return {}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
