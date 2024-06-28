import mysql.connector

if __name__ != '__main__':
    class Database:
        def __init__(self, user, password, host):
            self.mydb = mysql.connector.connect(user=user, password=password, host=host)
            self.curser = self.mydb.cursor()

        def create_database(self, database_name):
            self.curser.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
            self.curser.execute(f'USE {database_name}')

        def create_table(self,table_one,table_two):
            self.curser.execute(f'CREATE TABLE IF NOT EXISTS {table_one}(ID INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(255) UNIQUE NOT NULL,PRICE INT NOT NULL,IS_FOOD BOOLEAN DEFAULT TRUE)')
            self.curser.execute(f'CREATE TABLE IF NOT EXISTS {table_two}(ID INT AUTO_INCREMENT PRIMARY KEY,RECEIPT_ID INT,MENU_ID INT,COUNT INT,FOREIGN KEY(MENU_ID) REFERENCES {table_one}(ID))')

        def insert_data(self, table_name, data):
            sql = f'INSERT INTO {table_name}({", ".join(data.keys())}) VALUES({", ".join(["%s" for _ in range(len(data))])})'
            self.curser.executemany(sql, [tuple(data.values())])
            
        def get_data(self, table_name, condition=None):
            if condition is None:
                self.curser.execute(f'SELECT * FROM {table_name}')
            else:
                self.curser.execute(f'SELECT * FROM {table_name} WHERE {condition}')
            return self.curser.fetchall()

        def commit(self):
            self.mydb.commit()

        def close(self):
            self.curser.close()
            self.mydb.close()