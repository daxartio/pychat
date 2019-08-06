FROM node:carbon as builder

WORKDIR /opt/pychat/web

COPY ./package*.json ./
COPY ./yarn.lock ./

RUN npm install

COPY ./src ./src
COPY ./public ./public

RUN npm run build

FROM nginx:1.14

COPY --from=builder /opt/pychat/web/build /usr/share/nginx/html/
COPY default.conf /etc/nginx/conf.d/default.conf