# Library Management System

A desktop Library Management application built with Python and Tkinter.

## Overview

This project provides a simple librarian workflow with:

- User registration and login
- Add books to inventory
- Remove books from inventory
- Issue books to the lend list
- View available and issued books in real time

The UI is implemented as a single-window dashboard using Tkinter widgets.

## Project Structure

- `lib_manage.py` - Main application script containing all UI and logic

## Requirements

- Python 3.8 or newer
- Tkinter (usually bundled with standard Python on Windows)

## Run the Application

From the project folder:

```powershell
python lib_manage.py
```

## How to Use

1. Launch the app.
2. Register a librarian account using a username and password.
3. Log in with the same credentials.
4. Use the dashboard actions:
   - Add Book: adds a title to available books
   - Remove Book: removes a title from available books
   - Issue Book: moves a title from available books to issued books
5. Use Refresh Book List to reload displayed book data.

## Current Limitations

- Data is stored only in memory while the app is running.
- No database or file persistence after closing the window.
- Issued books cannot be returned yet.
- Passwords are not encrypted and are only kept in runtime memory.

## Future Improvements

- Save data to JSON or SQLite for persistence
- Add return-book functionality
- Add search and filtering
- Improve user management and password security

## License

This project currently has no license file. Add a `LICENSE` file if you plan to share or open-source it.
