FROM python:3.10

ENV POETRY_VERSION=1.1.13
ARG ENVIRONMENT=production

WORKDIR /opt/pychat

COPY ./poetry.lock ./pyproject.toml ./

RUN pip install poetry==${POETRY_VERSION} \
    && poetry config virtualenvs.create false \
    && poetry install

COPY ./server ./server

CMD ["python", "-m", "server"]
