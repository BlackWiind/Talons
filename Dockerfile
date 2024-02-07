FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Talons


COPY ./req.txt /req.txt
RUN pip install -r /req.txt

COPY . /Talons

EXPOSE 8066