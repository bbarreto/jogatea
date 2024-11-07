FROM python:3

COPY . /app

WORKDIR /app

RUN pip install -r /app/requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]