FROM python:3.11-rc-alpine3.16

ADD ./dd-app /dd-app
ADD ./requirements.txt /dd-app
ADD ./run.sh /run.sh
ADD ./instance /instance

RUN chmod +x /run.sh
RUN pip install -r /dd-app/requirements.txt
RUN pip install gunicorn

WORKDIR /

CMD ["./run.sh"]
#CMD ["gunicorn","-b", "0.0.0.0:8080","--log-level","debug", "dd-app:create_app()"]