import unittest
import json
import wmata_api


class WMATATest(unittest.TestCase):

    def setUp(self):
        self.app = wmata_api.app.test_client()

    def test_http_success(self):
        response_escalators = self.app.get('/incidents/escalators')
        response_elevators = self.app.get('/incidents/elevators')
        self.assertEqual(response_escalators.status_code, 200)
        self.assertEqual(response_elevators.status_code, 200)

    def test_required_fields(self):
        response = self.app.get('/incidents/escalators')
        data = json.loads(response.data)
        for incident in data:
            self.assertIn("StationCode", incident)
            self.assertIn("StationName", incident)
            self.assertIn("UnitName", incident)
            self.assertIn("UnitType", incident)

    def test_escalators(self):
        response = self.app.get('/incidents/escalators')
        data = json.loads(response.data)
        for incident in data:
            self.assertEqual(incident["UnitType"], "ESCALATOR")

    def test_elevator(self):
        response = self.app.get('/incidents/elevators')
        data = json.loads(response.data)
        for incident in data:
            self.assertEqual(incident["UnitType"], "ELEVATOR")


if __name__ == '__main__':
    unittest.main()
