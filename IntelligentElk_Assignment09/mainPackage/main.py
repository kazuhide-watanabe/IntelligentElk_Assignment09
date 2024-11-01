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

# main.py

import pyodbc
from connectionPackage.Connection import *

try:
    conn = Connect()
    # Submit a query to the SQL Server instance and store the results in the cursor object 
    cursor = conn.cursor()

except Exception as e:
    print("Error accessing database")
    print(e)
    exit()
