class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_spaces = {"big" : big, "medium" : medium, "small" : small}
        self.car_types = {1 : "big", 2 : "medium", 3 : "small"}

    def addCar(self, carType: int) -> bool:
        size_required = self.car_types[carType]
        num_avail = self.parking_spaces[size_required]

        if num_avail == 0:
            return False
        
        self.parking_spaces[size_required] -= 1
        
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)