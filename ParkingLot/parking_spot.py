# This is a parking spot class that has a parking spot in a specific level in the parking lot
# we need to initialize this place, 
# check wether it is available or not, 
# assign it to a car if it is available
# unassign it if a car is leaving
# it must have a type to park a specific type of vehicle
# I want to return the license plate of the vehicle
from vehicle import Vehicle
from vehicle_type import vehicleType
class parkingSpot:
    # a parking spot has availability, type of vehicle it can support, 
    def __init__(self, spotNumber: int):
        self.vehicle = None
        self.vehicle_type = vehicleType.CAR
        self.spot_number = spotNumber
    def is_available(self):
        return self.vehicle is None
    
    def parkVehicle(self, vehicle:Vehicle):
        if vehicle.getType() == self.vehicle_type and self.vehicle is None:
            self.vehicle = vehicle
        else:
            raise ValueError("This spot is either not compatible or is already taken!")
    def unParkVehicle(self):
        self.vehicle = None
    
    def get_vehicle_type(self):
        return self.vehicle_type
    
    def get_parked_vehicle(self):
        return self.vehicle

    def get_spot_number(self):
        return self.spot_number
