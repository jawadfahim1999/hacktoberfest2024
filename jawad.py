library_books = [
    {"ID": "001", "Title": "Brave New World", "Authors": "Aldous Huxley", "Year": 1932},
    {"ID": "001", "Title": "The mountain is you", "Authors": "Brianna Wiest", "Year": 2020},
    {"ID": "002", "Title": "Atomic Habits", "Authors": "James Clear", "Year": 2018},
    {"ID": "003", "Title": "Surrounded by idiots", "Authors": "thomas erikson", "Year": 2014},
    {"ID": "004", "Title": "The laws of human nature", "Authors": "robert greene", "Year": 2018},
    {"ID": "005", "Title": "games people play", "Authors": "Eric Berne", "Year": 1994},
    {"ID": "006", "Title": "How to talk anyone", "Authors": "Leil Lowndes", "Year": 1999},
    {"ID": "007", "Title": "The 48 Laws Of Power", "Authors": "Robert Greene", "Year": 1998},
    {"ID": "008", "Title": "Ikigai", "Authors": "Hector Garcia and Frances Miralles", "Year": 2016},
    {"ID": "009", "Title": "Wonder", "Authors": "R J.Palacio", "Year": 2012},
    {"ID": "010", "Title": "The Alchemist", "Authors": "Paulo Coelho", "Year": 1988 }
]

borrowed_books = []
requested_books = []

def display_books(books):
      for book in books:
        print("*************************")
        print(f"ID: {book['ID']}")
        print(f"Title: {book['Title']}")
        print(f"Authors: {book['Authors']}")
        print(f"Year: {book['Year']}")
        print("*************************")

def borrow_book(book_id):
    for book in library_books:
        if book['ID'] == book_id:
            library_books.remove(book)
            borrowed_books.append(book)
            print(f"The book with the ID {book_id} is successfully loaned to you now.")
            return
    for book in borrowed_books:
        if book['ID'] == book_id:
            requested_books.append(book)
            print(f"The book with the ID {book_id} is not available right now. However, we have requested it for you.")
            return
    print(f"The book with the ID {book_id} is unfortunately not available in the system. Please re-check the ID.")

def return_book(book_id):
    for book in borrowed_books:
        if book['ID'] == book_id:
            borrowed_books.remove(book)
            library_books.append(book)
            if book in requested_books:
                requested_books.remove(book)
            print(f"The book with the ID {book_id} is successfully returned.")
            return
    print(f"The book with the ID {book_id} cannot be returned. Please re-check the ID.")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Display Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_books(library_books)
        elif choice == "2":
            book_id = input("Enter the ID of the book you want to borrow: ")
            borrow_book(book_id)
        elif choice == "3":
            book_id = input("Enter the ID of the book you want to return: ")
            return_book(book_id)
        elif choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
