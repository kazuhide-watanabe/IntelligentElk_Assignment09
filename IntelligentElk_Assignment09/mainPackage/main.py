#*********************************
# Name: Kazuhide Watanabe, Alex Carnes, Alex Patton
# email:  watanake@mail.uc.edu
#         carnesas@mail.uc.edu
#         pattona6@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31/2024
# Course #/Section: IS 4010/001 
# Semester/Year:   Fall/2024
# Brief Description of the assignment: Group project where each member creates a class to be called to the main module.
# Brief Description of what this module does: This module imports the Stove and Fridge file. 
# It then creates and instance of the classes, invokes the non-dunder and dunder methods testing normal and exception cases of using the class. 
# Citations: In class notes, Bill Nicholson 
# Anything else that's relevant: This python file was assigned to Kazuhide Watanabe
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
