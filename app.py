from flask import Flask, jsonify
from flask_restful import Resource, Api
from models import User, Driver, Passenger

app = Flask(__name__)
api = Api(app)

#Dummy objects to use while testing
dummy_driver = Driver('dummy_username', 'dummy_password', 'dummy_accountID', 'dummy_fleetID', 'dummy_nationalID')
dummy_passenger = Passenger


class Ride(Resource):
    def get(self, rideID):
        # return {'ride': name}
        status = User.get_specific_ride(self, rideID)
        return status
    

    def put(self, rideID):
        # return {'ride': name}
        status = dummy_driver.create_ride_offer('dummy_route', 'dummy_origin', 'dummy_destination', rideID, 'dummy_departure_time', 'dummy_arrival_time')
        return status

class AllRides(Resource):
    def get(self):
        all_rides = User.get_all_rides(self)
        return jsonify(all_rides)


api.add_resource(Ride, '/api/v1/rides/<string:rideID>')
api.add_resource(AllRides, '/api/v1/rides')

app.run(debug=True)