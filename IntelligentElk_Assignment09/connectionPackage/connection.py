# Connection.py

import pyodbc

def Connect():
    """
    Connect to the database
    @return Connection Object: The open connection, or None on error
    """
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                              'Database=IS4010;'
                              'uid=IS4010Login;'
                              'pwd=P@ssword2;')
    except:
        conn = None
    
    return conn
