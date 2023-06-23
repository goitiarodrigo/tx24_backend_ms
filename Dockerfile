FROM python:3.9.17-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY .env .

EXPOSE 3000

CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]