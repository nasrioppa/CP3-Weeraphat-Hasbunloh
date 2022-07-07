def login() :
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput  == "admin" and passwordInput == "1234":
        return showMenu()
    else :
        print("Please try again !!!")
        return login()
def showMenu() :
    print("-----SAMUEL SHOP-----")
    print("1. Vat calculator")
    print("2. Price calculator")
    return menuSelect()
def menuSelect() :
    userSelected = int(input("menu selected >>"))
    if userSelected == 1 :
        return vatCal()
    elif userSelected == 2 :
        return priceCal()
def vatCal() : #take price_1 + price 2 to totalprice
    price = int(input("Price (THB) :"))
    vat = 7
    result = price + (price * vat / 100)
    return result
def priceCal() :
    price_1 = int(input("First product price :"))
    price_2 = int(input("Second product price :"))
    vat = 7
    priceNoVat = price_1 + price_2
    print("ราคาไม่รวม vat 7% :", priceNoVat, "THB")
    totalPrice = priceNoVat + (priceNoVat * vat/100)
    print("ราคารวม vat 7% :", totalPrice, "THB")
print(login())


#login

#menu
#select menu
#vat cal
#price cal