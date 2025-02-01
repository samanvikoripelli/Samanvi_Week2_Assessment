class product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    def check_availability(self,quantity):
        if quantity <= self.stock:
            return(f"{quantity} units of {self.name} are available")
        else:
            return(f"only{self.stock} units of {self.name} are available")
product = product("Mobile",1500,10)
print(product.check_availability(5))
print(product.check_availability(15))