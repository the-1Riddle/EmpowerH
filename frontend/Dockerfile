FROM node:20 AS frontend-builder

WORKDIR /app

COPY ./frontend /app

RUN npm install

RUN npm run build

CMD ["npm", "start"]