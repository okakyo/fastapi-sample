FROM python:3.8 AS builder

WORKDIR /src

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv 

RUN pipenv install --system

CMD ["uvicorn", "main:app", "--reload","--host", "0.0.0.0", "--port", "8000"]
