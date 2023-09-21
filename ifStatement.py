# num1 = int(input("Enter Num1 : "))
# num2 = int(input("Enter Num2 : "))


# if num1 > num2:
#     print(f"{num2} is the smaller number")
# else:
#     print(f"{num1} is the smaller number")   





burgerMenu = {1:"Chicken Burger",2: "Beef Burger",3: "Lamb Burger", 4:"exit programme" }
burgerChoice = int(input("please select a number from the Menu for your burger choice :\n1. Chicken Burger \n2. Beef Burger \n3. Lamb Burger \n4. Exit \nY  "))


if burgerChoice > 0 and  burgerChoice < 4:
    print(f"Your Choice is: {burgerMenu[burgerChoice]}")
elif  burgerChoice == 4 :
    print("You have exited the programme Goodbye")
else: 
    print("Please Choose a correct Value")
     
 
  

