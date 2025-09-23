inventory = []
MAX_CAPACITY = 100 

def find_product_by_sku(sku):
    for item in inventory:
        if item['sku'] == sku:
            return item
    return None


def find_product_by_name(name):
    results = []
    for item in inventory:
        if name.lower() in item['name'].lower():
            results.append(item)
    return results

def insert_product():
    if MAX_CAPACITY and len(inventory) >= MAX_CAPACITY:
        print(f"Error: Inventory capacity of {MAX_CAPACITY} reached!")
        return

def insert_multiple_products():
    try:
        count = int(input("How many products do you want to add? "))
        if count <= 0:
            print("Error: Enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    for _ in range(count):
        insert_product()   


    sku = input("Enter SKU: ").strip()
    if not sku:
        print("Error: SKU cannot be empty.")
        return

    existing = find_product_by_sku(sku)
    if existing:
        choice = input("Product exists. Update quantity? (y/n): ").strip().lower()
        if choice == 'y':
            try:
                qty = int(input("Enter new quantity to add: "))
                if qty <= 0:
                    print("Error: Quantity must be positive.")
                    return
                existing['quantity'] += qty
                print("Quantity updated successfully.")
            except ValueError:
                print("Invalid input. Quantity must be a number.")
        else:
            print("Duplicate SKU rejected.")
        return

    name = input("Enter Product Name: ").strip()
    if not name:
        print("Error: Product name cannot be empty.")
        return

    try:
        quantity = int(input("Enter Quantity: "))
        if quantity <= 0:
            print("Error: Quantity must be positive.")
            return
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return

    product = {'sku': sku, 'name': name, 'quantity': quantity}
    inventory.append(product)
    print("Product inserted successfully.")

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory:")
    print(f"{'SKU':<10}{'Product Name':<20}{'Quantity':<10}")
    print("-" * 40)
    for item in inventory:
        print(f"{item['sku']:<10}{item['name']:<20}{item['quantity']:<10}")
    print()

def search_by_sku():
    sku = input("Enter SKU to search: ").strip()
    product = find_product_by_sku(sku)
    if product:
        print(f"Found: {product['sku']} - {product['name']} - Qty: {product['quantity']}")
    else:
        print("Product not found.")

def search_by_name():
    name = input("Enter product name to search: ").strip()
    results = find_product_by_name(name)
    if results:
        for p in results:
            print(f"{p['sku']} - {p['name']} - Qty: {p['quantity']}")
    else:
        print("No products found with that name.")

def delete_product():
    sku = input("Enter SKU to delete: ").strip()
    product = find_product_by_sku(sku)
    if product:
        inventory.remove(product)
        print(f"Product {product['name']} removed from inventory.")
    else:
        print("Product not found.")

def main():
    while True:
        print("\nInventory Stock Manager")
        print("1. Insert / Update Product")
        print("2. Display Inventory")
        print("3. Search by SKU")
        print("4. Search by Name")
        print("5. Delete Product")
        print("6. Insert Multiple Products")
        print("7. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            insert_product()
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            search_by_sku()
        elif choice == '4':
            search_by_name()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            insert_multiple_products()
        elif choice == '7':
            print("Exiting Inventory Manager.")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()