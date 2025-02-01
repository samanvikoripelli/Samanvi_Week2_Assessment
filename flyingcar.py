class vehicle:
    def move(self):
        print("vehicle is moving")
class car(vehicle):
    def move(self):
        print("car is driving on the road")
class airplane(vehicle):
    def move(self):
        print("airplane is flying")
class flyingcar(car,airplane):
    def move(self):
        print("flying car can do both fly and drive")
        super().move()
flyingcar = flyingcar()
flyingcar.move()