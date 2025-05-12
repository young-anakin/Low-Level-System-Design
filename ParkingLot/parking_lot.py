

# we should instantiate a singleton in this class

from level import Level
from vehicle import Vehicle
class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingLot._instance = self
            self.levels: list[Level] = []

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance

    def add_level(self, level : Level) -> None:
        self.levels.append(level)
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    def unPark_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.unPark_vehicle(vehicle):
                return True
        return False
    
    def displayAvailability(self) -> None:
        for level in self.levels:
            level.availiable_spaces()

