


##### some dummy data for testing ####
## dictionaries having individual ride details
ride_1 = {
    'route': 'routefromgooglemap', #To be implemented later, use googlemap API or equivalent to get the route
    'origin': 'NBO',
    'destination': 'NKU',
    'rideID': 'XYZABC002', #To be implemented later, find a way to generate unique ride ID's for each ride
    'departure': '8.00AM',
    'arrival_time': '10.00AM'
}

ride_2 = {
    'route': 'routedetails2',
    'origin': 'NBO',
    'destination': 'NKU',
    'rideID': 'XYZABC002',
    'departure': '11.00AM',
    'arrival_time': '12.00AM'
}

ride_3 = {
    'route': 'routedetails3',
    'origin': 'NBO',
    'destination': 'NKU',
    'rideID': '001',
    'departure': '9.00AM',
    'arrival_time': '10.00AM'
}

## a dummy list of all rides
####rides_list = [ride_1, ride_2, ride_3]

rides_list = []

class User:
    def __init__(self, username, password, accountID):
        self.username = username
        self.password = password
        self.accountID = accountID

    def get_all_rides(self):
        return rides_list

    def get_specific_ride(self, rideID):
        ride_index = next((index for (index, d) in enumerate(rides_list) if d["rideID"] == str(rideID) ), None)
        return rides_list[ride_index]
        
    # def get_all_rides(self):
    #     pass #all rides

    def request_ride(self, rideID):
        pass
        
    
class Driver(User):
    def __init__(self,username, password, accountID, fleetID, nationalID):
        self.fleetID = fleetID
        self.nationalID = nationalID

    ###Create a new ride###
    def create_ride_offer(self, route, origin, destination, rideID, departure_time, arrival_time):
        
        #The original_list_length will later be used to check if the length of the list has been increased, in which case it will mean the ride was successfully created
        
        original_list_length = len(rides_list)
        # print(original_list_length)

        rides_list.append({
            'route': 'googlemaplink',
            'origin': origin,
            'destination': destination,
            'rideID' : rideID, #come back and insert function to generate unique rideID for ever new ride
            'departure': departure_time,
            'arrival_time': arrival_time
        })

        #Checking to see if the number of rides in the list has increased        
        current_list_length = len(rides_list)
        #print(current_list_length)


        if current_list_length>original_list_length:
            #print('Success')
            return 'The ride was successfully created'
        else:
            #print('Failed')
            return 'Something went wrong: Your ride was not created'
            

            
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