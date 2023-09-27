"Read data structures and record for 2 minutes"
"""
Data structures are used to store data in an organised and accessible way. 
A list is a data structure.  Another example of a data structure is a record.  
You might have heard of the word record if you have ever created a database before. 


A record allows you to store a collection of attributes for a single entity.
Data structure: record: An entity can be any object, place, person, or thing. 
Attributes are properties or characteristics of that entity.  
Attributes are sometimes referred to as fields. 

"""


"To Do: Predict, then Run, and then Investigate"
# create a dictionary 
# dict1 = {"key":"value", "key":"value", "key":"value"......}
dict1 = {"fName": "James Smith", "age":23, "interests": "coding", "gamer":True, "fName": "Abdul Malik", 2:"Test"}
print("Start of print")
# print entire dictionary 
print(dict1)

# print specific value(s) from the dictionary 
print(dict1["fName"])  # use  key to print a value
print(dict1["age"]) # use  key to print a value

print("End of print\n")


"Using dictionary methods"
print("\nUsing dictionary methods")
# D.items() -> a set-like object providing a view on D's items
dItems = dict1.items()
print(dItems)
"or"
print(dict1.items())


# D.keys() -> a set-like object providing a view on D's keys
dKeys = dict1.keys()
print(dKeys)

# D.values() -> an object providing a view on D's values
dVals = dict1.values()
print(dVals)

print("\nEnd of  dictionary methods")
"To Do: Task 1: Refer to the example code above to create your own dictionary with key value pairs and explain the differences between the items(), keys() and values() dictionary methods"

print("\nStart of  dictionary loop")
# Loop through the keys ansd/values

print("\nKeys")
for aKey in dKeys:
    print(aKey)
"""
for somekey in dict1.values():
    print(somekey)
"""

print("\nValues")
for aVal in dVals:
    print(aVal)


print("\nKeys and Values")
for aKey, aVal in dItems:
    print(f"Key: {aKey} | Value: {aVal}")

print("\nEnd of dictionary loop")


"To Do: Task 2: Modify"
# Modify: The for loop block above to loop through your own the values 

"To Do: Extension: Can you use the for loop with the items method to loop through the keys and values simultaneously"
# Modify: The for loop block above to loop through the keys and the values and format your output

# create a dictionary 
dict2 = {2:"Python", 3:"HTML", 4:"CSS"}
print(f"Dictionary 2 {dict2}")


# Use of the Update method to merge two dictionaries
dict1.update(dict2)
print(f"Updated dictionary 1\n{dict1}")

"To Do: Task 2: Research: Look up Pop vs popItem explaind comment the code below to explain the difference"


print("Below is pop method")
print(dict2)

# Add comment here to explain the function of th pop() method.
# pop(3) removes the the specified 3rd key and value pair.
dict2.pop(3)  
print(dict2)

print(dict1)
# Add comment here to explain the function of th popItem() method.

# pop item removes the last key value pair in the dictionary records
dict1.popitem()
print(dict1)


"Delete key-value pair from dictionary:"
# We can delete a key-value pair from a dictionary using the del keyword followed
# by the key value to be deleted enclosed in [].

print("this is del function")
print(dict1)

del dict1[2]

print(dict1)

del dict1["interests"]

print(dict1)

# update dictionary value using the key
dict1["fName"] = "Abdul Aziz"

user={"interests" :"coding"}

print(user)
user["interests"] = "Football"

print(dict1)
print(user)