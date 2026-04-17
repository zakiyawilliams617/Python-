import requests
from api import API


class APOD(API):
    APOD_URL = "https://api.nasa.gov/planetary/apod"

    def __init__(self, api_key):

        API.__init__(self, APOD.APOD_URL, api_key)

    def fetch_apod(self, date):

        params = {"api_key": self.api_key, "date": date}
        result = self.get_response(params)
        return result

    def download_image(self, url, filename):
        response = requests.get(url)
        if response.status_code == 200:
            file = open(filename, "wb")
            file.write(response.content)
            file.close()
            print("Image successfully saved as ' " + filename + "'")
        else:
            print("Failed to download iamge. Status code: " +
                  str(response.status_code))
