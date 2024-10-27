FROM python:3.4

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

WORKDIR /params
COPY params ./
RUN pip install -r requirements.txt --no-cache-dir

WORKDIR /app
COPY app ./
COPY cmd.sh /cmd.sh

EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]