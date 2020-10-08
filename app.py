import os

from flask import Flask, request
from flask_json import FlaskJSON, as_json, json_response

from web.http import RouteRequest
from web.route_service import RouteServiceFactory

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
json = FlaskJSON(app)
route_service_factory = RouteServiceFactory()


@app.route('/')
def hello_world():
    app_name = os.getenv('APP_NAME')
    if app_name:
        return '{}'.format(app_name)
    return 'Multiple Points Route'

def compute_route(route_request: RouteRequest):
    service = route_service_factory.service(route_request)
    return service.compute_route(route_request)

def compute_route_response(service: str, mode: str, points):
    try:
        route_request = RouteRequest(service, mode, points)
        return json_response(route=compute_route(route_request).serialize())
    except ValueError as e:
        return json_response(error=str(e), status_=400)
    except Exception as e:
        return json_response(error=str(e), status_=500)

@app.route('/route', methods=['POST'])
@as_json
def compute_route_default():
    return compute_route_response('ors', 'driving-car', request.json['points'])

@app.route('/route/<mode>', methods=['POST'])
@as_json
def compute_route_mode(mode: str):
    return compute_route_response('ors', mode, request.json['points'])

@app.route('/route/<mode>/<service>', methods=['POST'])
@as_json
def compute_route_full(mode: str, service: str):
    return compute_route_response(service, mode, request.json['points'])

if __name__ == '__main__':
    app.run()
