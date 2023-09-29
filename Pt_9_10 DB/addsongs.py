from connect import * # import the connect.py module 

def insert_data(): 
  songTitle=input("Enter Song Title: ")   
  songArtist=input("Enter Song Artist: ")   
  songGenre=input("Enter Song Genre: ")   


  dbCursor.execute("INSERT INTO songs(Title, Artist, Genre) VALUES(?,?,?)",(songTitle,songArtist,songGenre))
  dbCon.commit()
  print(f"{songArtist} inserted into songs table")


if __name__ == "__main__":
  insert_data()


                 