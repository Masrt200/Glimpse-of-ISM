FROM node:14.16.0-alpine

WORKDIR /app
COPY package.json .

ENV NODE_ENV production
ENV PORT 9999
RUN npm install

COPY . .

EXPOSE 9999

CMD ["node", "/app/index.js"]