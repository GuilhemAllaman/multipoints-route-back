from geo.models import Point

class RouteRequest:

    service: str
    mode: str
    points: [Point]

    def __init__(self, service: str, mode: str, points: [[float, float]]):
        self.service = service
        self.mode = mode
        self.points = [Point(p[0], p[1]) for p in points]