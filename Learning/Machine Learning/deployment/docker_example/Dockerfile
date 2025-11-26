FROM node:19-alpine

# COPY <src> on our machine <dest> in the container
COPY package.json /app/
COPY src /app/

# Equivalent of cd
WORKDIR /app

RUN npm install

# Starts application
CMD ["node", "server.js"]