from connect import * # import the connect.py module 

# create function
def read_data():
    # select all records 
    dbCursor.execute("SELECT * FROM songs")
     
    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)


if __name__ == "__main__":
    read_data()