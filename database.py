database = {}
class Database:
    def __init__(self):
        pass
        
    def criarConta(self):
        self.user = str(input("User: "))
        self.passwd = str(input("Pass: "))
        self.found = False
        for i in enumerate(database):    
            
            if self.user == list(database.keys())[i[0]]: #Verificador de usuário existente, caso exista alguém com o mesmo nome
                print("Erro: Conta já existente")
                self.found = True
                
        if not self.found: #Se não encontrar o usuário
            database.update({self.user: {self.passwd: 0}})  #Inserir no banco de dados
            print("Conta criada com sucesso")
            


    def verificarConta(self):
        self.acc_found = False
        self.user = str(input("User: "))
        
        for i in enumerate(database):    
            if  self.user == list(database.keys())[i[0]]:
                print ("User exists")
                self.acc_found = True
                
        if not self.acc_found:
            print("User not found")
    
    def fecharConta(self):
        self.user = str(input("User: "))
        #Todas dentro dessa função tem acesso a ela
        self.passwd = str(input("Pass: "))
        #Self só essa função acessa ela declarada com: def NOME_DA_FUNÇÃO(self):
        self.found = False
        
        def promptDelete():
        #Função dentro de função você chama apenas pela função, ex.: promptDelete()
            self.option = (str(input()))       
            if self.option == "s":
                database.pop(self.user)
                print("Usuário apagado com sucesso")
                self.found = True
                return True #Return interrompe a função for pois retornou a função e para o seu funcionamento de busca na variável i
            
        for i in enumerate(database):
            if  self.user == list(database.keys())[i[0]] and self.passwd == list(list(database.values())[i[0]])[0]:
                self.saldo = list(list(database.values())[i[0]].values())[0]
                    
                if list(list(database.values())[i[0]].values())[0] > 0:
                    print("Existe um saldo ativo de R$%.2f nesta conta! Deseja prosseguir com a remoção? (s/n)"% self.saldo)
                    promptDelete()
                else:
                    print("Deseja prosseguir com a remoção? (s/n)")
                    promptDelete()
                return False #Retorna falso caso o usuário digite "n" (sem aspas)
        if self.found == False:
            print("Erro")
        
            
    def mostrarContas(self):
        print(database)
 
    
    
teste = {}
teste.update({'skibidi': 'toilet'})
teste.update({'toilet': 'nis'})