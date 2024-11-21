# Implement a class called Library that manages a collection of books.
# Each book has a title, author, and available status. The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books= []  

def add_book(self, book):
        self.books.append(book)

def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return book

        print("Book not found.")

def is_available(self, title):
        for book in self.books:
            if book.title == title:
                return book.available
        return False

def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book borrowed successfully.")
                return 
        print("Book not available or not found.")

def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned successfully.")
                return
        print("Book not found.")


#Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Amount must be positive.")
def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient   balance.") 
        else:
            print("Invalid withdrawal amount. Amount must be positive.")
def print_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")
