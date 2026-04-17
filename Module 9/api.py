import requests


class API:
    # base API class for making GET requests

    def __init__(self, base_url, api_key=None):
        # constructor, stores base URL and API key
        self.base_url = base_url
        self.api_key = api_key

    def get_response(self, params):
        # sends GET request to API and returns JSON response
        response = requests.get(self.base_url, params=params)
        return response.json()
