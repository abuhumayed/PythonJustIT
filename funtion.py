def userName4():
    fullName = input("Enter your name: ")
    address = input("Enter your address ")
    interest = input("Any Interests? ")
    return fullName,address,interest


print (userName4())

def inmates(inmate1,inmate2,*args):
    print(*args[2])
    inmates = inmate1, + "" + inmate2  
    return  inmates 

inmates("John","Rachel","Katarina","Kevin","Elizabeth","Fernando","Aicha")
   