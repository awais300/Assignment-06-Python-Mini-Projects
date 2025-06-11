# Smart Grocery Store Assistant

product_catalog = {
    "apple": [100, 10],
    "banana": [60, 20],
    "milk": [120, 8],
}

def display_products():
    print("\nAvailable Products:")
    for product, (price, stock) in product_catalog.items():
        print(f"{product.capitalize()} - Rs.{price}, In stock: {stock}")
        if stock < 5:
            print(f"Low Stock Alert: {product.capitalize()} (Only {stock} left)")

def add_update_product():
    name = input("Enter product name: ").lower()
    price = int(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    product_catalog[name] = [price, stock]
    print(f"{name.capitalize()} updated/added successfully!")

def purchase_item():
    bill = {}
    while True:
        item = input("Enter item to purchase (or type 'done'): ").lower()
        if item == 'done':
            break
        if item in product_catalog:
            qty = int(input(f"Enter quantity for {item}: "))
            if qty <= product_catalog[item][1]:
                product_catalog[item][1] -= qty
                bill[item] = (product_catalog[item][0], qty)
            else:
                print("Not enough stock.")
        else:
            print("Item not found.")
    
    total = 0
    print("\n🧾 Purchase Receipt")
    for item, (price, qty) in bill.items():
        subtotal = price * qty
        print(f"{item.capitalize()}: {qty} x Rs.{price} = Rs.{subtotal}")
        total += subtotal
    print(f"Total Bill: Rs.{total}")

# Main Loop
while True:
    print("\nWelcome to the Smart Grocery Store Assistant")
    print("1. View Products\n2. Add/Update Product\n3. Purchase Items\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        display_products()
    elif choice == '2':
        add_update_product()
    elif choice == '3':
        purchase_item()
    elif choice == '4':
        print("Thank you for using the assistant. Goodbye!")
        break
    else:
        print("Invalid option.")
