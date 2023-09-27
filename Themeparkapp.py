from datetime import date

adultCost = 25
childCost = 10
seniorCost= 5
parkingPass = False
today = date.today()

print("Welcome to Safari Rides Theme park!\nFind our Entrance Prices below:\nAdult £25.00\nChild(under 16): £10.00\nSenior(65+): £5.00")

adult = int(input("Please Enter the amount of Adult Tickets Required: "))
child = int(input("Please Enter the amount of Child Tickets Required: "))
senior = int(input("Please Enter the amount of Senior Tickets Required: "))

bookingSurname = input("Please Enter Your Surname: ").upper()
ParkingConfirm = input("Please Enter Characters Y/N if you require a parking pass:  ").upper()

if ParkingConfirm == "Y" :
    parkingPass = True
else:
    parkingPass = False    

totalCost = (adultCost*adult)+(childCost*child)+(seniorCost*senior)

def totalCosts():
    print(f"Total Costs: £{totalCost}.00")

totalCosts()

def printTicket():
    print(f"{bookingSurname}\nTickets Purchased: \nAdult: {adult} \nChild: {child} \nSenior: {senior}\nPurchase Date: {today}")

printTicket()

def printParking():
    print(f"Parking Pass\n{today}")

if parkingPass == True:
    printParking()
    
 
print("Thank You for your Purchase, and we hope you enjoy Safari Rides!")
