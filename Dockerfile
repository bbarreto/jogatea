FROM python:3

COPY ./app /app

WORKDIR /app

RUN export CLOUDSDK_INSTALL_DIR=/google-cloud-sdk

RUN curl -sSL https://sdk.cloud.google.com | bash

RUN pip install -r /app/requirements.txt

RUN python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]