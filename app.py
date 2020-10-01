from flask import Flask
from flask_json import FlaskJSON, as_json, jsonify, json_response
from geo.point import Point
from geo.route import Route

app = Flask(__name__)
json = FlaskJSON(app)


@app.route('/')
def hello_world():
    return 'Multiple points routing API'


@app.route('/test/point')
@as_json
def create_point():
    return json_response(point=Point(4.3, 3.4).serialize())

@app.route('/test/route')
@as_json
def create_route():
    route = Route('test-route', [Point(i * 0.5, i * 1.5) for i in range(10)])
    return json_response(route=route.serialize())

if __name__ == '__main__':
    app.run()
