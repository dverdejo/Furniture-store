#Articles
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
lovely_loveseat_price = 254.00

print(lovely_loveseat_description + " $" + str(lovely_loveseat_price))

stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
stylish_settee_price = 180.50

print(stylish_settee_description + " $" + str(stylish_settee_price))

luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
luxurious_lamp_price = 52.15

print(luxurious_lamp_description + " $" + str(luxurious_lamp_price))

#Tax
sales_tax = 0.88

#Our first customer!!
customer_one_total = 0.0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#Adding the tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

#Printing up their receipt
print("Customer one items: " + customer_one_itemization)
print("Customer one total: " + str(customer_one_total))

