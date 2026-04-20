import tkinter as tk
from tkinter import messagebox

# library main class 
class LibraryManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("820x560")
        self.master.minsize(760, 520)
        self.master.config(bg="#0f172a")

        self.books = []
        self.lend_list = []
        self.username = ""
        self.password = ""
        self.librarians = []

        self.palette = {
            "bg": "#0f172a",
            "panel": "#111827",
            "panel_alt": "#1f2937",
            "text": "#e5e7eb",
            "muted": "#94a3b8",
            "accent": "#14b8a6",
            "accent_hover": "#0d9488",
            "danger": "#ef4444",
            "danger_hover": "#dc2626",
            "entry_bg": "#0b1220",
        }

        self.title_font = ("Segoe UI Semibold", 22)
        self.heading_font = ("Segoe UI Semibold", 13)
        self.body_font = ("Segoe UI", 11)
        self.button_font = ("Segoe UI Semibold", 11)

        self.main_container = tk.Frame(self.master, bg=self.palette["bg"])
        self.main_container.pack(fill="both", expand=True, padx=24, pady=24)

        self.login_screen()

    def clear_container(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def make_button(self, parent, text, command, bg_color=None, hover_color=None):
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=self.button_font,
            bg=bg_color or self.palette["accent"],
            fg="white",
            activebackground=hover_color or self.palette["accent_hover"],
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=12,
            pady=10,
            cursor="hand2",
        )
        btn.bind("<Enter>", lambda e: btn.configure(bg=hover_color or self.palette["accent_hover"]))
        btn.bind("<Leave>", lambda e: btn.configure(bg=bg_color or self.palette["accent"]))
        return btn

    def make_entry(self, parent, show=None):
        return tk.Entry(
            parent,
            font=self.body_font,
            bg=self.palette["entry_bg"],
            fg=self.palette["text"],
            insertbackground=self.palette["text"],
            relief="flat",
            bd=6,
            highlightthickness=1,
            highlightbackground="#334155",
            highlightcolor=self.palette["accent"],
            show=show,
        )

    def login_screen(self):
        self.clear_container()

        hero = tk.Frame(self.main_container, bg=self.palette["bg"])
        hero.pack(fill="x", pady=(0, 18))

        tk.Label(
            hero,
            text="Library Management System",
            font=self.title_font,
            bg=self.palette["bg"],
            fg=self.palette["text"],
        ).pack(anchor="w")
        tk.Label(
            hero,
            text="Manage books and lending with a clean workflow",
            font=self.body_font,
            bg=self.palette["bg"],
            fg=self.palette["muted"],
        ).pack(anchor="w", pady=(4, 0))

        panel = tk.Frame(self.main_container, bg=self.palette["panel"], padx=26, pady=24)
        panel.pack(fill="x")

        tk.Label(panel, text="Username", font=self.heading_font, bg=self.palette["panel"], fg=self.palette["text"]).pack(anchor="w")
        self.username_entry = self.make_entry(panel)
        self.username_entry.pack(fill="x", pady=(6, 14))

        tk.Label(panel, text="Password", font=self.heading_font, bg=self.palette["panel"], fg=self.palette["text"]).pack(anchor="w")
        self.password_entry = self.make_entry(panel, show="*")
        self.password_entry.pack(fill="x", pady=(6, 18))

        actions = tk.Frame(panel, bg=self.palette["panel"])
        actions.pack(fill="x")

        self.make_button(actions, "Login", self.login).pack(side="left", fill="x", expand=True)
        self.make_button(actions, "Register", self.register, bg_color=self.palette["panel_alt"], hover_color="#334155").pack(
            side="left", fill="x", expand=True, padx=(10, 0)
        )

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        if not self.username or not self.password:
            messagebox.showerror("Error", "Please enter username and password")
            return

        for librarian in self.librarians:
            if self.username == librarian[0] and self.password == librarian[1]:
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.library_management_screen()
                return
        messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        if not self.username or not self.password:
            messagebox.showerror("Error", "Username and password cannot be empty")
            return

        for librarian in self.librarians:
            if self.username == librarian[0]:
                messagebox.showerror("Error", "Username already registered")
                return

        self.librarians.append([self.username, self.password])
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Registration successful")

    def library_management_screen(self):
        self.clear_container()

        header = tk.Frame(self.main_container, bg=self.palette["bg"])
        header.pack(fill="x", pady=(0, 14))

        tk.Label(
            header,
            text="Library Dashboard",
            font=self.title_font,
            bg=self.palette["bg"],
            fg=self.palette["text"],
        ).pack(anchor="w")
        tk.Label(
            header,
            text=f"Signed in as {self.username}",
            font=self.body_font,
            bg=self.palette["bg"],
            fg=self.palette["muted"],
        ).pack(anchor="w", pady=(4, 0))

        content = tk.Frame(self.main_container, bg=self.palette["bg"])
        content.pack(fill="both", expand=True)

        left = tk.Frame(content, bg=self.palette["panel"], padx=16, pady=16)
        left.pack(side="left", fill="both", expand=True)

        right = tk.Frame(content, bg=self.palette["panel_alt"], padx=16, pady=16)
        right.pack(side="left", fill="both", expand=True, padx=(12, 0))

        tk.Label(left, text="Book Actions", font=("Segoe UI Semibold", 14), bg=self.palette["panel"], fg=self.palette["text"]).pack(anchor="w", pady=(0, 10))

        tk.Label(left, text="Add Book", font=self.heading_font, bg=self.palette["panel"], fg=self.palette["text"]).pack(anchor="w")
        self.add_book_entry = self.make_entry(left)
        self.add_book_entry.pack(fill="x", pady=(6, 8))
        self.make_button(left, "Add", self.add_book).pack(fill="x", pady=(0, 14))

        tk.Label(left, text="Remove Book", font=self.heading_font, bg=self.palette["panel"], fg=self.palette["text"]).pack(anchor="w")
        self.remove_book_entry = self.make_entry(left)
        self.remove_book_entry.pack(fill="x", pady=(6, 8))
        self.make_button(left, "Remove", self.remove_book, bg_color=self.palette["danger"], hover_color=self.palette["danger_hover"]).pack(
            fill="x", pady=(0, 14)
        )

        tk.Label(left, text="Issue Book", font=self.heading_font, bg=self.palette["panel"], fg=self.palette["text"]).pack(anchor="w")
        self.issue_book_entry = self.make_entry(left)
        self.issue_book_entry.pack(fill="x", pady=(6, 8))
        self.make_button(left, "Issue", self.issue_book, bg_color="#2563eb", hover_color="#1d4ed8").pack(fill="x")

        tk.Label(right, text="Available Books", font=("Segoe UI Semibold", 14), bg=self.palette["panel_alt"], fg=self.palette["text"]).pack(anchor="w")
        self.books_listbox = tk.Listbox(
            right,
            font=self.body_font,
            bg="#0b1220",
            fg=self.palette["text"],
            selectbackground="#0f766e",
            relief="flat",
            bd=0,
            height=10,
        )
        self.books_listbox.pack(fill="both", expand=True, pady=(8, 12))

        self.make_button(right, "Refresh Book List", self.view_books, bg_color="#334155", hover_color="#475569").pack(fill="x")

        tk.Label(right, text="Issued Books", font=("Segoe UI Semibold", 14), bg=self.palette["panel_alt"], fg=self.palette["text"]).pack(
            anchor="w", pady=(14, 0)
        )
        self.issued_listbox = tk.Listbox(
            right,
            font=self.body_font,
            bg="#0b1220",
            fg=self.palette["text"],
            relief="flat",
            bd=0,
            height=5,
        )
        self.issued_listbox.pack(fill="x", pady=(8, 0))

        self.view_books()

    def add_book(self):
        book = self.add_book_entry.get().strip()
        if not book:
            messagebox.showerror("Error", "Book name cannot be empty")
            return

        self.books.append(book)
        messagebox.showinfo("Success", "Book added successfully")
        self.add_book_entry.delete(0, tk.END)
        self.view_books()

    def remove_book(self):
        book = self.remove_book_entry.get().strip()
        if not book:
            messagebox.showerror("Error", "Enter a book to remove")
            return

        if book in self.books:
            self.books.remove(book)
            messagebox.showinfo("Success", "Book removed successfully")
        else:
            messagebox.showerror("Error", "Book not found")
        self.remove_book_entry.delete(0, tk.END)
        self.view_books()

    def issue_book(self):
        book = self.issue_book_entry.get().strip()
        if not book:
            messagebox.showerror("Error", "Enter a book to issue")
            return

        if book in self.books:
            self.lend_list.append(book)
            self.books.remove(book)
            messagebox.showinfo("Success", "Book issued successfully")
        else:
            messagebox.showerror("Error", "Book not found")
        self.issue_book_entry.delete(0, tk.END)
        self.view_books()

    def view_books(self):
        if hasattr(self, "books_listbox"):
            self.books_listbox.delete(0, tk.END)
            if self.books:
                for book in self.books:
                    self.books_listbox.insert(tk.END, book)
            else:
                self.books_listbox.insert(tk.END, "No books available")

        if hasattr(self, "issued_listbox"):
            self.issued_listbox.delete(0, tk.END)
            if self.lend_list:
                for book in self.lend_list:
                    self.issued_listbox.insert(tk.END, book)
            else:
                self.issued_listbox.insert(tk.END, "No books issued")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagement(root)
    root.mainloop()