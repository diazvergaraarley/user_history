#Ejercicios de diccionarios

#5:

    #person: 
personA= {
    "Name": "Ana",
    "Age" : 27,
    "City": "Barranquilla"
}
    #a. print name:
print(personA["Name"])

    #b. print age:
print("Age: ", personA.get("Age"))

    #c. print phone:
print("Phone: ", personA.get("phone", "Doesn't exist"))

print("-")

#6: 

    #a. Add:
personA["Profession"] = "Egineer"

    #b. Change age:
personA["Age"]= 28
print("Updated Age: ", personA.get("Age"))

    #c. delete:
print("Removed value: ", personA.pop("City"))

    #d. final list: 
print("Final list: ", personA)

print("-")

#7: 
#products dictionary:

products= {
    "Bread": 1500,
    "Milk": 3200,
    "Eggs": 9000
} 

    #a. keys:
for key in products.keys():
    print("Products names: ", key)

    #b. values:
for value in products.values():
    print("Products price: ",value)

    #. products: 
for key, value in products.items():
    print("Product:", key, "- Price:", value)