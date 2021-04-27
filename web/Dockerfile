FROM node:15

# non-root user setup
WORKDIR /opt/web
RUN chown node:node /opt/web
USER node

# install the dependencies
COPY package.json package-lock.json ./
RUN npm ci
CMD ["npm", "start"]
