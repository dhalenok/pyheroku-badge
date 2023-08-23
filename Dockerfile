FROM python:3.11-slim-bullseye as python-base

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./pyheroku_badge /code/pyheroku_badge
COPY ./public /code/public

CMD ["uvicorn", "pyheroku_badge.main:app", "--host", "0.0.0.0", "--port", "8080"]