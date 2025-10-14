grocery_list = []

def add_item():
    item = input("What item do you want to add?: ")
    grocery_list.append(item)
    print(f"{item} has been added to the list.\n")
    
def remove_item():
    item = input("What item do you want to remove?: ")
    grocery_list.remove(item)
    print(f"{item} has been removed from the list.\n")
    
def show_list():
    for num, grocery in enumerate(grocery_list, 1):
        print(f"{num}. {grocery}\n")

while True:
    print("1.Add Item\n2.Remove Item\n3.View List\n4.Exit")
    action = int(input("Choose your option: "))

    if action == 1:
        add_item()
    elif action == 2:
        remove_item()
    elif action == 3:
        show_list()
    elif action == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid Response\n")
    
    





