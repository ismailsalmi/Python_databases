from base64 import main
import pymysql.cursors

class Mysqldb:
    # Connect to the database
    try:
        con = pymysql.connect(
            host='localhost',
            user='username',
            password='password',
            db='mydb', charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        cursor = con.cursor()
    except (Exception, pymysql.Error) as connection_error:
        print(connection_error)

    # creat table on database
    def creat_table(self):
        try:
            self.cursor.execute('''
            CREATE TABLE laptops (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `brand` varchar(255) COLLATE utf8_bin NOT NULL,
            `model` varchar(255) COLLATE utf8_bin NOT NULL,
            PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
            AUTO_INCREMENT=1 ;''')
        except (Exception, pymysql.Error) as table_error:
            return table_error
        return 'Table is created'
    #insert recoed on table
    def insert(self, id:int, brand:str, model:str):
        try:
            self.cursor.execute('''
            insert into laptops values(%s, %s, %s)
            ''', (id, brand, model))
        except () as insert_error:
            return insert_error
        self.con.commit()
        return 'Record inserted'
    # read records
    def read(self):
        try:
            self.cursor.execute("select id, brand, model from laptops")
        except (Exception, pymysql.Error) as select_error:
            return select_error
        rows = self.cursor.rowcount
        mach = 'row' if rows < 1 else 'rows'
        print(rows, mach)
        return self.cursor.fetchall()
    #update record
    def update(self, brand, model, id):
        try:
            self.cursor.execute('''
            update laptops set brand=%s, model=%s where id = %s'''
                                , (brand, model, id))
        except (Exception, pymysql.Error) as update_erroe:
            return update_erroe
        self.con.commit()
        return 'Record updated'
    #delete
    def delete(self, id):
        try:
            self.cursor.execute("delete from laptops where id = %s", (id,))
        except (Exception, pymysql.Error) as delete_error:
            return delete_error
        return 'Record deleted'
if __name__ == "__main__":
    mysql = Mysqldb()
    # creat table
    # creat_table = mysql.creat_table()
    # print(creat_table)
    #insert
    # insert = mysql.insert(1, 'hp', 'E401')
    # print(insert)
    #read
    read = mysql.read()
    print(read)
    # update
    # update = mysql.update(id=1, brand='lenovo', model='yoga')
    # print(update)
    # delete
    delete = mysql.delete(1)
    print(delete)
    main()