"""This is the main library system functions operator 
this program will hold the menu and main functions."""
from enum import Enum
from create import create_tables
from delete import remove_book, remove_client
from display import display_all_books, display_all_clients, display_all_borrow
from insert import insert_client, insert_books, insert_borrow,find_book_by_name,find_client_by_name
from update import update_client, update_book, update_borrow
from sql_functions import connect

# Define the menu options using an Enum
class Menu(Enum):
    ADD_NEW_CUSTOMER = 1
    ADD_NEW_BOOK = 2
    LOAN_BOOK = 3
    RETURN_A_BOOK = 4
    DISPLAY_ALL_BOOKS = 5
    DISPLAY_ALL_CLIENTS = 6
    DISPLAY_ALL_BORROW = 7
    DISPLAY_LATE_BORROWS = 8
    FIND_BOOK_BY_NAME = 9 
    FIND_CUSTOMER_BY_NAME = 10
    REMOVE_BOOK = 11
    REMOVE_CUSTOMER = 12
    UPDATE_BOOK = 13
    UPDATE_CLIENT = 14
    UPDATE_BORROW = 15
    EXIT = 16

def main():
    # Connect to the database and create tables
    conn, cur = connect()
    create_tables(cur)
    
    while True:
        # Print the menu options
        for m in Menu:
            print(f"{m.value}) {m.name.replace('_', ' ').title()}")
        
        # Prompt the user to choose an option
        option = input("Please pick your action according to your needs.\n")
        if not (option.isnumeric() and 1 <= int(option) <= len(Menu)):
            # Invalid input handling
            print("Invalid option. Please choose a number between 1 and 16.")
            continue
        
        option = int(option)
        
        # Handle the chosen option
        if option == Menu.ADD_NEW_BOOK.value:
            # Add a new book
            insert_books(cur, conn)
        elif option == Menu.ADD_NEW_CUSTOMER.value:
            # Add a new customer
            insert_client(cur, conn)
        elif option == Menu.LOAN_BOOK.value:
            # Loan a book
            insert_borrow(cur, conn)
        elif option == Menu.DISPLAY_ALL_BOOKS.value:
            # Display all books
            books = display_all_books(cur)
            for book in books:
                print(book)
        elif option == Menu.DISPLAY_ALL_CLIENTS.value:
            # Display all clients
            clients = display_all_clients(cur)
            for client in clients:
                print(client)
        elif option == Menu.DISPLAY_ALL_BORROW.value:
            # Display all borrow records
            borrows = display_all_borrow(cur)
            for borrow in borrows:
                print(borrow)
        elif option == Menu.FIND_BOOK_BY_NAME.value:
            # Find a book by its name
            books = find_book_by_name(cur)
            for book in books:
                print(book)
        elif option == Menu.FIND_CUSTOMER_BY_NAME.value:
            # Find a customer by their name
            clients = find_client_by_name(cur)
            for client in clients:
                print(client)
        elif option == Menu.REMOVE_BOOK.value:
            # Remove a book
            book_id = int(input("Enter the ID of the book to remove:\n"))
            remove_book(cur, conn, book_id)
        elif option == Menu.REMOVE_CUSTOMER.value:
            # Remove a customer
            client_id = int(input("Enter the ID of the customer to remove:\n"))
            remove_client(cur, conn, client_id)
        elif option == Menu.UPDATE_BOOK.value:
            # Update a book record
            book_id = int(input("Enter the ID of the book to update:\n"))
            update_book(cur, conn, book_id)
        elif option == Menu.UPDATE_CLIENT.value:
            # Update a client record
            client_id = int(input("Enter the ID of the client to update:\n"))
            update_client(cur, conn, client_id)
        elif option == Menu.UPDATE_BORROW.value:
            # Update a borrow record
            borrow_id = int(input("Enter the ID of the borrow record to update:\n"))
            update_borrow(cur, conn, borrow_id)
        elif option == Menu.EXIT.value:
            # Exit the program
            break
        else:
            # Handle any unexpected case
            print("Invalid option.")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
