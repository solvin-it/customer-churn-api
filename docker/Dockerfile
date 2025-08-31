FROM python:3.12-slim

WORKDIR /app

COPY ../requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ../app ./app

COPY ../models ./models

COPY ../data ./data

CMD ["fastapi", "run", "app/main.py", "--port", "80"]

EXPOSE 8000
