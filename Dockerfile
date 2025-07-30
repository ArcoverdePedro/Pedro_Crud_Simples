FROM python:3.12-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
	&& apk update \
	&& apk add -y --no-cache postgresql-client \
	&& rm -rf /var/cache/apk/*
	
COPY . .

RUN chmod +x /usr/src/app/commands.sh


EXPOSE 8002
