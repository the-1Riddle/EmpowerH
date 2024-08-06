FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@5.0.8 -g

COPY package.json .
COPY package-lock.json .
RUN npm install

CMD ["npm", "run", "serve"]

# this would be used for production

# Stage 1: Build
# FROM node:20 AS builder

# WORKDIR /app

# COPY ./frontend/package.json ./frontend/package-lock.json ./
# RUN npm install

# COPY ./frontend ./
# RUN npm run build

# Stage 2: Serve
# FROM nginx:stable-alpine AS production

# COPY --from=builder /app/dist /usr/share/nginx/html

# Copy custom Nginx configuration if you have one
# COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

# EXPOSE 80

# CMD ["nginx", "-g", "daemon off;"]
