groceries = []

while True:
    action = input("What would you like to do? (add/remove/view/exit): ").lower()

    if action == "add":
        item = input("What item do you want to add?: ")
        groceries.append(item)
        print(f"{item} has been added to your list.")

    elif action == "remove":
        item = input("What item do you want to remove?: ")
        groceries.remove(item)
        print(f"{item} has been removed.")

    elif action == "view":
        for num, grocery in enumerate(groceries, 1):
            print(f"{num}. {grocery}")
    
    elif action == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid action, please try again.")
