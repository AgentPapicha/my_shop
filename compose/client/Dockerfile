FROM node:20-alpine

ARG PROJ_DIR=/vue_proj

RUN mkdir -p ${PROJ_DIR}
COPY ./shop_vue $PROJ_DIR

WORKDIR ${PROJ_DIR}

RUN npm install -g npm

COPY ./shop_vue/package.json $PROJ_DIR
COPY ./shop_vue/package-lock.json $PROJ_DIR

RUN npm install

CMD ["npm", "run", "serve"]