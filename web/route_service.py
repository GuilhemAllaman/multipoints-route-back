from abc import abstractmethod

import requests

from geo.models import Point, Segment, Route
from web.http import RouteRequest


class RouteService:

    @abstractmethod
    def format_transport_mode(self, req_mode: str) -> str:
        pass

    @abstractmethod
    def compute_route(self, route_request: RouteRequest) -> Route:
        pass

class OrsService(RouteService):

    tokens_counter = 0
    tokens = [
        '5b3ce3597851110001cf6248825666083b1e45f79ea80b6d26f8b0a2'
    ]

    transport_mode_switcher = {
        'car': 'driving-car',
        'driving': 'driving-car',
        'bicycle': 'cycling-regular',
        'bike': 'cycling-regular',
        'cycling': 'cycling-regular',
        'foot': 'foot-walking',
        'pedestrian': 'foot-walking',
        'walking': 'foot-walking'
    }

    def get_auth(self) -> str:
        token = self.tokens[self.tokens_counter]
        self.tokens_counter = (self.tokens_counter + 1) % len(self.tokens)
        return token

    def format_transport_mode(self, req_mode: str) -> str:
        if not req_mode in self.transport_mode_switcher:
            raise ValueError('Unknown transport mode <{}>'.format(req_mode))
        return self.transport_mode_switcher.get(req_mode)

    def compute_route(self, route_request: RouteRequest) -> Route:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Authorization': self.get_auth(),
            'Content-Type': 'application/json',
            'User-Agent': 'MPR-flask'
        }
        url = 'https://api.openrouteservice.org/v2/directions/{}/geojson'.format(self.format_transport_mode(route_request.mode))
        payload = {'coordinates': [[p.x, p.y] for p in route_request.points]}
        req = requests.post(url, headers=headers, json=payload)

        feature = req.json()['features'][0]
        distance = feature['properties']['summary']['distance']
        duration = feature['properties']['summary']['duration']
        points = [Point(p[0], p[1]) for p in feature['geometry']['coordinates']]

        segments = []
        for segment in feature['properties']['segments']:
            print(segment)
            for step in segment['steps']:
                segments.append(Segment(step['distance'], step['duration'], step['instruction'], step['name'], [points[i] for i in step['way_points']]))

        return Route(distance, duration, segments)

class RouteServiceFactory:

    services = {
        'ors': OrsService()
    }

    def service(self, route_request: RouteRequest) -> RouteService:
        if not route_request.service in self.services:
            raise ValueError('Unknown service <{}>'.format(route_request.service))
        return self.services.get(route_request.service)