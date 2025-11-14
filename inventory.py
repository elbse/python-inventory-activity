print("====== INVENTORY MENU ======")


item_names = []         
item_prices = {}        

while True:
    print("\nSelect an option:")
    print("[1] Add Item")
    print("[2] Update Price")
    print("[3] Exit")

    choice = input("Enter your choice: ")

   
    try:
        if choice not in ['1', '2', '3']:
            raise ValueError("Invalid menu option.")
    except ValueError as e:
        print(e)
        continue

    
    if choice == '1':
        item_name = input("Enter item name: ").strip()

      
        if item_name in item_names:
            print(f"Error: '{item_name}' already exists in inventory.")
            continue

        
        try:
            item_price = float(input("Enter item price: "))
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue

       
        item_names.append(item_name)
        item_prices[item_name] = item_price

        print(f"Item '{item_name}' added with price {item_price}.")

 
    elif choice == '2':
        item_name = input("Enter item name to update: ").strip()

        if item_name not in item_names:
            print(f"Error: Item '{item_name}' does not exist.")
            continue

        
        try:
            new_price = float(input("Enter new price: "))
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue

        item_prices[item_name] = new_price
        print(f"Price for '{item_name}' updated to {new_price}.")

  
    elif choice == '3':
        print("Exiting Inventory Menu.")
        break
