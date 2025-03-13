# Question 1: Cleaning Robot Cost Calculator

# Get user inputs
name = input("Enter the customer's name: ")
num_robots = int(input("Enter the number of robots to order: "))
province = input("Enter the province to ship to: ")

# Set prices and shipping cost
single_robot_price = 75.99
bulk_robot_price = 59.99
shipping_cost = 40
free_shipping_province = "ON"

# Determine price per robot
if num_robots >= 6:
    price_per_robot = bulk_robot_price
else:
    price_per_robot = single_robot_price

# Calculate costs
cost_before_shipping = num_robots * price_per_robot
if province == free_shipping_province:
    shipping = 0
else:
    shipping = shipping_cost
total_cost = cost_before_shipping + shipping

# Display results
print("\nOrder Summary:")
print(f"Customer Name: {name}")
print(f"Province: {province}")
print(f"Number of Robots Ordered: {num_robots}")
print(f"Price per Robot: ${price_per_robot:.2f}")
print(f"Cost Before Shipping: ${cost_before_shipping:.2f}")
print(f"Cost of Shipping: ${shipping:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

# Question 2: Wage Calculator
# Get user inputs
name = input("Enter the employee's name: ")
hours_worked = float(input("Enter the number of hours worked: "))

# Set wage rates
normal_wage = 18.75
overtime_rate = 1.5
regular_hours = 40

# Calculate wages
if hours_worked > regular_hours:
    regular_pay = regular_hours * normal_wage
    overtime_hours = hours_worked - regular_hours
    overtime_pay = overtime_hours * (normal_wage * overtime_rate)
    total_pay = regular_pay + overtime_pay
else:
    total_pay = hours_worked * normal_wage

# Display results
print("\nWage Summary:")
print(f"Employee Name: {name}")
print(f"Total Hours Worked: {hours_worked}")
print(f"Total Earnings: ${total_pay:.2f}")
