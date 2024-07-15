from database import Database
def menu():
    print("Bem-vindo ao Banco Central, gostaria de escolher qual opção?\n1 - Acessar conta\n2 - Criar conta\n3 - Verificar existencia de conta\n4 - Deletar conta")

while True:
    Banco = Database()
    menu()
    option = (int(input()))
    if option == 1:
        pass
    if option == 2:
        Banco.criarConta()
    if option == 3:
        Banco.verificarConta()
    if option == 5:
        Banco.mostrarContas()