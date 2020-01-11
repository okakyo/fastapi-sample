FROM python:3.8.0-alpine
WORKDIR /api
# python3 pipのインストール
RUN apk add build-base libffi-dev
COPY ./requirements.txt .
EXPOSE 8000
RUN pip install --upgrade setuptools && pip install -r requirement.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
