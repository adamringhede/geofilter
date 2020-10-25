from typing import Iterator

from app.customers import Customer
from app.geomath import Coordinate, distance_in_km


def is_within(customer: Customer, center: Coordinate, radius: float):
    customer_location = Coordinate(long=customer.longitude, lat=customer.latitude)
    return distance_in_km(center, customer_location) < radius


def filter_customers(customers: Iterator[Customer], center: Coordinate, radius: float) -> Iterator[Customer]:
    for customer in customers:
        if is_within(customer, center, radius):
            yield customer
