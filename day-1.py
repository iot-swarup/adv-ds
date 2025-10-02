import array as A

# Global array
arr = A.array('i', [])   # integer array

print(type(arr))

# Function to insert element
def insert_element():
    global arr
    print("\n--- Insert Menu ---")
    print("1. Insert at end")
    print("2. Insert at specific index")
    choice = input("Enter choice (1-2): ")

    if choice == '1':
        val = int(input("Enter element to insert: "))
        arr.append(val)
        print("Element inserted at end. Updated array:", arr.tolist())

    elif choice == '2':
        val = int(input("Enter element to insert: "))
        idx = int(input("Enter index: "))
        if 0 <= idx <= len(arr):
            arr.insert(idx, val)
            print(f"Element inserted at index {idx}. Updated array:", arr.tolist())
        else:
            print("Invalid index.")

    else:
        print("Invalid choice.")

# Function to display array
def display_array():
    global arr
    if len(arr) == 0:
        print("Array is empty.")
    else:
        print("Current Array:", arr.tolist())

# Function to read element by index
def read_element():
    global arr
    if len(arr) == 0:
        print("Array is empty.")
        return
    idx = int(input("Enter index to read: "))
    if 0 <= idx < len(arr):
        print(f"Element at index {idx}:", arr[idx])
    else:
        print("Invalid index.")

# Function to update element
def update_element():
    global arr
    if len(arr) == 0:
        print("Array is empty.")
        return
    idx = int(input("Enter index to update: "))
    if 0 <= idx < len(arr):
        new_val = int(input("Enter new value: "))
        arr[idx] = new_val
        print("Array updated:", arr.tolist())
    else:
        print("Invalid index.")

# Function to delete element
def delete_element():
    global arr
    if len(arr) == 0:
        print("Array is empty.")
        return
    val = int(input("Enter value to delete: "))
    try:
        arr.remove(val)
        print("Value deleted. Updated array:", arr.tolist())
    except ValueError:
        print("Value not found in array.")

# Main Menu
def menu():
    while True:
        print("\n--- Array Operations Menu ---")
        print("1. Insert Element")
        print("2. Display Array")
        print("3. Read Element")
        print("4. Update Element")
        print("5. Delete Element")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            insert_element()
        elif choice == '2':
            display_array()
        elif choice == '3':
            read_element()
        elif choice == '4':
            update_element()
        elif choice == '5':
            delete_element()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the menu
menu()
