import flask
import requests
import json

app = flask.Flask(__name__)

WMATA_API_KEY = "cde46e9f5c8147618ab1ebfa14bb189c"


@app.route('/incidents/<unit_type>', methods=['GET'])
def get_incidents(unit_type):
    url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
    headers = {"api_key": WMATA_API_KEY}

    response = requests.get(url, headers=headers)
    data = response.json()

    incidents = data["ElevatorIncidents"]
    result = []

    for incident in incidents:
        if unit_type == "escalators" and incident["UnitType"] == "ESCALATOR":
            machine = {}
            machine["StationCode"] = incident["StationCode"]
            machine["StationName"] = incident["StationName"]
            machine["UnitName"] = incident["UnitName"]
            machine["UnitType"] = incident["UnitType"]
            result.append(machine)
        elif unit_type == "elevators" and incident["UnitType"] == "ELEVATOR":
            machine = {}
            machine["StationCode"] = incident["StationCode"]
            machine["StationName"] = incident["StationName"]
            machine["UnitName"] = incident["UnitName"]
            machine["UnitType"] = incident["UnitType"]
            result.append(machine)

    return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=True)
