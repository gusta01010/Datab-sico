database = {}
database.update({"Teste": {"123": 0}})
#{"[User]": {"[Password]": [Money value]}"
database.update({"Abc": {"456": 2}})
database.update({"Cachaça": {"69": 3}})
print(list(database.values()))
print(list(list(database.values())[0])[0])
print(list(list(database.values())[[0][0]])[0])

depositar = 5
for i in enumerate(database):    
    if "69" in list(database.values())[i[0]] and "Cachaça" in list(database.keys())[i[0]]:
        print(list(list(database.values())[i[0]].values())[0])
        
        database.update({"Cachaça": {"69": list(list(database.values())[i[0]].values())[0] + depositar}})
        #Atualiza o valor do database do usuario, o valor do saldo dele, + depositar
        
        print(database) 

print (list(list(database.values())[i[0]].values())[0]) #Funciona
#print ((list(database.values())[i[0]].values())[0]) Não funciona

def verify():
    for i in enumerate(database):   
        if "Teste" == list(database.keys())[i[0]]:
            database.pop("Abc")
            return False

verify()
print(database)

#print(list(list(database.values())[0].values())[0])
#for i in enumerate(database):
#    print(i)
