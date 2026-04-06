Name: Zakiya Williams

Module Info: Module  Assignment 10: Building an Automated CI/CD Pipeline Due on 04/5/2026

Approach:

For the flask API, I created an single route /incidents/<unit_type> that accepts a path parameter of either escalators or elevators. Inside the get_incidents function, I made a GET request to the WMATA ElevatorIncidents api usingthe API Key in the request headers and converted the response to JSON. I then created an empty list and looped through all the incidents, checking each incident's unit type. If the unit type matched the requested type (escalator or elevator), I built a new dictionary with the 4 fields (station code, station name, unit name, and unit type) and appended it to the resutls list. Lastly, I converted the list to a JSON string and returned it as the endpoint response.

Fro the unit tests, I created a WMATATest class that inherits from unittest.TestCase. In setUp, I initialized a flask test client so tests could make http requests without needinga live server. I wrote 4 test methods.
1. test_http_success - sends the GET requests to both endpoints and asserts both return status code 200
2. test_required_fields - parses the escalators response and loops through each incident asserting all 4 required fields are present
3. test_escalators - loops through the escalators response and asserts every incident has unit type equal to escalator
4. test_elevators - loops through the elevators response and asserts every incident has unit type equal to elevator

Known bugs: n/a
Citations: n/a
