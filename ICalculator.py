from abc import ABC,abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    @abstractmethod
    def substract(self,a,b):
        pass
    @abstractmethod
    def multiply(self,a,b):
        pass
    @abstractmethod
    def divide(self,a,b):
        pass
class basiccalculator(ICalculator):
    def add(self,a,b):
        return a + b
    def substract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self,a,b):
        if b == 0:
            return "error:cannot divide by zero"
        return a / b
if __name__ == "__main__":
    calc = basiccalculator()
    print("addition:",calc.add(15,5))
    print("substraction:",calc.substract(15,5))
    print("multiplication:",calc.multiply(15,5))
    print("division:",calc.divide(15,5))
    print("division:",calc.divide(15,5))
    print("division by xero:",calc.divide(15,5))
    