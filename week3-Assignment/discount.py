def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount
        discount = price * (discount_percent / 100)
        # Return price after discount
        return price - discount
    else:
        # Return original price if discount is less than 20%
        return price

# Get input from user
original_price = float(input("Enter the original price: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Display results
if final_price == original_price:
    print(f"No discount applied. Final price: ${final_price:.2f}")
else:
    print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
    print(f"You saved: ${(original_price - final_price):.2f}")