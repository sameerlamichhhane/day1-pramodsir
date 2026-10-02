# Shopping Discount Calculator
# Create a shopping program that asks for:
# Customer name
# Product price
# Quantity
# Membership status (yes/no)
# Calculate:
# Subtotal = price × quantity
# Apply discounts:
# Subtotal ≥ Rs. 10,000 → 15%
# Subtotal ≥ Rs. 5,000 → 10%
# Subtotal ≥ Rs. 2,000 → 5%
# Otherwise → No discount
# If the customer is a member and subtotal is at least Rs. 5,000, give an additional 5% discount.
# Display:
# Customer name
# Subtotal
# Discount
# Final amount
# Use f-strings.


cn = input("Enter customer name: ")
pp = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
ms = input("Are you a member? (yes/no): ")

subtotal = pp * quantity

if subtotal >= 10000:
    discount = 0.15
elif subtotal >= 5000:
    discount = 0.10
elif subtotal >= 2000:
    discount = 0.05
else:
    discount = 0

final_discount = discount

if ms == "yes" and subtotal >= 5000:
    final_discount += 0.05

final_amount = subtotal - (subtotal * final_discount)

print(f"Customer Name: {cn}")
print(f"Subtotal: Rs. {subtotal}")
print(f"Discount: {final_discount * 100}%")
print(f"Final Amount: Rs. {final_amount}")