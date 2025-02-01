class student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
    def get_details(self):
        return(f"student name:{self.name},roll number:{self.roll_number}")
stu = student("Alice","12345")
print(stu.get_details())