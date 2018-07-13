


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
    'rideID': '1',
    'departure': '9.00AM',
    'arrival_time': '10.00AM'
}

## a dummy list of all rides
rides_list = [ride_3]

## 
drivers_list = []
passengers_list = []


# rides_list = []

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
        
    def load_default_page():
        return "You should not be here. In order to get things working, try adding /api/v1/rides to the url above"
        
class Driver(User):
    def __init__(self,username, password, fleetID, nationalID):
        self.driverID = 'driver'+str(len(drivers_list)+1)
        self.fleetID = fleetID
        self.nationalID = nationalID

    ###Create a new ride###
    def create_ride_offer(self): #take the ride as an object
        
        #The original_list_length will later be used to check if the length of the list has been increased, in which case it will mean the ride was successfully created
        
        original_list_length = len(rides_list)
        # print(original_list_length)

        ride = Ride('dummy_route', self, 'dummy_origin', 'dummy_destination', 'dummy_departure_time', 'dummy_arrival_time')

        # rides_list.append(ride)
        rides_list.append({
            'route': ride.route,
            'origin': ride.origin,
            'destination': ride.destination,
            'rideID' : ride.rideID,
            'departure': ride.departure_time,
            'arrival_time': ride.arrival_time,
            'driverID': self.driverID,
            'passengerID': ride.passengerID

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
    def __init__(self, username, password, nationalID):
        self.passengerID = 'pass'+str(len(passengers_list)+1)

    def request_ride(self, rideID):
        ride_index = next((index for (index, d) in enumerate(rides_list) if d["rideID"] == str(rideID) ), None)
        print('You are about to request this ride:')
        print(rides_list[ride_index])
        rides_list[ride_index]['passengerID'] = self.passengerID
        return(rides_list[ride_index])
        
    

class Ride:
    def __init__(self, route, driver, origin, destination, departure_time, arrival_time):
        self.rideID = str(len(rides_list)+1)
        self.route = route
        self.driverID = driver.driverID
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.passengerID = 'null'