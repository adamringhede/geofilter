from dataclasses import dataclass
from typing import List, Dict, Generator
import os
import json


FILE_LOCATION = os.path.join(os.path.dirname(__file__), "../data/customers.txt")


@dataclass
class Customer():
    user_id: int
    name: str
    latitude: float
    longitude: float


class CustomersRepo(object):
    def __init__(self, file_path: str):
        self._file_path = file_path

    def find_all(self) -> Generator[Customer, None, None]:
        return self._load_customers()

    def _load_customers(self) -> Generator[Customer, None, None]:
        with open(self._file_path, 'r') as file:
            for line in file:
                customer_data = json.loads(line)
                customer = self._parse_customer(customer_data)
                yield customer


    @staticmethod
    def _parse_customer(data: Dict):
        return Customer(
            user_id=data['user_id'],
            name=data['name'],
            latitude=float(data['latitude']),
            longitude=float(data['longitude'])
        )
