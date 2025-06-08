FROM python:3.12-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    && apk update \
    && apk add --no-cache postgresql-client \
    && rm -rf /var/cache/apk/*

COPY . .

EXPOSE 8002 8005