class Point:

    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def serialize(self) -> [float]:
        return [self.x, self.y]

class Segment:

    distance: float
    duration: float
    instruction: str
    name: str
    points: [Point]

    def __init__(self, distance: float, duration: float, instruction: str, name: str, points: [Point]):
        self.distance = distance
        self.duration = duration
        self.instruction = instruction
        self.name = name
        self.points = points

    def serialize(self) -> dict:
        return {
            'dist': self.distance,
            'time': self.duration,
            'instr': self.instruction,
            'name': self.name,
            'points': [p.serialize() for p in self.points]
        }

class Route:

    distance: float
    duration: float
    segments: [Segment]

    def __init__(self, distance: float, duration: float, segments: [Segment]):
        self.distance = distance
        self.duration = duration
        self.segments = segments

    def serialize(self) -> dict:
        return {
            'distance': self.distance,
            'duration': self.duration,
            'segments': [s.serialize() for s in self.segments]
        }
