print("Hello, welcome to the Low and Upper limit!")

lowLimit = int(input("Enter your low limit: "))
UpperLimit = int(input("Enter your upper limit: "))

response = str(input("Would you want to display an even or odd range?, \n ,Enter E/O : "))
if response == 'E':
    print("The even numbers in your range are: ")
    for value in range(lowLimit , UpperLimit):
        if (value%2 == 0):
            print (value)
            

elif response == 'O':
    print("The odd numbers in your range are: ")
    for value in range(lowLimit , UpperLimit):
        if (value%2 == 1):
            print (value)
            

else:
    print('Invalid entry')

print("Thank you for using the ranger!")