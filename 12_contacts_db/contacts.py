import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

def create_table(conn):
	cur.execute('''
		CREATE TABLE IF NOT EXISTS contacts (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT,
			email TEXT,
			phone_number TEXT
			)
		''')
	conn.commit()

def add_contact(conn, name, email, phone_number):
	cur.execute("INSERT INTO contacts(name, email, phone_number) VALUES (?, ?, ?)", (name, email, phone_number))
	conn.commit()

def search_contact(conn, name):
	cur.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
	results = cur.fetchall()
	return results

def delete_contact(conn, name):
	cur.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
	results = cur.fetchall()

	if(len(results)) == 0:
		print("No contact found.")
	
	elif len(results) == 1:
		contact_id = results[0][0]
		cur.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
		print(f"Deleted contact: {results[0][1]}")
	
	else:
		print("Multiple contacts found:")
		for row in results:
			print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}")

		selected_id = input("Enter the ID of the contact to delete: ")
		cur.execute("DELETE FROM contacts WHERE id = ?", (selected_id,))
		print("Contact deleted.")
		
		conn.commit()


def list_contacts(conn):
    cur.execute("SELECT * FROM contacts ORDER BY name")
    for row in cur.fetchall():
        print(row)


conn.close()