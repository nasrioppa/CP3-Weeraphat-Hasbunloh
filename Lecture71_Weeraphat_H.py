menuList = [] #เก็บข้อมูลที่ผู้ใช้พิมพ์ไว้ใน List
priceList = []

def showBill () :
    print("My Food".center(21,"-"))
    #print(menuList[0],priceList[0])
    for number in range(len(menuList)) :
        totalPrice = 0
        print(menuList[number], priceList[number])
        totalPrice = totalPrice + int(priceList[number])
    print("Total Price :", totalPrice, "THB")

while True :
    menuName = input("Pls Enter Menu :")
    if menuName.lower() == "exit" :
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
        
showBill()
