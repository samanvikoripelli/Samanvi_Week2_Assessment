from abc import ABC,abstractmethod
class IDatabaseoperation(ABC):
    @abstractmethod
    def insert(self,data):
        pass
    @abstractmethod
    def update(self,id,data):
        pass
    @abstractmethod
    def delete(self,id):
        pass
class sqldatabase(IDatabaseoperation):
    def __init__(self,database_name):
        self.database_name = database_name
    def insert(self,data):
        print(f"inserting data into sql database")
    def update(self,id,data):
        print(f"updating data into sql database '{self.database_name}': {data}")
    def delete(self, id):
        print(f"deleting record with id {id} from sql database '{self.database_name}'")
class nosqldatabase(IDatabaseoperation):
    def __init__(self,database_name):
        self.database_name = database_name
    def insert(self,data):
        print(f"inserting data into nosql database '{self.database_name}': {data}")
    def update(self, id, data):
        print(f"updating document with id {id} in nosql database '{self.database_name}: {data}")
    def delete(self,id):
        print(f"deleting document with id {id}from nosql database '{self.database_name}'")
if __name__ == "__main__":
    sql_db = sqldatabase("mysql_server")
    nosql_db = nosqldatabase("mongodb_cluster")
    sql_db.insert({"name":"ram","age":20})
    nosql_db.insert({"name":"alice","age":25})
    sql_db.update(1, {"name":"ram laxman", "age":26})
    nosql_db.update("deoc1234", {"name": "alice bob","age":30})
    sql_db.delete(1)
    nosql_db.delete("doc1234")