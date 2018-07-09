##### some dummy data for testing ####
## dictionaries having individual ride details
ride_1 = {
    'status': 'ride created successfully',
    'route': 'routedetails1',
    'rideID': 'XYZABC002',
    'departure': '8.00AM',
    'arrival_time': '10.00AM'
}

ride_2 = {
    'status': 'ride created successfully',
    'route': 'routedetails2',
    'rideID': 'XYZABC002',
    'departure': '11.00AM',
    'arrival_time': '12.00AM'
}

ride_3 = {
    'status': 'ride created successfully',
    'route': 'routedetails3',
    'rideID': 'XYZABC003',
    'departure': '9.00AM',
    'arrival_time': '10.00AM'
}
## a dummy list of all rides
#rides_list = [ride_1, ride_2, ride_3]

rides_list = []
rrides_list = []
class User:
    def __init__(self, username, password, accountID):
        self.username = username
        self.password = password
        self.accountID = accountID

    def get_all_rides(self):
        return rides_list

    def get_specific_ride(self, rideID):
        return ride_3
        
    # def get_all_rides(self):
    #     pass #all rides

    def request_ride(self, rideID):
        pass
        
    
class Driver(User):
    def __init__(self,username, password, accountID, fleetID, nationalID):
        self.fleetID = fleetID
        self.nationalID = nationalID

    def create_ride_offer(self, route, departure_time, arrival_time):
        
        #Will be later used to check if the length of the list has been increased, in which case it will mean the ride was successfully created
        
        original_list_length = len(rides_list)
        # print(original_list_length)

        rrides_list.append({
            'route': 'routedetails3',
            #come back and insert function to generate unique rideID for ever new ride
            'departure': '9.00AM',
            'arrival_time': '10.00AM'
        })

        #Checking to see if the number of rides in the list have increased
        
        current_list_length = len(rides_list)
        #print(current_list_length)


        if current_list_length>original_list_length:
            print('Success')
            return True
        else:
            print('Failed')
            return False
            

            
class Passenger(User):
    def request_ride():
        # if condition: #success
        #     pass # return confirmation message
        # else condition:
        #     pass #return error message
        pass
    

class Ride:
    def __init__(self, rideID, route):
        self.rideID = rideID
        self.route = route