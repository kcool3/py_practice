# if/else statements:
eaten_brussel_sprouts = True
                
if eaten_brussel_sprouts:
    print('Yayyyy! You get a cookie!')
else:
    print('Sorry, You get nothing!!!')
           
#PySoy can be used as a game engine.
#Game
guess = 7
if guess == 7:
    print('You win!')
elif guess == 8: # elif can be used as an 'or' this.
    print('runner up!')
elif guess == 6:
    print('runner up!')   
else:
    print('uh oh')

#compound conditional expressions: AND/OR
eaten_peas = True
eaten_carrots = False
if eaten_peas and eaten_carrots:
    print('You get ice cream')
else:
    print('Nothing for you!!')
print()
#This is the inclusive OR example.
#eaten_peas = True
#eaten_carrots = False
#if eaten_peas or eaten_carrots:
#    print('You get ice cream')
#else:
#    print('Nothing for you!!')


give_money = True
fuel_up = True

if give_money and fuel_up:#exclusive or
     print('No, that is too generous!')
elif give_money or fuel_up:
     print('Thank you!')
else:
    print('I need your help!')
print()
#For loops:
employees = ['Bob', 'Sue', 'Justin', 'Harry', 'Kerri', 'Jon']
attempts = range(3)
print('Employees: ', employees)
for employee in employees:
    print('Employee: ', employee)
fav_number = 13
for attempt in attempts:
    guess = int(input("What is my favorite number? \n"))
    if guess == fav_number:
       print('YAY, You win!')
       break
    else:
        print('Try again.')
        print()
#print('This is how many attempts it took to guess: ',attempt)    

for index, employee in enumerate(employees):
    print(index, ':', employee)



