# Как запустить контейнер:
# Из директории с Dockerfile введите:
# docker build -t ping_pong_app .
# docker run -p 8000:8000 ping_pong_app

FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
