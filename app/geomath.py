from math import cos, sin, acos, radians
from dataclasses import dataclass

MEAN_EARTH_RADIUS = 6371.0088


@dataclass
class Coordinate:
    lat: float
    long: float


def distance_in_km(a: Coordinate, b: Coordinate):
    return MEAN_EARTH_RADIUS * central_angle_on_sphere(a, b)


def central_angle_on_sphere(a: Coordinate, b: Coordinate):
    """ Based on https://en.wikipedia.org/wiki/Great-circle_distance """

    phi_a, lambda_a = radians(a.lat), radians(a.long)
    phi_b, lambda_b = radians(b.lat), radians(b.long)

    return acos(sin(phi_a) * sin(phi_b) +
                cos(phi_a) * cos(phi_b) * cos(lambda_a - lambda_b))
