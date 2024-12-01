import json
from tutorials.pydantic_demo.models import Employee


def models_examples():
    # EXAMPLE 1: Object instantiation using explicit values
    test_employee = Employee(
        name="Tobias",
        email="tobias@pydantic.com",
        date_of_birth="1995-12-02",
        salary=1000,
        department="IT",
        elected_benefits=False,
    )

    print(f"Created Employee: {test_employee}\n")

    # EXAMPLE 2: Object instantiation from dict
    employee_as_dict = {
        "name": "Tobias",
        "email": "tobias@pydantic.com",
        "date_of_birth": "1995-12-02",
        "salary": 1000,
        "department": "IT",
        "elected_benefits": False,
    }
    employee_from_dict = Employee.model_validate(employee_as_dict)
    print(f"Created Employee: {employee_from_dict}\n")

    # EXAMPLE 3: Go from object to dict represantation
    ## Serialize the object to JSON string
    json_string = employee_from_dict.model_dump_json()
    ## Deserialize the JSON string back into a dictionary:
    employee_dump_dict = json.loads(json_string)
    ## Remove the 'employee_id' key from the dictionary
    employee_dump_dict.pop("employee_id")

    print(f"Is the dict dump method ok: {employee_dump_dict == employee_as_dict}", "\n")


def fields_example():
    # EXAMPLE 1: Incorrect data
    print("--- EXAMPLE 1: Incorrect data ---")
    incorrect_employee_data = {
        "name": "",
        "email": "tobias@pydantik.com",
        "birth_date": "1995-12-02",
        "salary": -10,
        "department": "IT",
        "elected_benefits": True,
    }

    try:
        Employee.model_validate(incorrect_employee_data)
    except Exception as e:
        print(f"Error: {e}\n")

    # EXAMPLE 2: Correct data
    print("\n--- EXAMPLE 2: Correct Data ---")
    employee_data = {
        "name": "Tobias",
        "email": "tobias@pydantic.com",
        "birth_date": "1995-12-02",
        "salary": 1000,
        "department": "ENGINEERING",
        "elected_benefits": True,
    }

    test_employee = Employee.model_validate(employee_data)
    print(f"Created Employee: {test_employee}\n")

    # EXAMPLE 2.1: Getting `repr=False` values
    print("--- EXAMPLE 2.1: Getting `repr=False` values ---")
    print(f"Getting DoB value: {test_employee.date_of_birth}")
    print(f"Getting salary value: {test_employee.salary}\n")

    # EXAMPLE 2.2: Updating `frozen=True` values
    print("--- EXAMPLE 2.2: Updating `frozen=True` values ---")
    try:
        test_employee.name = "Jesus"
    except Exception as e:
        print(f"Error: {e}\n")


if __name__ == "__main__":

    # Creating models from: explict values, dict
    models_examples()

    # Using fields
    fields_example()
