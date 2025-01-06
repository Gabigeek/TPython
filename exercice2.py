list1 = ['Bronze','Argent','Or']
list1[1] = 'Platine'

dictionnaire = {"rang": list1}
print(dictionnaire)

dictionnaire = {"rang": list1, "niveau": 30}
dictionnaire["niveau"] = int(dictionnaire["niveau"]/2)
print(dictionnaire)
