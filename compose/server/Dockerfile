FROM python:3.11-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG PROJ_DIR=/my_proj

RUN mkdir -p ${PROJ_DIR}
COPY ./my_project $PROJ_DIR

WORKDIR ${PROJ_DIR}

RUN pip install -r requirements.txt

#RUN python3 -m virtualenv --python=python3 virtualenv
#
#ENV PYTHONPATH "${PYTHONPATH}:/my_project"
COPY ./my_project/db.json ${PROJ_DIR}/
COPY ./compose/server/entry.sh /entry.sh

RUN chmod +x /entry.sh

ENTRYPOINT ["/entry.sh"]