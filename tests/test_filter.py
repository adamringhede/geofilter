from unittest import TestCase

from app.customers import Customer
from app.locations import dublin
from app.filter import filter_customers

customers = [
    # About 150 km from dublin
    Customer(user_id=27, name="Enid Gallagher", latitude=54.1225, longitude=-8.143333)
]


class TestFilter(TestCase):
    def test_filter_exclude_customer(self):
        filtered = list(filter_customers(customers, dublin, 100))
        self.assertEquals(0, len(filtered))

    def test_include_customer(self):
        filtered = list(filter_customers(customers, dublin, 160))
        self.assertEquals(1, len(filtered))
