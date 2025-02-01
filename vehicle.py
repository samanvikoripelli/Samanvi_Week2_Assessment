class vehicle:
    def __init__(self,brand):
        self.brand = brand
    def show_brand(self):
        print(f"brand:{self.brand}")
class car(vehicle):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model = model
    def display_model(self):
        print(f"model:{self.model}")
class bike(vehicle):
    def __init__(self, brand,type):
        super().__init__(brand)
        self.type = type
    def display_type(self):
        print(f"type:{self.type}")
class electriccar(car):
    def __init__(self, brand,model,battery_capacity):
        super().__init__(brand,model)
        self.battery_capacity = battery_capacity
    def display_battery(self):
        print(f"battery_capacity:{self.battery_capacity} kwh")
electric_car = electriccar("tesla","model s",200)
electric_car.show_brand()
electric_car.display_model()
electric_car.display_battery()


