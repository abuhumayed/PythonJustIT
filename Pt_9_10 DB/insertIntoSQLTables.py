from connect import * # import the connect.py module 
dbCursor.execute(""" 

INSERT INTO members (MemberID, Firstname, Lastname, Email)
VALUES (1, "Abu", "Tyson", "abu@hotmail.com");                 
                 

)""")