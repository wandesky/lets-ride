from app import app
import models
import unittest

#dummy data for testing
dummy_test_driver = models.Driver('driver_piet', 'dummy_password', 'dummy_fleetID', 'dummy_nationalID')
dummy_test_ride = models.Ride('route', dummy_test_driver, 'origin', 'destination', 'departure_time', 'arrival_time')
dummy_test_passenger = models.Passenger('passenger_paul', 'dummy_password', 'dummy_nationalID')

class FlaskTestCase(unittest.TestCase):

# Ensure that all rides are displayed
    def test_get_all_rides(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/rides', content_type='html/text')
        self.assertEqual(response.status_code, 200)

# Ensure that a user can access a specific ride
    def test_get_specific_ride(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/rides/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

# Ensure that a driver can post a ride
    # def test_post_ride(self):
    #     tester = app.test_client(self)
    #     response = tester.post('/api/v1/rides', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)

# Ensure that a passanger can request a ride
    def test_request_ride(self):
        tester = app.test_client(self)
        response = tester.post('/api/v1/rides/1/requests', content_type='html/text')
        self.assertEqual(response.status_code, 200)


def test_load_default_page():
    response = models.User.load_default_page()
    assert 'Warning:' in response

def test_add_ride():
    original_list = models.rides_list
    original_list_length = len(original_list)
    dummy_test_driver.create_ride_offer(dummy_test_ride)
    current_list = models.rides_list
    current_list_length = len(current_list)
    assert original_list_length < current_list_length

if __name__ == '__main__':
    unittest.main()

