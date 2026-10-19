FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install requests

CMD ["python", "main.py"]