import os
from flask import Flask, request
from flask_json import FlaskJSON, as_json, jsonify, json_response
from geo.models import Point, Route
from web.http import RouteRequest
from web.routeservice import RouteServiceFactory


app = Flask(__name__)
json = FlaskJSON(app)
route_service_factory = RouteServiceFactory()


@app.route('/')
def hello_world():
    app_name = os.getenv('APP_NAME')
    if app_name:
        return 'Hello from {}!'.format(app_name)
    return 'Hello from Multiple Points Route API!'

@app.route('/route', methods=['POST'])
@as_json
def compute_route():
    payload = request.json
    route_request = RouteRequest(payload['service'], payload['mode'], payload['coordinates'])
    service = route_service_factory.service(route_request)
    route = service.compute_route(route_request)
    return json_response(route=route.serialize())


@app.route('/test/point')
@as_json
def create_point():
    return json_response(point=Point(4.3, 3.4).serialize())

@app.route('/test/route')
@as_json
def create_route():
    route = Route(666, 420, [Point(i * 0.5, i * 1.5) for i in range(10)])
    return json_response(route=route.serialize())

if __name__ == '__main__':
    app.run()
