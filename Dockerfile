FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV username=your_user_name
ENV password=your_user_password

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
