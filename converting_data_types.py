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

