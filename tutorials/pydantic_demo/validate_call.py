import time
from typing import Annotated
from pydantic import PositiveFloat, Field, EmailStr, validate_call


# Check: https://docs.pydantic.dev/latest/concepts/strict_mode/#using-field-as-an-annotation
@validate_call
def send_invoice(
    client_name: Annotated[str, Field(min_length=1)],
    client_email: EmailStr,
    items_purchased: list[str],
    amount_owed: PositiveFloat,
) -> str:
    email_str = f"""
    Dear {client_name}, \n
    Thank you for choosing xyz inc! you
    owe ${amount_owed:,.2f} for the following items: \n
    {items_purchased}
    """

    print(f"Sending email to {client_email} ...")
    time.sleep(2)

    return email_str
