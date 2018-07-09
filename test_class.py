from models import User, Driver, Passenger

# content of test_class.py
class TestClass(object):
    def test_get_all_rides(self):
        rides_list = User.get_all_rides(self)
        assert rides_list


    def test_get_specific_ride(self, rideID):
        specific_ride = User.get_specific_ride(self)
        assert specific_ride

    def test_create_ride_offer(self, route, departure_time, arrival_time):
        create_ride_response = Driver.create_ride_offer(self, route, departure_time, arrival_time)
        assert create_ride_response

     def test_request_ride_offer(self, route, departure_time, arrival_time):
        ride_request_response = User.request_ride_offer(self, route, departure_time, arrival_time)
        assert ride_request_response

    



    # def test_two(self):
    #     x = "check"
    #     assert hasattr(x, 'check')

    # content from previously used test_sample.py
    # def func(x):
    #     return x + 1

    # def test_answer():
    #     assert func(3) == 5

