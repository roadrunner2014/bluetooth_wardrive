# https://github.com/GoogleCloudPlatform/python-docker <-- Google Base Python/Debian-Jesse image
FROM gcr.io/google_appengine/python
EXPOSE 8080

# Create a virtualenv for the application dependencies. Using the python3.4 flag.
RUN virtualenv /env -p python3.4

# Set the variables fo rthe virtural environment.
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Install depencies
ADD requirements.pip /app/requirements.pip
RUN pip3 install -r /app/requirements.pip

# Add in the Django source code
ADD bt_djangoserver /app/

# TODO: Remove this NODB variable once connected to the mysql instance
ENV NODB 1

# Add the code and start Gunicorn.
CMD export DJANGO_PASSWORD=$(cat /etc/secrets/djangouserpw); gunicorn -b :$PORT bt_djangoserver.wsgi