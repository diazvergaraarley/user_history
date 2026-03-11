#Ejercicios de listas
#1:
    #fruits list:
fruits= ["Banana", "Apple", "Watermelon", "Pineapple", "Strawberry"]
print("fruits")
    #a. add a fruit with append()
fruits.append("Blackberry")
print("a,", fruits)

    #b. insert on position 2    
fruits.insert(2, "Cucumber")
print("b.", fruits)

    #c. remove a fruit
fruits.remove("Pineapple")
print("c.", fruits)

    #d. delete last element with pop()
fruits.pop()
print("d.", fruits)

print("-----------------------")

#2:
    #numbers list
numbers= [4, 2, 7, 2, 9, 1, 2]
print("numbers: ", numbers)
    #a. sort list
sorted_numbers= sorted(numbers)
print("a. Sorted lower to higher: ", sorted_numbers)

    #b. reverse
sorted_numbers.reverse()
print("b. Sorted higher to lower: ", sorted_numbers)

    #c. count
counting= numbers.count(2)
print("c. Counting number '2': ", counting)

    #d. index
positioning= numbers.index(7)
print("d.Position of number '7': ", positioning)

print("-----------------------")

#3:
    #lists a & b
numA= [1, 2, 3]
numB= [4, 5, 6]
print("lists: ", numA, "," , numB)

    #a. copy
numC= numA.copy()
print("a. Copy of list 1:", numC)

    #b. extend 
numC.extend(numB)

    #c. final list
print("c. Extended list: ", numC)

print("-----------------------")

#4:

    #students list
students = ["Ana", "Carlos", "María", "Luis", "Sofía", "Pedro", "Valentina"]

    #a. show list 
print("a. Students list: ", students)

    #b. clear
cleanlist= students.copy()
cleanlist.clear()
print("b. Clear list: ", cleanlist)

    #c. show list again
print("c. Show list again: ", students)
