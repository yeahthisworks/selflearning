import string
#here,  we use string.ascii_letters, string.digits, string.punctuation
import random 
#here, we generate random numbers

length = int(input("Enter desired password length: "))
print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
CharacterList = ""

while(True):
    choice = int(input("Pick a number: "))
    if choice == 1:
        CharacterList += string.digits
    elif choice == 2:
        CharacterList += string.ascii_letters
    elif choice == 3:
        CharacterList += string.punctuation
    elif choice == 4:
        break
    else:
        print("invalid input")

password = []
for i in range(length):
    randomchar = random.choice(CharacterList)
    password.append(randomchar)


print("The random password is " + "".join(password))


