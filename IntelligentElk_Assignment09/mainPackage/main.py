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

    # Execute the query and fetch all results
    cursor.execute("SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct")
    results = cursor.fetchall()
    random_row = random.choice(results)

    product_id = random_row[0]
    description = random_row[2]
    manufacturer_id = random_row[3]
    brand_id = random_row[4]
    
    print("ProductID:", product_id)
    print("Description:", str(description))
    print("ManufacturerID:", manufacturer_id)
    print("BrandID:", brand_id)
    

    cursor.execute("SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = '" + str(manufacturer_id) + "'")
    manufacturerName = cursor.fetchall()
    """
    print(manufacturerName)
    """
    
    cursor.execute("SELECT Brand FROM tBrand WHERE BrandID = '" + str(brand_id) + "'")
    brandName = cursor.fetchall()
    print(brandName)

    cursor.execute("SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold FROM dbo.tTransactionDetail INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID =  str(product_id) ")
    
