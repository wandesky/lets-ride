from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # # Ensure that flask was set up correctly
    # def test_index(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/login', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)

# Ensure that all rides are displayed
    def test_acess_all_rides(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/rides', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()



###from models import User, Driver, Passenger

# content of test_class.py



######Differentiate between unit and integration tests then come back and write these tests#######
# class TestClass(object):
#     def test_get_all_rides(self):
#         rides_list = User.get_all_rides(self)
#         assert rides_list


#     def test_get_specific_ride(self, rideID):
#         specific_ride = User.get_specific_ride(self)
#         assert specific_ride

#     def test_create_ride_offer(self, route, departure_time, arrival_time):
#         create_ride_response = Driver.create_ride_offer(self, route, departure_time, arrival_time)
#         assert create_ride_response

#      def test_request_ride_offer(self, route, departure_time, arrival_time):
#         ride_request_response = User.request_ride_offer(self, route, departure_time, arrival_time)
#         assert ride_request_response

    



    # def test_two(self):
    #     x = "check"
    #     assert hasattr(x, 'check')

    # content from previously used test_sample.py
    # def func(x):
    #     return x + 1

    # def test_answer():
    #     assert func(3) == 5

