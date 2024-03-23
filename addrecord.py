"Objectives"
"" '' # Import connect module
from connect import *

"" '' # Create a function to add record(s) to a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

# ceate a function to insert ecord in the songs table
def insert_record():
    try:
        dbCon, dbCursor = db_access()
        # fields/columns = SongID, Title, Artist, Genre
        # SongID field is auto increment, no data required

        # create variables to store the input for the respective fields
        
        film_title  = input("Enter film title: ")
        film_release = input("Enter film year release: ")
        film_rating  = input("Enter film rating: ")
        film_duration  = input("Enter film duration: ")
        film_genre  = input("Enter film genre: ")

        
        # Create a sql insert statement to inset data from the rspective variables above
        dbCursor.execute("INSERT INTO tblFilms (Title,YearReleased,Rating,Duration,Genre) VALUES(?,?,?,?,?)", (film_title, film_release, film_rating, film_duration, film_genre ))
        # Call/invoke the commit method to save the changes(record) permanently in the db table
        dbCon.commit()

        print(f"{film_title}  inserted in the tblFilm table")
    except sql.OperationalError as oe:
        print(f"Failed because {oe}")
if __name__ == "__main__":
    insert_record()
