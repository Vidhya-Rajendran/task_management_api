FROM python:3.10-bullseye

WORKDIR /code

COPY requirements.txt .

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_PROGRESS_BAR=off

RUN pip install -r requirements.txt

COPY ./app ./app
COPY .env .env

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]