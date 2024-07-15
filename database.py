database = {}
class Menu:
    def __init__(self):
        self.option = 0
    def menu(self):
        print("Bem-vindo ao Banco Central, gostaria de escolher qual opção?\n1 - Acessar conta\n2 - Criar conta\n3 - Verificar existencia de conta\n4 - Deletar conta")
        
    def criarConta(self):
        database.update({str(input("User: ")): str(input("Pass: "))})  
        
    def verificarConta(self):
        self.acc_found = False
        user = input("User: ")
        passwd = input("Password: ")
        for i in database:
            if i in database and passwd in (database[i]).casefold():
                print ("User exists")
                self.acc_found = True
        if not self.acc_found:
            print("User not found")
    
    def mostrarContas(self):
        print(database)
 

class Conta:
    def __init__(self, name, password):
        self.username = name
        self.password = password

    
    
teste = {}
teste.update({'skibidi': 'toilet'})
teste.update({'toilet': 'nis'})

while True:
    Banco = Menu()
    Banco.menu()
    option = (int(input()))
    if option == 1:
        pass
    if option == 2:
        Banco.criarConta()
    if option == 3:
        Banco.verificarConta()
    if option == 5:
        Banco.mostrarContas()
