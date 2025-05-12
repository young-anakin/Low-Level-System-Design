# # A parking lot has multiple levels
# # This Class contains that level
# # A level has multiple parking_spots
# we can implement parking a vehicle from this class
# we can display availability of the parking spots
# We also need to know which floor our level is in

from parking_spot import parkingSpot
from vehicle import Vehicle
class Level:
    def __init__(self, floor:int, available_spots:int):
        self.floor = floor
        self.parking_spots = [parkingSpot(i) for i in range(available_spots)]
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.is_available() and spot.vehicle_type() == vehicle.getType():
                spot.parkVehicle(vehicle=vehicle)
                return True
        return False
    
    def unPark_vehicle(self, vehicle:Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.is_available() and spot.get_parked_vehicle() == vehicle:
                spot.unParkVehicle()
                return True
            else:
                return False
    
    def availiable_spaces(self) -> None:
        for spot in self.parking_spots:
            if spot.is_available:
                print("f parking lot ", spot.get_spot_number(), "is available")
            else:
                print("not available")
