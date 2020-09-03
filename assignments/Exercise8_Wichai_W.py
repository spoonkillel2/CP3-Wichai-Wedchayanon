#Product Name
productName = "1. SANTINO | The Ostrish Feather\n2. SANTINO | Praying to The Sky\n3. SANTINO | Bucket Hat"
product1Name = "SANTINO | The Ostrish Feather"
product2Name = "SANTINO | Praying to The Sky"
product3Name = "SANTINO | Bucket Hat"

#Product Size
Xs = "Xs"
S = "S"
M = "M"
L = "L"
XL = "XL"

#Product Price
product1Price = 1890
product2Price = 1890
product3Price = 450

#SIZE
sizeShirt = "Xs | S | M | L | XL |"
sizeHat = "S | M | L"

#User & Pass Function
usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "admin" and passwordInput == "0000":
    print("Done !!")
    #First_Page
    print("____ Santino Bkk ___")
    print("1. Catalog")
    print("2. Calculator")

    userSelected = int(input("โปรดเลือกเมนู : "))
    if userSelected == 1:
        print(productName)
        catalogSelected = int(input("โปรดเลือกสินค้า : "))
        if catalogSelected == 1:
            print(product1Name)
            print("***Avaliable Size***")
            print(sizeShirt)
            sizeSelected = str(input("โปรดระบุไซด์ :"))
            if sizeSelected == Xs or S or M or L or XL:
                print(product1Name,"ราคา :", product2Price,"THB")
                print("Stock Avaliable!")

        elif catalogSelected == 2:
            print(product2Name)
            print("***Avaliable Size***")
            print(sizeShirt)
            sizeSelected = str(input("โปรดระบุไซด์ :"))
            if sizeSelected == Xs or S or M or L or XL:
                print(product2Name,"ราคา :", product2Price,"THB")
                print("Stock Avaliable!")

        elif catalogSelected == 3:
            print(product3Name)
            print("***Avaliable Size***")
            print(sizeHat)
            sizeSelected = str(input("โปรดระบุไซด์ :"))
            if sizeSelected == S or M or L:
                print(product3Name,"ราคา :", product3Price,"THB")
                print("Stock Avaliable!")
        else:
            print("Error!!")

#Calculate Order
    elif userSelected == 2:
        print(productName)
        print("***โปรดเลือกสินค้า***")

        calculatorSelect = int(input("รายการที่ : "))
        if calculatorSelect == 1 :
            print(product1Name)
            print("ราคา:", product1Price,"THB")
            quantity = int(input("โปรดระบุจำนวน : "))
            if True:
                price = product1Price*quantity
                print("รวมทั้งสิ้น :",price, "THB")


        elif calculatorSelect == 2:
            print(product2Name)
            print("ราคา:", product2Price,"THB")
            quantity = int(input("โปรดระบุจำนวน : "))
            if True:
                price = product2Price*quantity
                print("รวมทั้งสิ้น :",price, "THB")

        elif calculatorSelect == 3:
            print(product3Name)
            print("ราคา:", product3Price,"THB")
            quantity = int(input("โปรดระบุจำนวน : "))
            if True:
                price = product3Price*quantity
                print("รวมทั้งสิ้น :",price, "THB")

        else:
            print("Error!!")
else:
    print("Username&Password Incorrect !!")

