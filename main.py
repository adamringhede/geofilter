from app.customers import CustomersRepo
from app.filter import filter_customers
from app.output import write_customers_to_file
from app.locations import dublin
import os


def main():
    input_file_path = os.path.join("data", "customers.txt")
    output_file_path = "output.txt"
    max_distance_km = 100

    repo = CustomersRepo(input_file_path)
    customers = filter_customers(repo.find_all(), dublin, max_distance_km)
    write_customers_to_file(customers, output_file_path)


if __name__ == '__main__':
    main()
