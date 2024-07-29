from database import database
class Conta:
                
    def __init__(self, name, password):
        self.username = name
        self.password = password
        self.switch = False
        self.saldo = self.Get_Saldo() #tipo float
        
    def Get_Saldo(self):
        for i in enumerate(database):    
            if self.password in list(database.values())[i[0]] and self.username in list(database.keys())[i[0]]:
                return (list(list(database.values())[i[0]].values())[0]) 
                #retorna o valor para o saldo                
   
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
        print(f"Titular: {self.username} | Saldo: %.2f"% self.saldo)
    
    def Set_Saldo(self, n):
            for i in enumerate(database):    
                if self.password in list(database.values())[i[0]] and self.username in list(database.keys())[i[0]]:
                        database.update({self.username: {self.password: list(list(database.values())[i[0]].values())[0] + n}})
                        #atualiza o banco de dados
                        self.saldo = (list(list(database.values())[i[0]].values())[0])
                        #atualiza o saldo visivel
                        #print(database)
                            #Self.username e self.password intactos, altera apenas o valor do saldo do usuário, pegando o valor do saldo dele e somando + self.depositar
    
    def depositar(self):
        self.deposito = float(input("Digite o valor de depósito: "))
        if self.deposito >= 0:
            self.Set_Saldo(self.deposito)
            
    def sacar(self):
        self.saque = float(input("Digite o valor de saque: "))
        if self.saque <= self.saldo and self.saque >= 0:
            self.Set_Saldo(-(self.saque))
        else:
            print("Erro: Saldo insuficiente ou Valor inválido")
                        