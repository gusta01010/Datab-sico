from database import database
class Conta:
    def __init__(self, name, password):
        self.username = name
        self.password = password
        self.switch = False
        for i in enumerate(database):    
            if self.password in list(database.values())[i[0]] and self.username in list(database.keys())[i[0]]:
                self.saldo = (list(list(database.values())[i[0]].values())[0])
                
                
    def verify(self):
        self.acc_found = False
        for i in enumerate(database):    
            if self.password in list(database.values())[i[0]] and self.username in list(database.keys())[i[0]]:
                print ("User exists")
                self.acc_found = True
                self.switch = True
                
        if not self.acc_found:
            print("Erro, verifique os dados novamente.")
            self.switch = False
    
    def extrato(self):
            print(f"Titular: {self.username} | Saldo: {self.saldo}")