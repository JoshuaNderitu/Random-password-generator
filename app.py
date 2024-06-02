import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

def generate_pasword():
    password_length = int(input('How long would you like the passsword to be: '))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = ''.join(password)

    print(password)

option = input('Do you wanrt to generate a password(yes/no): ').lower()

if option == 'yes':
    print('Welcome to random generator Password!')
    print()
    generate_pasword()
elif option == 'no':
    print('Program Terminated. Try again')
    quit()
else:
    print('You chose the wrong option')
    quit()