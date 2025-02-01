class animal:
    def speak(self):
        print("animal will speak")
class dog(animal):
    def speak(self):
        print("dog barks")
class cat(animal):
    def speak(self):
        print("cat say meow")
dog = dog()
cat = cat()
dog.speak()
cat.speak()