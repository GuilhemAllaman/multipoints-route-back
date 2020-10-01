from geo.point import Point

class Route:

    name = str
    points = [Point]

    def __init__(self, name: str, points: [Point]):
        self.name = name
        self.points = points

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'start': self.start().serialize(),
            'end': self.end().serialize(),
            'points': [p.serialize() for p in self.points]
        }

    def add_point(self, point: Point):
        self.points.append(point)

    def start(self) -> Point:
        return self.points[0]

    def end(self) -> Point:
        return self.points[-1]