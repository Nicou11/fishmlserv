#FROM nicou11/fishmlserv:0.9.1
FROM python:3.11
#FROM python:3.8.19-slim-bullseye
#FROM python:3.8.19-alpine3.20

WORKDIR /code

#COPY . /code/
COPY src/fishmlserv/knn.py /code/

#COPY ./requirements.txt /code/requirements.txt
#COPY requirements.txt /code/

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --no-cache-dir --upgrade git+https://github.com/Nicou11/fishmlserv.git@1.6.0/python3.11
# 모델서빙만(의존성의 위 BASE image에서 모두 설치함)


CMD ["uvicorn", "knn:app", "--host", "0.0.0.0", "--port", "8080"]
# 모델 서빙을 위해 API 구동을 위한 FastAPI RUN
