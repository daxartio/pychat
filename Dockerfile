FROM python:3.8.1

COPY ./poetry.lock /opt/pychat/poetry.lock
COPY ./pyproject.toml /opt/pychat/pyproject.toml
RUN cd /opt/pychat && pip install poetry==1.0.3 && poetry install

COPY ./server /opt/pychat/server

WORKDIR /opt/pychat/

CMD ["poetry", "run", "python", "-m", "server"]