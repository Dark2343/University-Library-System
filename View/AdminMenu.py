import tkinter as tk

from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Label


class AdminMenu(ttk.Frame):
    def __init__(self, parent, app, controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app

        # Create a grid to place the buttons
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        message = Label(self, text="Hello, Admin! How may I server you ?")
        message.grid(row=0, column=1, padx=10, pady=10)

        # Row 1
        browse_books_button = ttk.Button(self, text="Browse Books", command=lambda: self.app.show_frame("Browse"))
        browse_books_button.grid(row=1, column=0, padx=0, pady=10)

        show_books_button = ttk.Button(self, text="Show Books Based On Criteria",
                                       command=lambda: self.app.show_frame("SearchBook"))
        show_books_button.grid(row=1, column=1, padx=0, pady=10)

        update_user_data_button = ttk.Button(self, text="Update User Data",
                                             command=lambda: self.app.show_frame("UpdateUserDetails"))
        update_user_data_button.grid(row=1, column=2, padx=0, pady=10)

        # Row 2
        add_book_button = ttk.Button(self, text="Add Book", command=lambda: self.app.show_frame("AddBook"))
        add_book_button.grid(row=2, column=0, padx=0, pady=10)

        signup_new_user_button = ttk.Button(self, text="Sign Up New User / Admin",
                                            command=lambda: self.app.show_frame("AddUser"))
        signup_new_user_button.grid(row=2, column=1, padx=0, pady=10)

        update_book_button = ttk.Button(self, text="Update Book Details",
                                        command=lambda: self.app.show_frame("UpdateBookDetails"))
        update_book_button.grid(row=2, column=2, padx=0, pady=10)

        # Row 3
        add_book_button = ttk.Button(self, text="Statistics (Report)", command=lambda: self.app.show_frame("Report"))
        add_book_button.grid(row=3, column=1, padx=0, pady=10)
