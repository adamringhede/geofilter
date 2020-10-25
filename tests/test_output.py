from unittest import TestCase
import tempfile

from app.customers import Customer
from app.output import write_customers_to_file, format_customer

customer = Customer(user_id=27, name="Enid Gallagher", latitude=54.1225, longitude=-8.143333)


class TestOutput(TestCase):
    def test_format(self):
        formatted = format_customer(customer)
        self.assertEqual('{"name": "Enid Gallagher", "user_id": 27}', formatted)

    def test_write_to_file(self):
        customers = [customer]
        output_path = tempfile.mktemp()
        write_customers_to_file(customers, output_path)
        with open(output_path, "r") as file:
            first_line = file.readline()
            self.assertEqual('{"name": "Enid Gallagher", "user_id": 27}\n', first_line)

