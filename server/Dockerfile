FROM python:3-alpine

COPY ./ /opt/pychat/server
WORKDIR /opt/pychat/

RUN pip install -r ./server/requirements.txt

CMD ["python", "-m", "server.app"]