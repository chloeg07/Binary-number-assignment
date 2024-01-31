menu = "1.Binary numbers to Decimal numbers. \n2.Decimal number to Binary numbers. \n3.Add two Binary numbers"
print(menu)
choice = input("Please choose one of the given options....")
choiceint = int(choice)
print(choiceint)

#Binary to Decimal
if choiceint == 1:
    urnumbinary1 = input("Enter your Binary number: ")
    x = len(urnumbinary1)-1
    total = 0
    for i in urnumbinary1 :
        if i == "1":
            total = total + (2**x)
        else : total = total + 0
        x = x-1
    print("in Binary your Decimal number is...",total)
    
#Decimal number to Binary number
if choiceint == 2:
    decimalnum1 = input("Enter your Decimal number: ")
    y = len(decimalnum1)
    binarylist = []
    decimalnum1int = int(decimalnum1)
    while decimalnum1int != 0:
        decimalnum1left = decimalnum1int % 2
        decimalnum1int = decimalnum1int // 2
        binarylist.append(decimalnum1left)
    binarylist.reverse()
    print("Your Decimal number in Binary is",binarylist) 