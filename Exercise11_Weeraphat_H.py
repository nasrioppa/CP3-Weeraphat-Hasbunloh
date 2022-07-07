numberInput = int(input("input :"))
for x in range(numberInput) :
    print("*" * ((2*x)+1))

# for hard
number = int(input("input :"))
for i in range(number) :
    text = " "
    for y in range((2*i)+1) :
        text += "*"
    print(text)
