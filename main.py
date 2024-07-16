from database import Database
from conta import Conta
def menu():
    print("Bem-vindo ao Banco Central, gostaria de escolher qual opção?\n1 - Acessar conta\n2 - Criar conta\n3 - Verificar existencia de conta\n4 - Deletar conta")

banco = Database()
escolhas = [1, 2, 3, 4, 5]
while True:
    menu()
    option = (int(input()))
    while option in escolhas:
        if option == 1:
            conta = Conta(input("User: "), input("Pass: "))
            conta.verify()
            if conta.switch:
                option = 0
                print("Bem vindo a sua conta, selecione a opção desejada:\n\n1 - Extrato")
                option = int(input())
                if option == 1:
                    conta.extrato()
                    option = 0
        elif option == 2:
            banco.criarConta()
            option = 0
            
        elif option == 3:
            banco.verificarConta()
            option = 0
        elif option == 5:
            banco.mostrarContas()
            option = 0