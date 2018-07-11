from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

# Ensure that all rides are displayed
    def test_access_all_rides(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/rides', content_type='html/text')
        self.assertEqual(response.status_code, 200)

# Ensure that a user can access a specific ride
    def test_access_specific_ride(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/rides/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

# Ensure that a driver can post a ride
    def test_post_ride(self):
        tester = app.test_client(self)
        response = tester.post('/api/v1/rides', content_type='html/text')
        self.assertEqual(response.status_code, 200)

# Ensure that a passanger can request a ride
    def test_request_ride(self):
        tester = app.test_client(self)
        response = tester.post('/api/v1/rides/1/requests', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

