import requests
import json
from abc import abstractmethod
from geo.models import Point, Route
from web.http import RouteRequest
from web.key import KeyManager

class RouteService:

    key_manager = KeyManager()

    @abstractmethod
    def compute_route(self, route_request: RouteRequest) -> Route:
        pass

class OrsService(RouteService):

    def compute_route(self, route_request: RouteRequest) -> Route:
        url = 'https://api.openrouteservice.org/v2/directions/{}/geojson'.format(route_request.mode)
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Authorization': self.key_manager.token('ors'),
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla'
        }
        payload = {'coordinates': [[p.x, p.y] for p in route_request.points]}
        req = requests.post(url, headers=headers, json=payload)
        feature = req.json()['features'][0]
        distance = feature['properties']['summary']['distance']
        duration = feature['properties']['summary']['duration']
        points = [Point(p[0], p[1]) for p in feature['geometry']['coordinates']]
        return Route(distance, duration, points)

class RouteServiceFactory:

    services = {
        'ors': OrsService()
    }

    def service(self, route_request: RouteRequest) -> RouteService:
        return self.services.get(route_request.service)