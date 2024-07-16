database = {}
class Database:
    def __init__(self):
        self.option = 0
        
    def criarConta(self):
        database.update({str(input("User: ")): {str(input("Pass: ")): 0}})  #Inserir no banco de dados
        print("Usuário criado com sucesso") #Criação do usuário

    def verificarConta(self):
        self.acc_found = False
        user = input("User: ")
        for i in enumerate(database):    
            if user in user in list(database.keys())[i[0]]:
                print ("User exists")
                self.acc_found = True
        if not self.acc_found:
            print("User not found")
    
    def mostrarContas(self):
        print(database)
 
    
    
teste = {}
teste.update({'skibidi': 'toilet'})
teste.update({'toilet': 'nis'})