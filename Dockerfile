FROM python:3.10.11
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD exec gunicorn minders.wsgi:application --bind 0.0.0.0:80 --workers 3