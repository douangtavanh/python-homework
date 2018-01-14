import math

a = float(input("Please enter a value: \n"))
b = float(input("Please enter b value: \n"))
c = float(input("Please enter c value: \n"))

if (a == 0):
    x = -c/b
    print(x, "\n")
else:
    delta = (math.pow(b, 2))-(4*a*c)
    if (delta == 0):
        x = (-b)/(2*a)
        print(x, "\n")
    elif (delta > 0):
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(x1, x2, "\n")
    else:
        print("Incorrect")
