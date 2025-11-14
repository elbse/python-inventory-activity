print("======INVENTORY MENU======")

while True:
    print("\nSelect an option:")
    print("[1] Add Item")
    print("[2] Update Price")
    print("[3] Exit" )

    choice = input("Enter your choice:")

    if choice == '1':
        item_name = input("Enter item name: ")
        item_price = input("Enter item price: ")
        with open("inventory.txt", "a") as file:
            file.write(f"{item_name},{item_price}\n")
        print(f"Item '{item_name}' added with price {item_price}.")

    elif choice == '2':
        item_name = input("Enter item name to update: ")
        new_price = input("Enter new price: ")
        updated = False

        with open("inventory.txt", "r") as file:
            lines = file.readlines()

        with open("inventory.txt", "w") as file:
            for line in lines:
                name, price = line.strip().split(',')
                if name == item_name:
                    file.write(f"{name},{new_price}\n")
                    updated = True
                    print(f"Price for '{item_name}' updated to {new_price}.")
                else:
                    file.write(line)

        if not updated:
            print(f"Item '{item_name}' not found in inventory.")

    elif choice == '3':
        print("Exiting Inventory Menu.")
        break
    
