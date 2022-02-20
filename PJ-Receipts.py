#We’re going to build a system to help speed up the process of creating receipts for your customers.
#In this project, we will be storing the names and prices of a furniture store’s catalog in variables. 
#You will then process the total price and item list of customers, printing them to the output terminal.

#Defining the products and prices
lovely_loveseat_description = """
Lovely Loveseat. 
Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. 
Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. 
Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

#defining a sales tax
sales_tax = 0.088
#creating a new variable to store the customers total in
customer_one_total = 0
#creating a string to store the item descriptions in the receipt
customer_one_itemization = ""

#adding the total prices and descriptions to the sales receipt
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#calculating the total price based on items selected above
customer_one_tax = customer_one_total * sales_tax
customer_one_total + customer_one_tax

#printing both item descriptions and total price
print("Customer One Items:", customer_one_itemization)
print("Customer One Total:", customer_one_total)