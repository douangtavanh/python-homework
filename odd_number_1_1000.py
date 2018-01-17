print("Odd number from 1 - 1000: \n")
number = 1
sumodd = 0
quantityodd = 0
quantityodd3 = 0
quantityodd4 = 0
while (number < 1000):
    number += 1
    if ((number % 2) != 0):
        sumodd += number
        quantityodd +=1
        print(number, "\n")
print("Odd number which divided by 3: \n")
number = 0
while (number < 1000):
    number += 1
    if ((number % 2) != 0):
        if ((number % 3) == 0):
            quantityodd3 += 1
            print(number, "\n")
print("Odd number which divided by 4: \n")
number = 0
while (number < 1000):
    number += 1
    if ((number % 2) != 0):
        if ((number % 4) == 0):
            quantityodd3 += 1
            print(number, "\n")
print("Sum all odd number: ", sumodd, "\n")
print("All odd's quantity: ", quantityodd, "\n")
print("Average of all odd number", sumodd/quantityodd, "\n")
print("Quantity of odd number which divided by 3: ", quantityodd3, "\n")
print("Quantity of odd number which divided by 4: ", quantityodd4, "\n")
