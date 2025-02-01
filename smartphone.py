class electronics:
    def __init__(self,model):
        self.model = model
    def diplay_model(self):
        print(f"model:{self.model}")
class mobiledevice(electronics):
    def __init__(self,model,screen_size):
        super().__init__(model)
        self.screen_size = screen_size
    def diplay_screen_size(self):
        print(f"screen_size:{self.screen_size}")
class smartphone(mobiledevice):
    def __init__(self,model,screen_size,version):
        super().__init__(model,screen_size)
        self.version = version
    def display_version(self):
        print(f"version:{self.version}")
    def display_model(self):
        print(f"smartphone model:{self.model}")
smartphone = smartphone("samsung",6.2,"android")
smartphone.diplay_model()
smartphone.diplay_screen_size()
smartphone.display_version()