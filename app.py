from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
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





class Ride(Resource):
    def post(self):
        #code obtained https://stackoverflow.com/questions/48095713/accepting-multiple-parameters-in-flask-restful-add-resource
        # Define parser and request args
        parser = reqparse.RequestParser()
        parser.add_argument('route', type = str)
        parser.add_argument('origin')
        parser.add_argument('destination')
        parser.add_argument('rideID')
        parser.add_argument('departure')
        parser.add_argument('arrival_time')
        # parser.add_argument('class', type=int)
        # parser.add_argument('analysis', type=bool, default=False, required=False, help='Enable analysis')
        args = parser.parse_args()
        route = args['route']
        origin = args['origin']
        destination = args['destination']
        rideID = args['rideID']
        departure = args['departure']
        arrival_time = args['arrival_time']

        dummy_ride = Ride(route, driver, origin, destination, departure_time, arrival_time)
        dummy_driver.create_ride_offer(dummy_ride)

    #    dummy_driver.create_ride_offer(self, route, origin, destination, rideID, departure, arrival_time)

    #    classes = args['class']  # List ['A', 'B']
    #    analysis = args['analysis'] # Boolean True


# class AddRide(Resource):    
#     def post(self):
#         status = dummy_driver.create_ride_offer()
#         return status


class RequestRide(Resource):
    def post(self, rideID):
        all_rides = dummy_passenger.request_ride(rideID)
        return jsonify(all_rides)

class DefaultErrorPage(Resource):
    def get(self):
        error_message = User.load_default_page()
        return error_message


# a user viewing all available rides
api.add_resource(AllRides, '/api/v1/rides')

# a user viewing a specific ride
api.add_resource(SpecificRide, '/api/v1/rides/<string:rideID>')

# a driver adding a ride
# api.add_resource(AddRide, '/api/v1/rides')

api.add_resource(Ride, '/api/v1/rides')

# a passenger requesting a ride
api.add_resource(RequestRide, '/api/v1/rides/<string:rideID>/requests')

# letting the user know they are using a wrong link
api.add_resource(DefaultErrorPage, '/', '/api', '/api/v1')


if __name__ == '__main__':
    app.run(debug=True)