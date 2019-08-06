FROM node:carbon

WORKDIR /opt/pychat/web

COPY ./package*.json ./
COPY ./yarn.lock ./

RUN npm install

COPY ./src ./src
COPY ./public ./public

CMD ["npm", "run", "start"]