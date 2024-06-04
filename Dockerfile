FROM python 

RUN pip install poetry

WORKDIR /app

COPY . .

COPY backend/ /app/

COPY frontend/ /app/frontend/

EXPOSE 8000

RUN poetry install


CMD poetry run python manage.py runserver 0.0.0.0:8000