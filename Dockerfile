FROM python:3.8

ENV POETRY_VERSION=1.0.5 \
    ENVIRONMENT=production

WORKDIR /opt/pychat

COPY ./poetry.lock ./pyproject.toml ./

RUN pip install poetry==${POETRY_VERSION} \
    && poetry config virtualenvs.create false \
    && poetry install  $(test "$ENVIRONMENT" == production && echo "--no-dev")

COPY ./server ./server

CMD ["python", "-m", "server"]
