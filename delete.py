# Import necessary libraries
import sqlite3

# Functions to delete records
def remove_book(cur, conn, book_id):
    cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()

def remove_client(cur, conn, client_id):
    cur.execute("DELETE FROM client WHERE id = ?", (client_id,))
    conn.commit()
