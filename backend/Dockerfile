FROM python:3.8.12-alpine3.15

WORKDIR /backend

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8888
CMD ["python3", "app.py"]