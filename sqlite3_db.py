import sqlite3

#Sqlite3 connection
conn = sqlite3.connect('mydblite.db', uri=True)
cursor = conn.cursor()
# Create table
def creat_table(table_name: str='contact'):
    try:
        cursor.execute('''CREATE TABLE %s
               (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT NOT NULL, lname TEXT NOT NULL, 
               email CHAR(50), number INT, post INT)''' % table_name)
    except(Exception, sqlite3.Error) as creat_table_error:
        return creat_table_error
    finally:
        return 'Table is created'
# Insert a row of data
def insert_row(id, name, lname, email, number, post):
    try:
        insert_query = (id, name, lname, email, number, post)
        cursor.execute("INSERT INTO contact VALUES("
                       "?, ?, ?, ?, ?, ?)", insert_query)
    except(Exception, sqlite3.Error) as insert_row_error:
        print(insert_row_error)
    finally:
        # Save (commit) the changes
        conn.commit()
        return 'Row is added'
# Update row on table
def update_row(id, name, lname, email, number, post):
    try:
        update_query = (name, lname, email, number, post, id)
        cursor.execute("UPDATE contact SET name=?, lname=?,"
                       " email=?, number=?, post=? WHERE id = ?",
                       update_query)
    except(Exception, sqlite3.Error) as update_row_error:
        return update_row_error
    finally:
        # Save (commit) the changes
        conn.commit()
        return 'Row is updated'
# Delete row data on table
def delete_row(id):
    try:
        cursor.execute("DELETE FROM contact WHERE id = %s" % id)
    except() as delete_row_error:
        return delete_row_error
    finally:
        # Save (commit) the changes
        conn.commit()
        return 'Row is deleted'
# Reatrive rews from table
def read_rows():
    try:
        cursor.execute("SELECT id, name, lname, email,"
                       " number, post FROM contact")
    except(Exception, sqlite3.Error) as reatrive_error:
        return reatrive_error
    finally:
        return cursor.fetchall()
        # close the connection
        conn.close()

# Call methouds
# Creat table
'''table = creat_table()
print(table)'''
# Insert row
'''insert = insert_row(3, 'ismail', 'salmi', 'ismail@gmail.com', '069374563', 34000)
print(insert)'''
# Update row
'''update = update_row(1, 'muhammed', 'salmi', 'mossa@gmail.com', '069374563', 35000)
print(update)'''
# Delete row
'''delete = delete_row(1)
print(delete)'''
# Reatrive rows
reatrive = read_rows()
for contact in reatrive:
    print(contact)


