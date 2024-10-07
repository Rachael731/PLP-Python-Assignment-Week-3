# Define the function to calculate the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example input to test the function (since input can't be simulated here)
original_price = 100.0  # Example price
discount_percent = 25.0  # Example discount percentage

# Calculate and display the final price
final_price = calculate_discount(original_price, discount_percent)

final_price  # Returning final price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display the final price
final_price = calculate_discount(original_price, discount_percent)
if discount_percent >= 20:
    print(f"The final price after a {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {final_price}")

