class User:
     def __init__(self, name, age,password):
      self.name = name
      self.age = age
      self.password=password
     def get_user_info(self):
        return  f"{self.name} {self.age} {self.password}"
     def changename(self,name):
        self.name=name


user1=User("Hamza",19,"1234")
print(user1.get_user_info())
user1.changename("ali")
print(user1.get_user_info())

