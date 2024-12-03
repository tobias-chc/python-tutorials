from fastapi import FastAPI
from pydantic import BaseModel, Field


"""
To run this app execute the following:

uvicorn fastapi_app:app --reload

Then go to:

http://127.0.0.1:8000/countries
"""

app = FastAPI()


def _find_next_id() -> int:
    return max(country.country_id for country in countries) + 1


class Country(BaseModel):
    country_id: int = Field(default_factory=_find_next_id, alias="id")
    name: str
    capital: str
    area: int


countries = [
    Country(id=1, name="Thailand", capital="Bangkok", area=513120),
    Country(id=2, name="Australia", capital="Canberra", area=7617930),
    Country(id=3, name="Egypt", capital="Cairo", area=1010408),
]


@app.get("/countries")
async def get_countries() -> list[Country]:
    return countries


@app.post("/countries", status_code=201)
async def add_country(country: Country) -> Country:
    countries.append(country)
    return country


"""
POST example

# -X: set the http method
# -H: set the http header
# -d: set the content

curl -i http://127.0.0.1:8000/countries \
-X POST \
-H "Content-Type: application/json" \
-d '{"name": "Germany", "capital": "Berlin", "area": 357022}' \
-w '\n'

# Expected output:

HTTP/1.1 201 Created
date: Tue, 03 Dec 2024 23:19:31 GMT
server: uvicorn
content-length: 58
content-type: application/json

{"id":4,"name":"Germany","capital":"Berlin","area":357022}
"""
