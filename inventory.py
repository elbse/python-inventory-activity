print("====== INVENTORY MENU ======")

# Inventory data structures
item_names = []          # List to store item names
item_prices = {}         # Dictionary: item_name -> price

while True:
    print("\nSelect an option:")
    print("[1] Add Item")
    print("[2] Update Price")
    print("[3] Exit")

    choice = input("Enter your choice: ")

    # Try–except for invalid menu input (not required but good practice)
    try:
        if choice not in ['1', '2', '3']:
            raise ValueError("Invalid menu option.")
    except ValueError as e:
        print(e)
        continue

    # --------------------------
    # OPTION 1: ADD ITEM
    # --------------------------
    if choice == '1':
        item_name = input("Enter item name: ").strip()

        # Prevent duplicate names
        if item_name in item_names:
            print(f"Error: '{item_name}' already exists in inventory.")
            continue

        # Price input with error handling
        try:
            item_price = float(input("Enter item price: "))
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue

        # Add to data structures
        item_names.append(item_name)
        item_prices[item_name] = item_price

        print(f"Item '{item_name}' added with price {item_price}.")

    # --------------------------
    # OPTION 2: UPDATE PRICE
    # --------------------------
    elif choice == '2':
        item_name = input("Enter item name to update: ").strip()

        if item_name not in item_names:
            print(f"Error: Item '{item_name}' does not exist.")
            continue

        # Price update with error handling
        try:
            new_price = float(input("Enter new price: "))
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue

        item_prices[item_name] = new_price
        print(f"Price for '{item_name}' updated to {new_price}.")

    # --------------------------
    # OPTION 3: EXIT
    # --------------------------
    elif choice == '3':
        print("Exiting Inventory Menu.")
        break
