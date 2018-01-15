number = int(input("Enter your number: "))
factorial = 1
if (number == 0):
    factorial = 1
elif (number < 0):
    print("can't calculate")
else:
    b = 1
    while (b <= number):
        factorial *= b
        b += 1
print(factorial)
