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

# How do I flip a list? (Reversing)

#reversed_employees = reversed(employees) #this will give you an iteration not list.
reversed_employees = list(reversed(employees))
print(employees)
print(reversed_employees)

employees.reverse() #another way to reverse the list
print(employees)
print()
#slicing lists
letters = list('abcdefghijklmnop')
print(letters)
#How do I get letters 'c' through 'f'?
selected = letters[2:6]
print('Selected: ', selected)
#How do I get every other letter/element from the list?
every_other = letters[0:len(letters):2] #start, stop, step /or letters[::2]
print('Every other letter: ', every_other)
print()
#Reversing with slicing
reverse_employees = employees[::-2]
print('Reversed : ', reverse_employees)
print('Employees : ', employees)
print()
