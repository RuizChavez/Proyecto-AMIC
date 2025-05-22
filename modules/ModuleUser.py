from models.User import User

class ModuleUser:
    
    def Create(self, data): 
        return User(data['name'],data['_id'],data['password'],data['rol'],data['agencia'])