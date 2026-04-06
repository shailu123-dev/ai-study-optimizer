FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install openenv-core

EXPOSE 8080

CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8080"]
ENV ENABLE_WEB_INTERFACE=true