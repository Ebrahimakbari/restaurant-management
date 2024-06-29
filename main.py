from tkinter import *
from tkinter.font import *
from mysql_db import Database

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

# ********************************************************************************** دیتابیس #

db = Database('root', 'admin@1997', 'localhost')
db.create_database('RESTAURANT')
db.create_table('MENU', 'RECEIPT')
db.insert_data('MENU', {'NAME': 'ماهی باکس', 'PRICE': 120000})
db.insert_data('MENU', {'NAME': 'کباب', 'PRICE': 150000})
db.insert_data('MENU', {'NAME': 'نوشابه', 'PRICE': 100000,'IS_FOOD':False})
db.commit()
drinks = db.get_data('MENU','is_food=False')
foods = db.get_data('MENU','is_food=True')
max_receipt = db.get_max_receipt('RECEIPT')
db.close()

# ********************************************************************************** صورت حساب #

receipt_frame = LabelFrame(window,text='صورت حساب' ,font=vfont,padx=5,pady=5)
receipt_frame.grid(row=0,column=0,sticky='nsew',padx=5,pady=5)
receipt_frame.rowconfigure(1,weight=1)
receipt_frame.columnconfigure(0,weight=1)

entry_frame = Entry(receipt_frame,justify='center',width=10,font=vfont)
entry_frame.grid(row=0,column=0)
if max_receipt[0][0] == None:
    max_receipt = 0
max_receipt += 1
entry_frame.insert('0',max_receipt)

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
drink_frame.columnconfigure(0,weight=1)
drink_frame.rowconfigure(0,weight=1)
drink_box = Listbox(drink_frame,font=vfont,justify='center',exportselection=False)
drink_box.grid(row=0,column=0,sticky='nsew')
for o in drinks:
    drink_box.insert('end',o[1])
drink_box.configure(justify=RIGHT) 

food_frame = LabelFrame(menu_frame,text='غذا ها',font=vfont)
food_frame.grid(row=0,column=1,sticky='nsew')
food_frame.columnconfigure(0,weight=1)
food_frame.rowconfigure(0,weight=1)
food_box = Listbox(food_frame,font=vfont,justify='center',exportselection=False)
food_box.grid(row=0,column=0,sticky='nsew')
for a in foods:
    food_box.insert('end',a[1])
food_box.configure(justify=RIGHT)   

# ********************************************************************************** دکمه ها  #
button_frame = LabelFrame(window ,font=vfont,padx=5,pady=5)
button_frame.grid(row=1,column=1,padx=5,pady=5)

exit_button = Button(button_frame,text='خروج' ,font=vfont)
exit_button.grid(row=0,column=0)

calculate_button = Button(button_frame,text='محاسبه قیمت' ,font=vfont)
calculate_button.grid(row=0,column=1)
window.mainloop()
