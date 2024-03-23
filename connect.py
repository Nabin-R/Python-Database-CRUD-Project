"Objectives"
"" '' # Import sqlite module
import sqlite3 as sql # Imported the sqlite3 module and assigned it an alias 'sql'

"" '' # Understand what is sqlite
"" '' # Create and use a function to create a database file
"" '' # Use try and except to handle error(s)
"" '' # Use the connect function from the sqlite module to create a database file
"" '' # Create a cursor variable from the connect function  

"" '' # Notes:
"" '' #  What is Sqlite
"" '' #  SQLite is a lightweight disk-based database that does not require a separate server process making it easy to integrate into applications
"" '' #  and it uses a variant of the SQL language for database queries to access database. This combination of features makes SQLite a popular 
"" '' #  choice for applications that need a simple and self-contained database solution

# create a function to that creates a database file 
def db_access():
    try: #try and execute the code within the try block
        # use context manager to access and automatically tear down resource(s)
        # invoke/call the sqlite connect function
        # create db file if it does not exist(use db if exist)
        with sql.connect("Python Project/filmflix 3.db") as dbCon:

            # create a variable called dbCursor and initialise with cursor() method from the connect function 
            dbCursor = dbCon.cursor() # cursor() method is used to cal the execute method
            
            return dbCon, dbCursor
    except sql.OperationalError as oe: # raise sql error
        #use the error raise to handle the exception/error
        print(f"Connection failed: {oe}")
#if this is the main file 'connect.py' run the function,
#but if this file is imported in another don't automaticallly run the function
if __name__ == "__main__":
    db_access()



    



