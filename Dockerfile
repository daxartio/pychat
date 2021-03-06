FROM python:3.8

ENV POETRY_VERSION=1.0.5
ARG ENVIRONMENT=production

WORKDIR /opt/pychat

COPY ./poetry.lock ./pyproject.toml ./

RUN pip install poetry==${POETRY_VERSION} \
    && poetry config virtualenvs.create false \
    && poetry install $(if test "$ENVIRONMENT" = production; then echo "--no-dev"; fi)

COPY ./server ./server

CMD ["python", "-m", "server"]
