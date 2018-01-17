number = 499
numberdivided3 = 0
numberdivided6 = 0
print("Number divided by 3:\n")
while (number < 1000):
    number += 1
    if ((number % 3) == 0):
        numberdivided3 += 1
        print(number, "\n")
number = 499
print("Number divided by 6:\n")
while (number < 1000):
    number += 1
    if ((number % 6) == 0):
        numberdivided6 += 1
        print(number, "\n")
print("Quantity of number divided by 3: ", numberdivided3, "\n")
print("Quanlity of number divided by 4: ", numberdivided6, "\n")
