from pydantic import BaseModel


class RequestBody(BaseModel):
    questions_num: int
