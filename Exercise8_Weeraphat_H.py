print("Please enter your Username and Password")
usernameInput = input("Username :")
passwordInput = input("password :")
if usernameInput == "nasrioppa" and passwordInput == "58745" :
    print("------Welcome to Nasri Shop------")
    print("...MENU...")
    print("1.Weed")
    print("2.Catnip")
    print("3.Cig")
    print("4.Cream")
    print("5.Beer")
    menuSelected = int(input("menu selected :"))
    if menuSelected == 1 :
        print("How many Weed ?")
        weedInput = int(input(" :"))
        totalPrice = weedInput * 500
        print("Total price is", totalPrice, "THB")
    elif menuSelected == 2 :
        print("How many Catnip ?")
        catnipInput = int(input(" :"))
        totalPrice = catnipInput * 150
        print("Total price is", totalPrice, "THB")
    elif menuSelected == 3 :
        print("How many Cig ?")
        cigInput = int(input(" :"))
        totalPrice = cigInput * 70
        print("Total price is", totalPrice, "THB")
    elif menuSelected == 4 :
        print("How many Cream ?")
        creamInput = int(input(" :"))
        totalPrice = creamInput * 175
        print("Total price is", totalPrice, "THB")
    elif menuSelected == 5 :
        print("How many Beer ?")
        beerInput = int(input(" :"))
        totalPrice = beerInput * 50
        print("Total price is", totalPrice, "THB")
    print("-------THANK YOU <3-------")
else:
    print("WRONG USERNAME OR PASSWORD !!!!")
