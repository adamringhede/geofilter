import os
import json
from app.customers import CustomersRepo
from unittest import TestCase


class TestCustomers(TestCase):
    def test_find_all(self):
        repo = CustomersRepo(_test_file_path("customers.txt"))
        customers = list(repo.find_all())
        self.assertGreater(len(customers), 0, "no customers found")

    def test_find_all_bad_data(self):
        repo = CustomersRepo(_test_file_path("bad_data.txt"))
        self.assertRaises(json.decoder.JSONDecodeError, lambda: list(repo.find_all()))


def _test_file_path(path: str):
    return os.path.join(os.path.dirname(__file__), "../data/", path)
