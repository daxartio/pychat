FROM python:3-alpine

COPY ./ /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./ /opt/pychat/server

WORKDIR /opt/pychat/

CMD ["python", "-m", "server"]