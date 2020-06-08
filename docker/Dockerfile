FROM python:3.8.1

RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /usr/src/app
COPY . .
RUN pip install -r docker/requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
