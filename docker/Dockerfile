# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1

# 작업 폴더 설정
WORKDIR /home
# 라이브러리 설치
COPY docker/requirements.txt /home/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 개발용으로 entrypoint.sh 파일를 연결
CMD ["sh", "/home/entrypoint.sh"]