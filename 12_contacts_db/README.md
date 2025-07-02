
# Simple Contact Book (SQLite + Python)

This is a beginner-level Python script that lets you manage a contact book using an SQLite database.  
You can add, list, search, and delete contacts, all from the command line.

## Features

- Add new contacts with name, email, and phone number
- Search contacts by (partial) name
- Delete a contact (with ID confirmation if multiple results)
- List all contacts sorted by name

## Technologies

- Python 3
- `sqlite3` (built-in Python module)

## Project Structure

```
contact_book/
├── contact_book.py         # main script with all functions
├── database.db             # SQLite database (created automatically)
└── README.md               # this file
```

## How to Run

1. Clone or download the repository.
2. Run the script with Python:

```bash
python contact_book.py
```

> Note: At the moment, the script only runs the `create_table()` function automatically.  
To add or view contacts, you can call the functions directly in the code, or build a simple menu (coming soon).

## Example Usage

Inside `contact_book.py`, after the function definitions, you can add test calls like:

```python
add_contact(conn, 'Alice', 'alice@example.com', '123456789')
list_contacts(conn)
```

Then re-run the script.

## To Do / Ideas

- [ ] Add a main menu with user input
- [ ] Input validation (e.g. check email format)
- [ ] Export contacts to CSV
- [ ] Search by phone number or email
- [ ] GUI version (Tkinter)

## Author

Made as a beginner project to practice working with:
- Databases in Python
- CRUD operations
- Clean and readable code

Feel free to suggest improvements or fork the repo!