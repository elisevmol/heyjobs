FROM python:2.7

RUN pip install BeautifulSoup

COPY run.py run.py

CMD [ "python", "run.py" ]
