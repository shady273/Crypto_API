FROM python:3.11

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/src"

CMD ["python", "src/main.py"]

