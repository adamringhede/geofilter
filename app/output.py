from typing import Iterator
import json
from app.customers import Customer


def format_customer(customer: Customer) -> str:
    return json.dumps({'name': customer.name, 'user_id': customer.user_id})


def write_customers_to_file(customers: Iterator[Customer], output_file_path: str):
    with open(output_file_path, "w") as out:
        for customer in customers:
            out.write(f"{format_customer(customer)}\n")
