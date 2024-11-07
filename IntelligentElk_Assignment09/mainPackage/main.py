#*********************************
# Name: Kazuhide Watanabe, Alex Carnes, Alex Patton
# email:  watanake@mail.uc.edu
#         carnesas@mail.uc.edu
#         pattona6@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:  11/07/2024
# Course #/Section: IS 4010/001 
# Semester/Year:   Fall/2024
# Brief Description of the assignment: Group project where we extract data from a Grocery Store Simulator database, and produce a statement about the different attributes of a product.
# Brief Description of what this module does: This module calls the function in order to connect to the database, and selects random attributes of a product and query the database to create a final statement with the attributes listed.
# Citations: In class notes, Bill Nicholson 
# Anything else that's relevant: Everyone had some contribution to this module. 
#**********************************

# main.py

import random
import pyodbc
from connectionPackage.connection import *

if __name__ == "__main__":

    try:
        conn = Connect()
        # Submit a query to the SQL Server instance and store the results in the cursor object 
        cursor = conn.cursor()

    except Exception as e:
        print("Error accessing database")
        print(e)
        exit()

    # Instruction 1
    # Execute the query and fetch all results
    cursor.execute("SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct")
    results = cursor.fetchall()

    # Instruction 2
    # Randomly seleting one row from the data structure in step 1 and storing the attributes into a variable. 
    random_row = random.choice(results)
    product_id = random_row[0]
    description = random_row[2] if random_row[2] else "with no description"
    manufacturer_id = random_row[3]
    brand_id = random_row[4]
    
    # Instruction 3
    # Query using the manufacturer_id variable in step 2 to query for the name of the manufacturer.
    cursor.execute("SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = '" + str(manufacturer_id) + "'")
   
    # Instruction 4
    # Storing the manufacturer name into a variable.
    manufacturerName = cursor.fetchall()
    
    # Instruction 5
    # Repeating steps 3 and 4 but for brand_id and brand name.
    cursor.execute("SELECT Brand FROM tBrand WHERE BrandID = '" + str(brand_id) + "'")
    brandName = cursor.fetchall()

    # Instruction 6
    # Using the product_id variable we created to input into the query below. 
    cursor.execute("SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold FROM dbo.tTransactionDetail INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = '" + str(product_id) + "')")
    numberOfItemsSold = cursor.fetchall()

    # Instruction 7
    # Using the different variables we created to print a sentence with the product attributes into the console. 
    grammaticallyCorrectSentence = f"The product {description}, manufactured by {manufacturerName[0][0]}, and branded as {brandName[0][0]}, has sold a total of {numberOfItemsSold[0][0]} items."
    print(grammaticallyCorrectSentence)