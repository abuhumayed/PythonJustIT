# # name = "Tim"
# # for letter in name:
# #     print(letter)  

# array = (0,1,2,3,4,5)
# for i in array:
#     print(i)

# # for i in range (1,7):
# #     print(i)

# # for countdown in range(10,-1,-1):
# #     print(countdown)

# highscore = [125, 63, 35, 12]

# for i in highscore:
#     print(i)  


# usersList = ["Anna","Paul","Joe","Anne","Pauline","Joan","Janet"]

# for i in usersList:
#     print(i)




# print("Welcome to the table quiz.\n")
# num = int(input("Enter a number: "))






# for i in range(1,6):   
#     answer = int(input(f" What is {i} x {num}? "))
#     print(f"the answer is {answer} ")
#     correct = i * num
#     if answer == correct:
#         print("Correct")
#     else:
#      print(f"No, the answer is  {correct}")

# print("Finished")

import time
import random

name = input("Welcome, What is your Name? ")
timer= int(input(f"Hi {name}, how many Seconds would you like your timer to be for? "))
num1 = int(input("Enter a Number for multiplication: "))
num2 = int(input("Enter a Number for how much you want your multiplication table to go up to: "))

for i in range (1,num2+1):
    answer = i*num1
    print(f"{i} X {num1} =  {answer}\n")

time.sleep(timer)

for t in range (1,6):
  
  randNumber = random.randint(1, num2)
  inputAnswer = int(input(f" What is {num1} x {randNumber}? "))
  correct = randNumber * num1
  if answer == correct:
        print("Correct")
  else:
     print(f"No, the answer is  {correct}")

print("Finished")
 


# for i in range(1,6):   
#     answer = int(input(f" What is {i} x {num}? "))
#     print(f"the answer is {answer} ")
#     correct = i * num
#     if answer == correct:
#         print("Correct")
#     else:
#      print(f"No, the answer is  {correct}")

# print("Finished")
