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

print("-----------------------")

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

print("-----------------------")

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

print("-----------------------")

#8: 
#Merge and update

    #Dictionaries:
d1 = {"a": 1, "b": 2}
d2 = {"b": 5, "c": 3}

    #a. update
d1.update(d2)
    #b. print
print(d1)
    #c. results
d1 = {"a": 1, "b": 2}
d2 = {"b": 5, "c": 3}
d2.update(d1)
print(d2)

print("-----------------------")

#9:
#Delete
    #Dictionary
    #a. dict
fruit1= {
    "Fruit": "Apple",
    "Color": "Red",
    "Quantity": 10,
    "Country": "Colombia"
}
print("Fruit Description: ", fruit1)

    #b. popitem
last_item= fruit1.popitem()
print("Item removed: ", last_item)

    #c. remaining list
print("Remaining List: ", fruit1)


print("-----------------------")

#10
#Mix lists and dictionaries
    #students list of dictionaries
students= [
    {"name": "Luis", "note": 4.5},
    {"name": "Marta", "note": 3.8},
    {"name": "Carlos", "note": 4.2}
]
    #a. print students name
print("Students Names: ")
for student in students:
    print(student["name"])

    #b.note average
total= 0
for student in students:
    total += student["note"]
average = total / len(students)
print("Students average:", average)

    #c. students over 4
print("Passing Students")
for student in students:
    if student ["note"]>=4:
        print(student)
