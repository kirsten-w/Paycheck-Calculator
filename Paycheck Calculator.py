# Get the user's first name.
first_name = input('Enter your first name: ')

# Get the user's last name.
last_name = input('Enter your last name: ')

# Get the user's age.
age = int(input('What is your age? '))

# Print a greeting to the user.
print('Hello', first_name, last_name)


print('''

''')


# string_value = input('How many hours did you work? ')
# hours = int(string_value)

# vs

hours = float(input('How many hours did you work today? '))
total_hours = float(input('How many hours did you work this week? '))
pay_rate = float(input('What is your hourly pay rate? '))


print('''

''')


print('Here is the data you entered:')
print('Name:', first_name, last_name)
print('Age:', age)
print('Hours Worked Today:', hours)
print('Hours Worked This Week:', total_hours)
print('Pay Rate:', pay_rate)
print('''
''')


pay = hours * pay_rate
print('You made this much money today:', pay)
total_pay = total_hours * pay_rate
print('You made this much money this week:', total_pay)
