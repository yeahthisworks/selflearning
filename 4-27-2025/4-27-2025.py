from mpmath import mp

userinput = input("Please enter how many slices of pi you want: " )

while(True):
    try:
        length = int(userinput)
        if length <= 0:
            print("Please enter a positive number: ")
            userinput = input("Please enter again: " )
        else:
            break
    except:
        print("Please enter numbers only: ")
        userinput = input("Please enter again: " )

mp.dps = length + 1
print(str(mp.pi))