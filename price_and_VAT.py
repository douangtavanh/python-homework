vat = 0.1
price = int(input("Please type price value: "))

pricePlusVat = price + (price * vat)

if ((price >= 1) & (price <= 1000)):
    discount = price * 0.03
    finalPrice = pricePlusVat - discount
    print("Price before VAT = ", price, "\n")
    print("Price plus VAT = ", pricePlusVat, "\n")
    print("Discount rate 3% = ", discount, "\n")
    print("Final price = ", finalPrice, "\n")
elif ((price >= 1001) & (price <= 2000)):
    discount = price * 0.05
    finalPrice = pricePlusVat - discount
    print("Price before VAT = ", price, "\n")
    print("Price plus VAT = ", pricePlusVat, "\n")
    print("Discount rate 5% = ", discount, "\n")
    print("Final price = ", finalPrice, "\n")
elif ((price >= 2001) & (price <= 5000)):
    discount = price * 0.07
    finalPrice = pricePlusVat - discount
    print("Price before VAT = ", price, "\n")
    print("Price plus VAT = ", pricePlusVat, "\n")
    print("Discount rate 7% = ", discount, "\n")
    print("Final price = ", finalPrice, "\n")
elif ((price >= 5001) & (price <= 10000)):
    discount = price * 0.09
    finalPrice = pricePlusVat - discount
    print("Price before VAT = ", price, "\n")
    print("Price plus VAT = ", pricePlusVat, "\n")
    print("Discount rate 9% = ", discount, "\n")
    print("Final price = ", finalPrice, "\n")
elif (price > 10000):
    discount = price * 0.1
    finalPrice = pricePlusVat - discount
    print("Price before VAT = ", price, "\n")
    print("Price plus VAT = ", pricePlusVat, "\n")
    print("Discount rate 10% = ", discount, "\n")
    print("Final price = ", finalPrice, "\n")
else:
    print("Do not be silly, just type the number in codition range")
