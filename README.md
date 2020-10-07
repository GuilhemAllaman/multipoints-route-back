# Multiple Points Route

Webservice that compute a route between points. Routes can be computed using a large range of middle points. This app uses third-party web services to compute routes (ORS, HERE, MapBox ...)

API written in python using Flask

### Setup

Run `setup.sh` script via command `sh setup.sh` or `./setup.sh`, to create virtual env and download pip dependencies

Set following variables :
```
export FLASK_APP=app.py
export FLASK_ENV=development # to enable dev environment 
export APP_NAME=SOME_APP_NAME
```

Don't forget to run `pip freeze > requirements.txt` after adding some pip dependencies to save them

### Build

Build docker image with `docker build -t multipoints-route-back:latest .`

Build and run docker-compose setup with `docker-compose up --build`. This will run flask server with uwsgi exposed on port 9666
