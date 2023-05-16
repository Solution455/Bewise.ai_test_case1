import os
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_text = Column(String)
    answer_text = Column(String)
    created_at = Column(DateTime, default=datetime.now)


engine = create_engine(f'postgresql+psycopg2://{os.getenv("username")}:{os.getenv("password")}@db/test_case')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def get_question_by_id(question_id: int) -> Question:
    """
    :param question_id:
    :return Question object::
    """
    question = session.query(Question).get(question_id)
    return question


def get_question_by_text(question_text: str) -> Question:
    """
    :param question_text:
    :return Question object::
    """
    question = session.query(Question).filter_by(question_text=question_text).first()
    return question


def save_question(question_text: str, answer_text: str) -> Question:
    """
    Saving questions
    :param question_text:
    :param answer_text:
    :return Question object:
    """
    question = Question(
        question_text=question_text,
        answer_text=answer_text
    )
    session.add(question)
    session.commit()
    return question
