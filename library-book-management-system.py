# Library Book Management System

books = {
    "1984": {"author": "Orwell", "available": True},
    "Dracula": {"author": "Stoker", "available": True},
    "Python 101": {"author": "John Doe", "available": True}
}

borrowed_books = []

def view_books():
    print("\nAvailable Books:")
    for title, info in books.items():
        status = "Available" if info["available"] else "Borrowed"
        print(f"{title} by {info['author']} - {status}")

def borrow_book():
    title = input("Enter book name: ").title()
    if title in books and books[title]["available"]:
        books[title]["available"] = False
        borrowed_books.append(title)
        print(f'You have borrowed "{title}".')
    else:
        print("Book not available or does not exist.")

def return_book():
    title = input("Enter book name to return: ").title()
    if title in borrowed_books:
        books[title]["available"] = True
        borrowed_books.remove(title)
        print(f'You have returned "{title}".')
    else:
        print("You didn’t borrow this book.")

def add_book():
    title = input("Enter new book title: ").title()
    author = input("Enter author name: ")
    books[title] = {"author": author, "available": True}
    print(f'Book "{title}" added.')

# Main Loop
while True:
    print("\nWelcome to the Library System")
    print("1. View Books\n2. Borrow Book\n3. Return Book\n4. Add Book\n5. View Borrowed Books\n6. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        view_books()
    elif choice == '2':
        borrow_book()
    elif choice == '3':
        return_book()
    elif choice == '4':
        add_book()
    elif choice == '5':
        print("Borrowed Books:", borrowed_books)
    elif choice == '6':
        print("Thank you for using the library system!")
        break
    else:
        print("Invalid option.")
