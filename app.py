from flask import Flask, jsonify
from flask_restful import Resource, Api
from models import User, Driver, Passenger, Ride

app = Flask(__name__)
api = Api(app)

#Dummy objects to use while testing
dummy_driver = Driver('driver_piet', 'dummy_password', 'dummy_fleetID', 'dummy_nationalID')
dummy_passenger = Passenger('passenger_paul', 'dummy_password', 'dummy_nationalID')




class AllRides(Resource):
    def get(self):
        all_rides = User.get_all_rides(self)
        return jsonify(all_rides)

class SpecificRide(Resource):
    def get(self, rideID):
        # return {'ride': name}
        status = User.get_specific_ride(self, rideID)
        return status


class AddRide(Resource):    
    def post(self):
    
        status = dummy_driver.create_ride_offer()
        return status


class RequestRide(Resource):
    def post(self, rideID):
        all_rides = dummy_passenger.request_ride(rideID)
        return jsonify(all_rides)


# a user viewing all available rides
api.add_resource(AllRides, '/api/v1/rides')

# a user viewing a specific ride
api.add_resource(SpecificRide, '/api/v1/rides/<string:rideID>')

# a driver adding a ride
api.add_resource(AddRide, '/api/v1/rides')

# a passenger requesting a ride
api.add_resource(RequestRide, '/api/v1/rides/<string:rideID>/requests')

if __name__ == '__main__':
    app.run(debug=True)