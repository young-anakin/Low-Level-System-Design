from parking_lot import ParkingLot
from level import Level
from vehicle import Vehicle

from car import Car
from truck import Truck
from motorcycle import MotorCycle
class ParkingLotDemo:
    def run():
        lot = ParkingLot.get_instance()

        lot.add_level(Level(1, 100))
        lot.add_level(Level(2, 90))


        car = Car("123")
        motor = MotorCycle("abc")
        truck = Truck("xyz")

        lot.park_vehicle(car)
        lot.park_vehicle(motor)
        lot.park_vehicle(truck)

    

if __name__ == "main":
    ParkingLotDemo.run()




