from flask import Flask, Response, request, jsonify

"""
To run this app execute the following:

flask --app flask_app run --debug

Then go to:

http://127.0.0.1:5000/countries
"""

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]


def _find_next_id() -> int:
    return max(country["id"] for country in countries) + 1


@app.get("/countries")
def get_countries() -> Response:
    return jsonify(countries)


@app.post("/countries")
def add_country() -> tuple[dict, int]:
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201

    return {"error": "Request must be JSON"}, 415


@app.get("/country")
def get_country():
    return countries[1]


"""
POST example

# -X: set the http method
# -H: set the http header
# -d: set the content

curl -i http://127.0.0.1:5000/countries \
-X POST \
-H "Content-Type: application/json" \
-d '{"name": "Germany", "capital": "Berlin", "area": 357022}'

# Expected output:

HTTP/1.1 201 CREATED
Server: Werkzeug/3.1.3 Python/3.13.0
Date: Tue, 03 Dec 2024 22:50:32 GMT
Content-Type: application/json
Content-Length: 76
Connection: close

{
  "area": 357022,
  "capital": "Berlin",
  "id": 4,
  "name": "Germany"
}
"""
