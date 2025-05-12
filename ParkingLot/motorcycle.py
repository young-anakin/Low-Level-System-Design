
# This is an extension of Vehicle Class
from vehicle import Vehicle
from vehicle_type import vehicleType
class MotorCycle(Vehicle):
    def __init__(self, license_plate:str):
        super().__init__(license_plate=license_plate, vehicle_type=MotorCycle)