from datetime import date
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"


class Employee(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str = Field(min_length=1, frozen=True)
    email: EmailStr = Field(pattern=r".+@pydantic\.com$")
    date_of_birth: date = Field(alias="birth_date", repr=False, frozen=True)
    salary: float = Field(gt=0, repr=False)
    department: Department
    elected_benefits: bool
