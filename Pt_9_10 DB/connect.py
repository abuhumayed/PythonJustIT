import sqlite3 as sql   #as sql as an alias 

dbCon = sql.connect("/Users/Abu/Documents/GitHub/PythonJustIT/Pt_9_10 DB/GLAW4C19.db")

dbCursor=dbCon.cursor()