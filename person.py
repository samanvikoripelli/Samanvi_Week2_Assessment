class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def disp_inforamation(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
class employee(person):
    def __init__(self, name, age,id):
        super().__init__(name, age)
        self.id = id
    def disp_emloyee_information(self):
        print(f"id:{self.id}")
class manager(employee):
    def __init__(self, name, age, id,department):
        super().__init__(name, age, id)
        self.department = department
    def approve_leave(self):
        print(f"leave approved by {self.name} from {self.department} department")
manager = manager("ram",21,"m123","HR")
manager.disp_inforamation()
manager.disp_emloyee_information()
manager.approve_leave()