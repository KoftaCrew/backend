FROM python:3.10-bullseye
ADD . /usr/src/app
WORKDIR /usr/src/app

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN apt-get install -y unixodbc-dev
RUN apt-get clean -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD exec gunicorn Backend.wsgi:application --bind 0.0.0.0:80 --workers 3