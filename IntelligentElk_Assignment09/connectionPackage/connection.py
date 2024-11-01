#*********************************
# Name: Kazuhide Watanabe, Alex Carnes, Alex Patton
# email:  watanake@mail.uc.edu
#         carnesas@mail.uc.edu
#         pattona6@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:  11/07/2024
# Course #/Section: IS 4010/001 
# Semester/Year:   Fall/2024
# Brief Description of the assignment: 
# Brief Description of what this module does:
# Citations: In class notes, Bill Nicholson 
# Anything else that's relevant: 
#**********************************

# Connection.py

import pyodbc

def Connect():
    """
    Coneect to the database
    @return Connection Object: The open connection or none, or error
    """
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                                  'Database=GroceryStoreSimulator;'
                                  'uid=IS4010Login;'
                                  'pwd=P@ssword2;')
    except :
        conn = None

    return conn

