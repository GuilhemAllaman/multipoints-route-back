class Point:

    lon = float
    lat = float

    def __init__(self, lon: float, lat: float):
        self.lon = lon
        self.lat = lat

    def serialize(self) -> dict:
        return {
            'lon': self.lon,
            'lat': self.lat
        }