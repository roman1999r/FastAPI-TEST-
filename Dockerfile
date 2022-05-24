#
FROM python:3.7


#
WORKDIR /app

#
COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install requirements.txt
#
COPY  . .

#
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
