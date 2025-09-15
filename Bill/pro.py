
# def load_store_items(filename):
#     store = {}
#     file = open(filename, "r")
#     for line in file:
#         parts = line.strip().split(",")
#         if len(parts) == 3:
#             code, name, price = parts
#             store[code.strip()] = {
#                 "name": name.strip(),
#                 "price": float(price.strip())
#             }
#     file.close()
#     return store

# def get_orders(store):
#     orders = []
#     total = 0.0

#     code = input("Enter Item Code (0 to finish): ").strip()
#     while code != "0":
#         if code in store:
#             quantity = int(input("Enter Quantity: "))
#             item_name = store[code]["name"]
#             item_price = store[code]["price"] * quantity
#             orders.append((item_name, quantity, item_price))
#             total += item_price
#         else:
#             print("Invalid code! Try again.")
#         code = input("Enter Item Code (0 to finish): ").strip()

#     return orders, total

# def save_bill(filename, orders, total):
#     file = open(filename, "a")
#     file.write("         my shop\n")
#     file.write("========== BILL =========\n")
#     file.write("Item       Qty   Price\n")
#     for item, qty, price in orders:
#         file.write(f"{item:<10} {qty:<5} {price:.2f}\n")
#     file.write("=========================\n")
#     file.write(f"Total :          {total:.2f}\n")
#     file.write("=========================\n")
#     file.close()
#     print(f"Bill saved to {filename}")

# def main():
#     store = load_store_items("store.txt")
#     orders, total = get_orders(store)
#     save_bill("bill.txt", orders, total)

# main()



# Simple POS Bill Generator (No main function)

def load_store():
    store = {}
    file = open("store.txt", "r")
    for line in file:
        code, name, price = line.strip().split(",")
        store[code] = [name, float(price)]
    file.close()
    return store

def get_orders(store):
    orders = []
    total = 0.0
    code = input("Enter Item Code (0 to finish): ")
    while code != "0":
        if code in store:
            qty = int(input("Enter Quantity: "))
            price = store[code][1] * qty
            orders.append((store[code][0], qty, price))
            total += price
        else:
            print("Invalid Code!")
        code = input("Enter Item Code (0 to finish): ")
    return orders, total

def save_bill(orders, total):
    file = open("bill.txt", "w")
    file.write("my shop\n")
    file.write("Item       Qty   Price\n")
    for item, qty, price in orders:
        file.write(f"{item:<10} {qty:<5} {price:.2f}\n")
    file.write(f"Total : {total:.2f}\n")
    file.close()

# --- Program Execution (Direct) ---
store = load_store()
orders, total = get_orders(store)
save_bill(orders, total)
print("Bill Generated in bill.txt")
