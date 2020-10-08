from geo.models import Point

class RouteRequest:

    service: str
    mode: str
    points: [Point]

    def __init__(self, service: str, mode: str, points: [[float, float]]):
        if (len(points) < 2):
            raise ValueError("You must specify at least 2 points")
        self.service = service
        self.mode = mode
        self.points = [Point(p[0], p[1]) for p in points]