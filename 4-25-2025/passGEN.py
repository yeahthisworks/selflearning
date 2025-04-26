import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

userinput = input("Please enter number of characters password should be: ")

#Check if password is long enough and if input was numbers 
while True:
    try:
        characternum = int(userinput)
        if characternum < 8:
            print("Password length should at least be 8")
            userinput = input("Please enter your number again: ")
        elif characternum > 52:  # The total number of available characters
            print("Password length cannot exceed 52 characters")
            userinput = input("Please enter your number again: ")
        else:
            break
    except:
        print("Please enter numbers only")
        userinput = input("How long do you want your password? ")


random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(characternum * (30/100))
part2 = round(characternum * (20/100))
 
# generation of the password (60% letters and 40% digits & punctuations)
result = []
 
for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])
 
for x in range(part2):
 
    result.append(s3[x])
    result.append(s4[x])
 
 
# shuffle result
random.shuffle(result)
 
 
# join result|
password = "".join(result)
print("Strong Password: ", password)

