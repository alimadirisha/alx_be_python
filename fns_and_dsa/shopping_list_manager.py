# shopping_list_manager.py

def display_menu():
    
    #Display the menu options to the user.
    
    print("Shopping List Manager")
    print("********************")
    print("1. Add item")
    print("2. Remove item")
    print("3. View List")
    print("4. Exit")
    
#Add an item to the shopping list.
def add_item(shopping_list):
    
    item = input("Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f'"{item}" has been added to your shopping list.')
    
#Remove an item from the shopping list.

def remove_item(shopping_list):
    
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'"{item}" has been removed from your shopping list.')
    else:
        print(f'"{item}" was not found in your shopping list.')

# Display of items in the shopping list.
def view_list(shopping_list):
    
    if not shopping_list:
        print("Your shopping list is currently empty.")
    else:
        print("\nCurrent Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

# Main function to manage the shopping list.
def shopping_list_manager():
    
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")


# Run the shopping list manager
if __name__ == "__main__":
    shopping_list_manager()
