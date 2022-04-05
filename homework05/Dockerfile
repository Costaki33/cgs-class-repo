FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY startCriteria.txt /app/startCriteria.txt

RUN pip3 install -r /app/startCriteria.txt 
COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]

