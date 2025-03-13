# Input: Get the number of customers for each hour
hour1 = int(input("Enter the number of customers from 12:00 - 1:00: "))
hour2 = int(input("Enter the number of customers from 1:00 - 2:00: "))
hour3 = int(input("Enter the number of customers from 2:00 - 3:00: "))
hour4 = int(input("Enter the number of customers from 3:00 - 4:00: "))

# Calculate the total and average number of customers
total_customers = hour1 + hour2 + hour3 + hour4
average_customers = total_customers / 4

# Output: Display the number of customers for each hour
print("\nCustomer count per hour:")
print(f"12:00 - 1:00: {hour1} customers")
print(f"1:00 - 2:00: {hour2} customers")
print(f"2:00 - 3:00: {hour3} customers")
print(f"3:00 - 4:00: {hour4} customers")

# Output: Display the total and average number of customers
print(f"\nTotal customers: {total_customers}")
print(f"Average customers per hour: {average_customers:.2f}")
