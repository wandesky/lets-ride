class User:
    def __init__(self, usename, password, accountID):
        self.username = username
        self.password = password
        self.accountID = accountID
    
    def get_all_rides(self):
        return #all rides info

    def get_specific_ride(self, rideID):
        return #specific ride
        
    def get_all_rides(self):
        return #all rides

    def request_ride(self, rideID):
        
    
class Driver(User):
    def __init__(self, fleetID, nationalID):
        self.fleetID = fleetID
        self.nationalID = nationalID


    def create_ride_offer(self, route, departure_time, arrival_time):
        if condition: #success
            pass #return ride info
        elif condition: #fail
            pass # error message

            

class Passenger(User):
    def request_ride():
        if condition: #success
            pass # return confirmation message
        elif:
            pass #return error message
    

class Ride:
    def __init__(self, rideID, route):
        self.rideID = rideID
        self.route = route