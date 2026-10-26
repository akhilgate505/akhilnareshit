# Program 4: Food order bill
# All order data and calculations are inside this file.

orders = [
    {"item": "Masala Dosa", "quantity": 2, "price": 60},
    {"item": "Veg Biryani", "quantity": 1, "price": 150},
    {"item": "Cold Coffee", "quantity": 2, "price": 50},
]

subtotal = 0

print("FOOD ORDER BILL")
print("-" * 40)

for order in orders:
    item_total = order["quantity"] * order["price"]
    subtotal += item_total
    print(
        f'{order["item"]}: {order["quantity"]} x '
        f'Rs.{order["price"]} = Rs.{item_total}'
    )

delivery_fee = 0 if subtotal >= 300 else 30
final_total = subtotal + delivery_fee

print("-" * 40)
print("Subtotal: Rs.", subtotal)
print("Delivery fee: Rs.", delivery_fee)
print("Final total: Rs.", final_total)
