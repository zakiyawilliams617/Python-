import json
import requests

from geojson import Point
from urllib.parse import urlencode, quote

# API endpoint URL's and access keys
# https://developer.wmata.com/demokey
WMATA_API_KEY = "cde46e9f5c8147618ab1ebfa14bb189c"
MAPBOX_API_KEY = "pk.eyJ1IjoiemFraXlhd2lsbGlhbXM2MTciLCJhIjoiY21taTlibTVtMTJ0ajJvb2ZldzM0OWYzNiJ9.z99mdvtkD_8yzEYquEewxg"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
STATION_URL = "https://api.wmata.com/Rail.svc/json/jStationInfo"
MAPBOX_URL = "https://api.mapbox.com/styles/v1/mapbox/streets-v12/static"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

# MapBox URL parameters
CENTER_POINT = "-77.054,38.942"
ZOOM_LEVEL = "9"
DIMENSIONS = "500x500"
MAPBOX_URL_PARAMS = f"{CENTER_POINT},{ZOOM_LEVEL}/{DIMENSIONS}"

################################################################################

# query the WMATA 'ElevatorIncidents' API to get a list of outages


def get_station_incidents():
    # use 'requests' to retrieve escalator/elevator incident information
    # docs: https://developer.wmata.com/api-details#api=54763641281d83086473f232&operation=54763641281d830c946a3d75
    response = requests.get(INCIDENTS_URL, headers=headers)
    data = response.json()
    print(data)

    # parse the JSON response of all incidents and create a set containing the station codes
    station_codes = set()
    for incident in data['ElevatorIncidents']:
        station_codes.add(incident['StationCode'])

    # return the set
    return station_codes

################################################################################

# query the WMATA 'Stations' API to get location coordinates (lat/lon)


def get_station_info(station_code: str):
    # use 'requests' to retrive station information by station code
    # docs: https://developer.wmata.com/api-details#api=5476364f031f590f38092507&operation=5476364f031f5909e4fe330c
    response = requests.get(STATION_URL, headers=headers, params={
                            'StationCode': station_code})

    # return the response as JSON
    return response.json()

################################################################################

# # convert list lat/lon pairs (tuples) to URL-encoded GeoJSON object


def encode_geojson(incident_locations):
    feature_collection = {"type": "FeatureCollection", "features": []}

    # build out FeatureCollection to contain a list of "features"
    # each "feature" contains a GeoJSON object that will be plotted as a map marker
    for location in incident_locations:
        feature = {"type": "Feature", "properties":
                   {"marker-color": "#462eff", "marker-size": "small",
                       "marker-symbol": "caution"},
                   "geometry": Point(location)}
        feature_collection["features"].append(feature)

    # return URL-encoded (quoted) GeoJSON object
    return quote(json.dumps(feature_collection))

################################################################################

# retrieve static map image with GeoJSON multiple marker overlay


def get_static_map(encoded_geo_json):
    # MapBox static map URL for 500x500 image centered at (-77.054,38.942) lon/lat
    static_map_url = f"{MAPBOX_URL}/geojson({encoded_geo_json})/{MAPBOX_URL_PARAMS}?access_token={MAPBOX_API_KEY}"

    # use 'requests' and the static_map_url to retrieve the map image
    response = requests.get(static_map_url)

    # if the status code is 200, write the raw bytes (binary data) in the response to a new file called map.png
    if response.status_code == 200:
        map_file = open('map.png', 'wb')
        map_file.write(response.content)
        map_file.close()

    # else print "Error returned from MapBox API"
    else:
        print('Error returned from MapBox API')

################################################################################


def main():
    # get a set of unique station codes experiencing outages
    station_codes = get_station_incidents()

    # print the total number of stations with outages
    # format: X stations are currently experiencing accessibility outages.
    print(str(len(station_codes)) +
          ' stations are currently experiencing accessibility outages.')

    # build a list of lon/lat pairs (tuples) of the location of the first 20 stations with an outage
    # format: [(lon1, lat1), (lon2, lat2), ..., ()]
    incident_locations = []
    for code in station_codes:
       # print the name of each station with an outage
        station_info = get_station_info(code)
        print(station_info['Name'])

        # only collect up to 20 locations (MapBox API Limits)
        if len(incident_locations) < 20:
            lon = station_info['Lon']
            lat = station_info['Lat']
            incident_locations.append((lon, lat))

    # convert the list of lon/lat pairs to a URL-encoded GeoJSON blob using the provided 'encode_geojson' function
    # hint: just pass the result of the previous step (the list of lon/lat tuples) to the 'encode_geojson' function
    encoded_geojson = encode_geojson(incident_locations)

    # use the provided 'get_static_map' function  to retrieve and download the static map image
    # hint: pass the return value from the previous step to the 'get_static_map' function
    get_static_map(encoded_geojson)
################################################################################


if __name__ == "__main__":
    main()
