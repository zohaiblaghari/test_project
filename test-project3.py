#get user input
num_people = int(input("Enter the number of people: "))
cost_per_meal = float(input("enter the cost of each meal: Rs"))
sales_tax_percentage = float(input("enter the sales tax percentage: "))
tip_percentage = float(input("enter the tip percentage: "))

#calculate the total cost of food
total_cost_of_food = num_people * cost_per_meal
print(f"\ntotal cost of food: Rs{total_cost_of_food:.2f}")

#calculate total sales tax
total_sales_tax = (sales_tax_percentage / 100)* total_cost_of_food
print(f"totalsales tax: Rs{total_sales_tax:.2f}")

#calculate total tip amount
total_tip_amount = (tip_percentage / 100)* total_cost_of_food
print(f"total tip Amount: Rs{total_tip_amount:.2f}")

#calculate total bill amount per person 
total_bill_per_person = (total_cost_of_food + total_sales_tax + total_tip_amount) / num_people
print(f"Total bill amount per person: Rs{total_bill_per_person:.2f}")