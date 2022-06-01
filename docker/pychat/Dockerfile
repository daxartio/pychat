FROM node:carbon as builder

WORKDIR /opt/pychat/web

COPY ./web/package*.json ./
COPY ./web/yarn.lock ./

RUN npm install

COPY ./web/src ./src
COPY ./web/public ./public

RUN npm run build

FROM python:3.10

ENV POETRY_VERSION=1.1.13

WORKDIR /opt/pychat

COPY ./poetry.lock ./pyproject.toml ./

RUN pip install poetry==${POETRY_VERSION} \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

COPY --from=builder /opt/pychat/web/build /opt/pychat/web/build

COPY ./server ./server

CMD ["python", "-m", "server"]
