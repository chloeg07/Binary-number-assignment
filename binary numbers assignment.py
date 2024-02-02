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
#Add two Binary numbers
if choiceint == 3:
    print("You will be asked to enter two Binary numbers that you want to add together")
    binnum1 = input("Enter your first Binary number ....  ")
    binnum2 = input("Enter your second Binary number .... ")
    newnum = []
    R = 0
    carry = 0
    startnum = 0
    startnum2 = 0
    print(binnum1, binnum2)
    lenbinnum1 = len(binnum1)
    lenbinnum2 = len(binnum2)
    for i in range (lenbinnum1) :
        startnum = startnum - 1
        variable1 = binnum1[startnum]
        variable2 = binnum2[startnum]
        newvari = int(variable1) + int(variable2) + carry
        if newvari > 1:
            carry = 1
            if newvari == 2:
                newnum.append(0)
            else: newnum.append(1)
        else:
            carry = 0
            newnum.append(newvari)
            carry = carry - carry
    if carry == 1:
        newnum.append(carry) 
        newnum.reverse()
        print("Final list is", newnum)
            
    

