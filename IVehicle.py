from abc import ABC, abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class car(IVehicle):
    def start_engine(self):
        print("car:engine started")
    def stop_engine(self):
        print("car:engine stopped")
class bike(IVehicle):
    def start_engine(self):
        print("bike:engine started")
    def stop_engine(self):
        print("bike:engine stopped")
class truck(IVehicle):
    def start_engine(self):
        print("truck:engine started")
    def stop_engine(self):
        print("truck:engine stopped")
if __name__ == "__main__":
    car = car()
    bike = bike()
    truck = truck()
    car.start_engine()
    car.stop_engine()
    bike.start_engine()
    bike.stop_engine()
    truck.start_engine()
    truck.stop_engine()
    