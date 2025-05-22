class User:
    def __init__(self,username, password, base, rols):
        self.username = username
        self.password = password
        self.base = base
        self.rol = rols
        self.id = 0

    def __repr__(self):
        return f'<name="{self.username}">'
    
    def getValues(self):
        return f"({self.username},{self.password},{self.base},{self.rol})"
    
    def getSet(self):
        return f"username={self.username}, password={self.password}, rols={self.rol}, base={self.base}"