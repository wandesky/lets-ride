####Driver Info####
##Driver(self,username, password, accountID, fleetID, nationalID)


#####Driver creating a ride########
##Driver(self, route, departure_time, arrival_time)

'''
ride_3 = {
    'status': 'ride created successfully',
    'route': 'routedetails3',
    'rideID': 'XYZABC003',
    'departure': '9.00AM',
    'arrival_time': '10.00AM'
}
'''


from models import User, Driver, User

driver_dummy = Driver('pogba', '123', '001', 'fleet002', '223399')
driver_dummy.create_ride_offer('routedetails3', '10.00AM', '12.00PM')






# driver_dummy.
# driver_dummy.fleetID = '000AQ'
# passanger_dummy = Passenger('David', 'pwd123', 'accountID')

# driver_dummy.create_ride_offer('AAABBBCCC', '11AM', '12PM')
# passanger_dummy.request_ride()