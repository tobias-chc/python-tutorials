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


if __name__ == "__main__":

    # Creating models from: explict values, dict
    models_examples()
