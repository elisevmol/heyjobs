FROM alpine

RUN apk add --update python py-pip
RUN pip install -r requirements.txt

COPY simpleapp.py /src/simpleapp.py

EXPOSE  5432