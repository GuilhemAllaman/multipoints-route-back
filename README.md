# Multiple Points Route

Webservice that compute a route between points. Routes can be computed using a large range of middle points. This app uses third-party web services to compute routes (ORS, HERE, MapBox ...)

API written in python using Flask

### Setup

Run `setup.sh` script via command `sh setup.sh` or `./setup.sh`, to create virtual env and download pip dependencies

Set following variables in dev environment:
```
export FLASK_APP=app.py
export FLASK_ENV=development # to enable dev environment 
export APP_NAME=SOME_APP_NAME
```

Don't forget to run `pip freeze > requirements.txt` after adding some pip dependencies to save them

### Build

Build docker image with `docker build -t multipoints-route-back:latest .`

Build and run docker-compose setup with `docker-compose up --build`. This will run flask server with uwsgi exposed on port 9666

### Test

Following commands can be used to test:
```
curl -H "Content-Type: application/json" -X POST -d '{"points": [[2.37113,48.88503],[2.37941,48.88837],[2.37123,48.88379]]}' http://localhost:5000/route/cycling
curl -H "Content-Type: application/json" -X POST -d '{"points": [[2.37113,48.88503],[2.37941,48.88837],[2.37123,48.88379]]}' https://mpr.guilhemallaman.net/route/cycling

```