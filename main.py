from tkinter import *
from tkinter.font import *
import mysql.connector

window = Tk()
window.title("مدیریت رستوران")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")
window.state('zoomed')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.rowconfigure(0, weight=1)
vfont = Font(family="Vazir", size=16)

# ********************************************************************************** mysql-database  #

class Database:
    def __init__(self, user, password, host):
        self.mydb = mysql.connector.connect(user=user, password=password, host=host)
        self.curser = self.mydb.cursor()

    def create_database(self, database_name):
        self.curser.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
        self.curser.execute(f'USE {database_name}')

    def create_table(self,table_one,table_two):
        self.curser.execute(f'CREATE TABLE IF NOT EXISTS {table_one}(ID INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(255) UNIQUE NOT NULL,PRICE INT NOT NULL)')
        self.curser.execute(f'CREATE TABLE IF NOT EXISTS {table_two}(ID INT AUTO_INCREMENT PRIMARY KEY,RECEIPT_ID INT,MENU_ID INT,COUNT INT,FOREIGN KEY(MENU_ID) REFERENCES {table_one}(ID))')

    def insert_data(self, table_name, data):
        sql = f'INSERT INTO {table_name}({", ".join(data.keys())}) VALUES({", ".join(["%s" for _ in range(len(data))])})'
        self.curser.executemany(sql, [tuple(data.values())])

    def commit(self):
        self.mydb.commit()

    def close(self):
        self.curser.close()
        self.mydb.close()

# Usage

db = Database('root', 'admin@1997', 'localhost')
db.create_database('RESTAURANT')
db.create_table('MENU', 'RECEIPT')
db.insert_data('MENU', {'NAME': 'ماهی باکس', 'PRICE': 120000})
db.insert_data('MENU', {'NAME': 'کباب', 'PRICE': 150000})
db.insert_data('MENU', {'NAME': 'سوسیس', 'PRICE': 100000})
db.insert_data('RECEIPT', {'RECEIPT_ID': 1, 'MENU_ID': 1, 'COUNT': 1})
db.commit()
db.close()

# ********************************************************************************** صورت حساب #

receipt_frame = LabelFrame(window,text='صورت حساب' ,font=vfont,padx=5,pady=5)
receipt_frame.grid(row=0,column=0,sticky='nsew',padx=5,pady=5)
receipt_frame.rowconfigure(1,weight=1)
receipt_frame.columnconfigure(0,weight=1)

entry_frame = Entry(receipt_frame,justify='center',width=10,font=vfont)
entry_frame.grid(row=0,column=0)

listbox_frame = Listbox(receipt_frame)
listbox_frame.grid(row=1,column=0,padx=5,pady=5,sticky='nsew')

receipt_button = LabelFrame(receipt_frame)
receipt_button.grid(row=2,column=0,sticky='nsew')

receipt_button.columnconfigure(0,weight=1)
receipt_button.columnconfigure(1,weight=1)
receipt_button.columnconfigure(2,weight=1)
receipt_button.columnconfigure(3,weight=1)

delete_button = Button(receipt_button,text='حذف صورت حساب',font=vfont)
delete_button.grid(row=0,column=0,sticky='nsew')
new_button=Button(receipt_button,text='اضافه کردن صورت حساب',font=vfont)
new_button.grid(row=0,column=1,sticky='nsew')
add_button = Button(receipt_button,text='+',font=vfont)
add_button.grid(row=0,column=2,sticky='nsew')
minus_button=Button(receipt_button,text='-',font=vfont)
minus_button.grid(row=0,column=3,sticky='nsew')

# ********************************************************************************** منو محصولات #

menu_frame = LabelFrame(window,text='منو محصولات' ,font=vfont,padx=5,pady=5)
menu_frame.grid(row=0,column=1,sticky='nsew',padx=5,pady=5)

menu_frame.columnconfigure(0,weight=1)
menu_frame.columnconfigure(1,weight=2)
menu_frame.rowconfigure(0,weight=1)

drink_frame = LabelFrame(menu_frame,text='نوشیدنی ها',font=vfont)
drink_frame.grid(row=0,column=0,sticky='nsew')
food_frame = LabelFrame(menu_frame,text='غذا ها',font=vfont)
food_frame.grid(row=0,column=1,sticky='nsew')

# ********************************************************************************** دکمه ها  #
button_frame = LabelFrame(window ,font=vfont,padx=5,pady=5)
button_frame.grid(row=1,column=1,padx=5,pady=5)

exit_button = Button(button_frame,text='خروج' ,font=vfont)
exit_button.grid(row=0,column=0)

calculate_button = Button(button_frame,text='محاسبه قیمت' ,font=vfont)
calculate_button.grid(row=0,column=1)
window.mainloop()
