#Operators
#Mathematical Operations: +, -, /, *, %, **,//
print('3 + 1 is :',3 + 1)
print('3 - 1 is :',3 - 1)
print('27 / 9 is :',27 / 9)
print('27 // 9 is :',27 // 9)
print('7 % 2 is : ', 7 % 2)
print('7 * 2 is : ', 7 * 2)
print('7 ** 2 is : ', 7 ** 2)
print()
#What about other types? (String)
print('a' + 'b') #concatenation operator
print('Kerri' * 4)
print()
#Comparison Operators: <, <=, >, >=, ==
print( 3 < 4)
print( 3 <= 4)
print( 3 > 4)
print( 3 >= 4)
print( 3 == 4)
print( 10 == 10)

word_one = 'Cheese'
word_two = 'Salami'
print('Is Cheese < Salami? :', word_one < word_two)
word_one = 'Cheese'
word_two = 'Crackers'
print('Is Cheese < Crackers? :', word_one < word_two)
print()
#Determining operator precedence:
# is, not, in
# membership tests
employees = ['Kerri', 'Joe', 'Daniel', 'Kristy', 'Noel']
print('Kerri in Employees: ', 'Kerri' in employees)
print('Justin in Employees: ', 'Justin' in employees)
print('Justin not in Employees: ', 'Justin' not in employees)
print()
# identity tests
fav_food = 'pizza'
lunch_today = 'pizza'
print('Is my favorite food lunch today? ', fav_food is lunch_today)# is (not the same as ==)
other_employees = ['Kerri', 'Joe', 'Daniel', 'Kristy', 'Noel']
print('Are these employees the same? ', employees is other_employees)
#not operator
print(not 1 == 1)
print(1 != 1)
#precedence
print( 4 * 3 + 1 )
print()
