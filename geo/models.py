class Point:

    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def serialize(self) -> [float]:
        return [self.x, self.y]

class Route:

    distance: float
    duration: float
    points: [Point]

    def __init__(self, distance: float, duration: float, points: [Point]):
        self.distance = distance
        self.duration = duration
        self.points = points

    def serialize(self) -> dict:
        return {
            'distance': self.distance,
            'duration': self.duration,
            'points': [p.serialize() for p in self.points]
        }

    def start(self) -> Point:
        return self.points[0]

    def end(self) -> Point:
        return self.points[-1]