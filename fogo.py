database = {}
database.update({"Teste": {"123": 0}})
database.update({"Abc": {"456": 2}})
database.update({"Cachaça": {"69": 3}})
print(list(database.values()))
print(list(database.values())[0])

    
for i in enumerate(database):    
    if "69" in list(database.values())[i[0]] and "Cachaça" in list(database.keys())[i[0]]:
        print(list(list(database.values())[i[0]].values())[0])

#print(list(list(database.values())[0].values())[0])
#for i in enumerate(database):
#    print(i)