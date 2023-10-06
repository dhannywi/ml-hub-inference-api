FROM python:3.11.4

COPY ml_requirements.txt /ml_requirements.txt

RUN pip install -r ml_requirements.txt

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT ["python3", "main.py"]