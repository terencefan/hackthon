FROM python:2

WORKDIR /usr/src/hackthon

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 7020

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:7020"]