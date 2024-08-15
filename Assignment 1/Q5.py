''' Design a Library Management System
Requirements:
Implement classes for Book, Member, Librarian, and Library.
Book should have attributes like title, author, ISBN, and status.
Member should have attributes like name, member_id, and a list of borrowed books.
Librarian should have attributes like name and employee_id.
Library should have a collection of books and methods to add/remove books, register members, lend books, and return books. '''

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = "available"

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self.status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.status == "available":
            self.borrowed_books.append(book)
            book.status = "borrowed"
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.status = "available"
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title} borrowed.")

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"Member: {self.name}, ID: {self.member_id}, Borrowed Books: {borrowed_titles if borrowed_titles else 'None'}"


class Librarian:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def __str__(self):
        return f"Librarian: {self.name}, Employee ID: {self.employee_id}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "available":
                    self.books.remove(book)
                    print(f"Book '{book.title}' removed from the library.")
                else:
                    print(f"Cannot remove '{book.title}' because it is currently borrowed.")
                return
        print(f"No book found with ISBN: {isbn}")

    def register_member(self, name, member_id):
        for member in self.members:
            if member.member_id == member_id:
                print(f"Member with ID {member_id} already exists.")
                return
        new_member = Member(name, member_id)
        self.members.append(new_member)
        print(f"Member '{name}' registered with ID {member_id}.")

    def lend_book(self, member_id, isbn):
        member = self.find_member(member_id)
        if not member:
            print(f"No member found with ID: {member_id}")
            return

        book = self.find_book(isbn)
        if not book:
            print(f"No book found with ISBN: {isbn}")
            return

        member.borrow_book(book)

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        if not member:
            print(f"No member found with ID: {member_id}")
            return

        book = self.find_book(isbn)
        if not book:
            print(f"No book found with ISBN: {isbn}")
            return

        member.return_book(book)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def show_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def show_members(self):
        if not self.members:
            print("No members registered in the library.")
        else:
            print("Library members:")
            for member in self.members:
                print(member)


# Example usage
library = Library()

# Librarian adding books
library.add_book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", "123456789")
library.add_book("Percy Jackson and The Olympians: The Lightning Theif", "Rick Riordan", "987654321")
print()

# Registering members
library.register_member("Christopher Bang", "M001")
library.register_member("Felix Lee", "M002")
print()

# Displaying books and members
library.show_books()
print()
library.show_members()
print()

# Lending and returning books
library.lend_book("M001", "123456789")  # Christopher borrows "The Great Gatsby"
library.lend_book("M002", "123456789")  # Felix tries to borrow "The Great Gatsby", but it's unavailable
library.return_book("M001", "123456789")  # Christopher returns "The Great Gatsby"
library.lend_book("M002", "123456789")  # Felix borrows "The Great Gatsby"
print()

# Display updated book statuses and member details
library.show_books()
print()
library.show_members()