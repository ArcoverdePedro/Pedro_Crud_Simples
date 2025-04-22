FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/

RUN apt update\
    && apt install -y --no-install-recommends postgresql-client build-essential libpq-dev\
    && rm -rf /var/lib/apt/lists/*\
    && pip install --no-cache-dir -r  requirements.txt

COPY . .

EXPOSE 8002 8006

CMD ["python","manage.py","runserver","0.0.0.0:8000"]