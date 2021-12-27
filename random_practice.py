#This is a boolean example
likes_oranges = True
likes_apples = False
# The equals sign is used to assign the variable.
print("This person likes oranges:")
print(likes_oranges)
print("This person likes apples:")
print(likes_apples)

#These are examples of string variables.
favorite_color = 'Purple' # you can use single or double quotes.
print("This is my favorite color:")
print(favorite_color)

#This is an example of an integer variable.
favorite_number = 13
print("This is my favorite number:")
print(favorite_number)

#This is an example of a float variable.
tax_rate = 6.5
print("This is the current tax rate:")
print(tax_rate)


#Multiple Assignment Statements
Kerri_job = 'System Admin' 
#Bob_job = 'System Admin'
#Multiple variables that are assigned to the same value.
Kerri_job = Bob_job = 'System Admin'

print("Kerri's Job: ", Kerri_job)
print("Bob's Job: ", Bob_job)
print()

hair_color, eye_color, shirt_color, age = 'brown', 'green', 'red', 33
#eye_color = 'green'
#shirt_color = 'red'
#age = 33

print("Kerri's Hair Color is:", hair_color)
print("Kerri's Eye Color is:", eye_color)
print("Kerri's Shirt Color is:", shirt_color)
print("Kerri's Age is:", age)
print()

#Converting data types in python.

favorite_number = '10' # string variable.
fav_num_type = type(favorite_number)
print('The type for favorite_number is: ', fav_num_type)

favorite_number_as_number = int(favorite_number) # you can change 'int()'  to float.
print("favorite_number_as_number: ", favorite_number_as_number)
print("The type for favorite_number_as_number is:", type(favorite_number_as_number))

age = 9
print("age: ", age)
print("The type for age is:", type(age))
# if you want the age as a string.
age_str = str(age)
print(age_str)

print("age_str: ", age_str)
print("The type for age_str is ", type(age_str))

#gives integer of a float value.
print(int(3.5635214521)) #does not round but it truncates the decimal off.

#Boolean conversion string to bool
likes_cheese = 'True'
print('as boolean:', bool(likes_cheese))

#BAD THINGS!!!
number = 'print("cheese and stuff")' # execute some arbitrary code
number_as_a_number = eval(number)
print('number_as_a_number :', number_as_a_number)
print('type:', type(number_as_a_number))
print()
print()
#Creating lists:
#the first list created
#An element is a thing inside a list
#indices:     0       1       2        3       4
employees = ['Bob', 'Jess', 'Kerri', 'Sean', 'Zach']

print('Employees: ', employees)
print("The third employee is:", employees[2])

# How do I know how many elements there are in a list?
print("The number of employees is: ", len(employees))
#works with strings
print("Kerri has this many letters: ", len("Kerri"))
# or it can be print("Kerri has this many letters: ", len(employees[2]))

#How do I convert a string (others apply) to a list?
fav_food = 'pizza'
fav_food_char_list = list(fav_food)
print('Favorite Food: ', fav_food)
print('Characters: ', fav_food_char_list)

#Modifying Lists
employees = ['Bob', 'Jess', 'Kerri', 'Sean', 'Zach']
#How to I add an element to the end of a list?
print('Employees: ', employees)
employees.append('Zayne')
print('Employees: ', employees)
#How do I remove an element from the list?
del employees[0]
print('Employees: ', employees)
del employees[2]
print('Employees: ', employees)
#How do I remove an element from the end of a list?
special = employees.pop()
print('Employees: ', employees)
print('Special: ', special)

#How do I change an element in a list?
print('Employees: ', employees)
employees[0] = 'Jessica'
print('Employees: ', employees)
print()
#Sorting and reversing lists:
numbers = [5, 80, 16, 2, 36, 10]
letters = ['b', 'l', 'k', 's', 'a']
employees = ['Brett', 'Alexa', 'Zach', 'Patrick', 'Ellen', 'Kerri', 'Justin']
print('Numbers:', numbers)
print('Letters:', letters)
print('Employees:', employees)
#How do I put a list in "ascending" order?
#sorted_num = numbers.sort() *If you use sort() it replaces list.
sorted_num = sorted(numbers)#if you use sorted function you get a copy of list.
#print('Sorted Numbers: ', numbers)
print('Sorted Numbers: ', sorted_num)
print('Numbers:', numbers)
print()
sorted_employees = sorted(employees)
print("Sorted Employees:", sorted_employees)
print("Employees:", employees)
print()
#How do I put a list in descending order?
sorted_letters = sorted(letters)
desc_letters = sorted(letters, reverse=True)
print('Letters:', letters)
print('Sorted Letters:', sorted_letters)
print('Descending Letters:', desc_letters)







