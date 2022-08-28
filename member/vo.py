class Member:
    def __init__(self, id: str = 0, pwd: str = None, name: str = None, email: str = None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def __str__(self): #toString()
        return 'id:'+self.id + ' / pwd :'+self.pwd+' / '+'name : '+self.name+' / '+'email :'+self.email