from base64 import main

import psycopg2
class Postgre:
    try:
        con = psycopg2.connect(
        user = "postgres",
        password = "1991",
        host = "127.0.0.1",
        port = "5432",
        database = "users")
        cursor = con.cursor()
    except Exception as connection_error:
        print(connection_error)
    print('Connected')
    # creat table on database
    def creatTable(self):
        try:
            self.cursor.execute(
                '''CREATE TABLE students (id serial PRIMARY KEY,
                 name varchar NOT NULL, lname varchar
                  NOT NULL, age integer NOT NULL)''')
        except Exception as creat_table_error:
            return creat_table_error
        self.con.commit()
        return 'Table is created'
    # insert record
    def insert(self, id, name, lname, age):
        try:
            self.cursor.execute('''
            INSERT INTO students VALUES(
            %s, %s, %s, %s)''', (id, name, lname, age))
        except Exception as insert_error:
            return insert_error
        self.con.commit()
        return 'Data is inserted'
    # read records
    def read(self):
        try:
            self.cursor.execute("SELECT id, name, lname, age FROM students")
        except Exception as select_error:
            return select_error
        print(self.cursor.rowcount ,'rows in your DB')
        return self.cursor.fetchall()

    #update record
    def update(self, age, id):
        try:
            self.cursor.execute("UPDATE students SET age = %s WHERE id= %s", (age, id))
        except Exception as update_error:
            return update_error
        self.con.commit()
        return 'Record is updated'
    #delete record
    def delete(self, id):
        try:
            self.cursor.execute("DELETE FROM students WHERE id = %s", (id,))
        except Exception as delete_error:
            return delete_error
        self.con.commit()
        return 'Record is deleted'

if __name__ == "__main__":
    postgresql = Postgre()
    # creat table
    # table = postgresql.creatTable()
    # print(table)
    # insert
    # insert = postgresql.insert(1, 'yassin', 'salmi', 2020-2007)
    # print(insert)
    # read
    read = postgresql.read()
    print(sorted(read[::-1]))
    #update
    # update = postgresql.update(10, 1)
    # print(update)
    # delete
    # delete = postgresql.delete(4)
    # print(delete)
    main()




