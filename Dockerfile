#
FROM python:3.8

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
#

EXPOSE 8000
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /app
COPY . /app

