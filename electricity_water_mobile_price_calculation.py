def mobile ():
    print("***Mobiel***\n")
    print("Usage's value\n")
    call = int(input("Call time (min): "))
    internet = int(input("Internet (MB): "))
    sms = int(input("SMS: "))
    print("\n")
    callPrice = 800 * call
    internetPrice = 1000 * internet
    smsPrice = 100 * sms
    total = callPrice + internetPrice + smsPrice
    print("Call: ", call, "min",
    "Internet: ", internet, "MB",
    "Messages: ", sms, "unit", "\n")
    print("Total: ", total, "KIP")

def electricity ():
    print("***Electricity***\n")
    use = int(input("Please type usage's value (KW): "))
    if ((use == 0) & (use < 10)):
        use_0_9 = 5000 * use
        print("0-9 = ", use_0_9, "\n")
        print("Total: ", use_0_9, "KIP")
    elif ((use >= 10) & (use < 50)):
        use_0_9 = 5000 * 9
        use_10_49 = 10000 * (use - 9)
        total = use_0_9 + use_10_49
        print("0-9 = ", use_0_9, "\n")
        print("10-49 = ", use_10_49, "\n")
        print("Total: ", total, "KIP")
    elif (use >= 50):
        use_0_9 = 5000 * 9
        use_10_49 = 10000 * (use - 9)
        use_50_up = 20000 * (use - 49)
        total = use_0_9 + use_10_49 + use_50_up
        print("0-9 = ", use_0_9, "\n")
        print("10-49 = ", use_10_49, "\n")
        print("50 up = ", use_50_up, "\n")
        print("Total: ", total, "KIP")
    else:
        print("Your given number is incorrect")

def water():
    print("***Water***\n")
    use = int(input("Please type usage's value (M square): "))
    if ((use == 0) & (use < 10)):
        use_0_9 = 500 * use
        print("0-9 = ", use_0_9, "\n")
        print("Total: ", use_0_9, "KIP")
    elif ((use >= 10) & (use < 50)):
        use_0_9 = 5000 * 9
        use_10_49 = 1000 * (use - 9)
        total = use_0_9 + use_10_49
        print("0-9 = ", use_0_9, "\n")
        print("10-49 = ", use_10_49, "\n")
        print("Total: ", total, "KIP")
    elif ((use >= 50) & (use < 100)):
        use_0_9 = 500 * 9
        use_10_49 = 1000 * (use - 9)
        use_50_99 = 1500 * (use - 49)
        total = use_0_9 + use_10_49 + use_50_99
        print("0-9 = ", use_0_9, "\n")
        print("10-49 = ", use_10_49, "\n")
        print("50-99 = ", use_50_99, "\n")
        print("Total: ", total, "KIP")
    elif (use >= 100):
        use_0_9 = 500 * 9
        use_10_49 = 1000 * (use - 9)
        use_50_99 = 1500 * (use - 49)
        use_100_up = 2500 * (use - 99)
        total = use_0_9 + use_10_49 + use_50_99 + use_100_up
        print("0-9 = ", use_0_9, "\n")
        print("10-49 = ", use_10_49, "\n")
        print("50-99 = ", use_50_99, "\n")
        print("100 up = ", use_100_up, "\n")
        print("Total: ", total, "KIP")
    else:
        print("Your given number is incorrect")

print("Which service do you want to calculate")
choice = int(input("1 - Mobiel\n2 - Electricity\n3 - Water\n"))
if (choice == 1):
    mobile()
elif (choice == 2):
    electricity()
elif (choice == 3):
    water()
else:
    print("Please provide number in codition")
input("Enter to Exit")
