FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV WORK_DIR /usr/src/app
RUN apt-get update \
    && apt-get install -y vim \
    && cd /usr/src \
    && mkdir -p app \
    && mkdir -p app/logs
WORKDIR $WORK_DIR
COPY requirements.txt $WORK_DIR/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r $WORK_DIR/requirements.txt
COPY . $WORK_DIR
COPY manage.py $WORK_DIR

# RUN chmod +x $WORK_DIR/entrypoint.sh
# RUN chmod +x $WORK_DIR/entrypoint_job.sh

EXPOSE 8000
EXPOSE 443
#ENTRYPOINT [ "/bin/sh","-c" ]
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
