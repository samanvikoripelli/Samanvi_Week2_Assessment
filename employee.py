class employee:
    def __init__(self,name,id,department):
        self.name = name
        self.id = id
        self.department = department
name = input("enter the employee name:")
id = input("enter the employee id:")
department = input("enter the department:")
employee = employee(name,id,department)
print("employee details:")
print(f"name:{employee.name}")
print(f"id:{employee.id}")
print(f"department:{employee.department}")