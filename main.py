from tkinter import *
from tkinter.font import *
from mysql_db import Database
from subprocess import call

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
db.create_view_menu_receipt()
db.insert_data('MENU', {'NAME': 'ماهی باکس', 'PRICE': 120000})
db.insert_data('MENU', {'NAME': 'کباب', 'PRICE': 150000})
db.insert_data('MENU', {'NAME': 'نوشابه', 'PRICE': 100000, 'IS_FOOD': False})
db.insert_data('MENU', {'NAME': 'دوغ', 'PRICE': 200000, 'IS_FOOD': False})
drinks = db.get_data('MENU', 'is_food=False')
foods = db.get_data('MENU', 'is_food=True')


# ********************************************************************************** صورت حساب #

receipt_frame = LabelFrame(window, text='صورت حساب',
                            font=vfont, padx=5, pady=5)
receipt_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
receipt_frame.rowconfigure(1, weight=1)
receipt_frame.columnconfigure(0, weight=1)

entry_frame = Entry(receipt_frame, justify='center', width=10, font=vfont)
entry_frame.grid(row=0, column=0)
max_receipt = db.get_max_receipt('RECEIPT')[0][0]
if max_receipt == None:
    max_receipt = 0
else:
    max_receipt = int(max_receipt)

max_receipt += 1
entry_frame.insert(0, max_receipt)


def entry_event(key):
    try:
        receipt = int(entry_frame.get())
    except:
        receipt = 0
    insert_into_listbox(receipt)


entry_frame.bind('<KeyRelease>', entry_event)

listbox_frame = Listbox(receipt_frame, font=vfont, justify='right')
listbox_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')


def insert_into_listbox(receipt_id):
    listbox_frame.delete(0, 'end')
    receipts = db.get_from_view(receipt_id)
    for receipt in receipts:
        listbox_frame.insert(
            0, f'{receipt[0]}-{receipt[1]} {receipt[2]} {receipt[4]}')


receipt_button = LabelFrame(receipt_frame)
receipt_button.grid(row=2, column=0, sticky='nsew')

receipt_button.columnconfigure(0, weight=1)
receipt_button.columnconfigure(1, weight=1)
receipt_button.columnconfigure(2, weight=1)
receipt_button.columnconfigure(3, weight=1)


def delete_receipt_item():
    receipt_id = entry_frame.get()
    menu_name = listbox_frame.get(listbox_frame.curselection())
    menu_name = menu_name.split('-')[0]
    menu_id = db.get_item_by_name(menu_name)[0]
    db.delete_from_receipt(receipt_id, menu_id)
    insert_into_listbox(receipt_id)


delete_button = Button(receipt_button, text='حذف از صورت حساب',
                        font=vfont, command=delete_receipt_item)
delete_button.grid(row=0, column=0, sticky='nsew')


def add_receipt():
    entry_frame.delete(0, 'end')
    listbox_frame.delete(0, 'end')
    max_receipt = db.get_max_receipt('RECEIPT')[0][0]
    if max_receipt == None:
        max_receipt = 0
    else:
        max_receipt = int(max_receipt)
    max_receipt += 1
    entry_frame.insert(0, max_receipt)


new_button = Button(receipt_button, text='اضافه کردن صورت حساب',
                    font=vfont, command=add_receipt)
new_button.grid(row=0, column=1, sticky='nsew')


def add_item_to_receipt():
    menu_name = listbox_frame.get(listbox_frame.curselection())
    menu_name = menu_name.split('-')[0]
    menu_id = db.get_item_by_name(menu_name)[0]
    receipt_id = entry_frame.get()
    result = db.get_from_receipt(receipt_id, menu_id)
    if len(result) == 0:
        db.insert_to_receipt(receipt_id, menu_id, 1, result[0][4])
    else:
        db.increase_count(receipt_id, menu_id)
    insert_into_listbox(receipt_id)


add_button = Button(receipt_button, text='+', font=vfont,
                    command=add_item_to_receipt)
add_button.grid(row=0, column=2, sticky='nsew')


def delete_item_from_receipt():
    receipt_id = entry_frame.get()
    menu_name = listbox_frame.get(listbox_frame.curselection())
    menu_name = menu_name.split('-')[0]
    menu_id = db.get_item_by_name(menu_name)[0]
    db.decrease_count(receipt_id, menu_id)
    insert_into_listbox(receipt_id)


minus_button = Button(receipt_button, text='-', font=vfont,
                        command=delete_item_from_receipt)
minus_button.grid(row=0, column=3, sticky='nsew')

# ********************************************************************************** منو محصولات #

menu_frame = LabelFrame(window, text='منو محصولات', font=vfont, padx=5, pady=5)
menu_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

menu_frame.columnconfigure(0, weight=1)
menu_frame.columnconfigure(1, weight=2)
menu_frame.rowconfigure(0, weight=1)

drink_frame = LabelFrame(menu_frame, text='نوشیدنی ها', font=vfont)
drink_frame.grid(row=0, column=0, sticky='nsew')
drink_frame.columnconfigure(0, weight=1)
drink_frame.rowconfigure(0, weight=1)
drink_box = Listbox(drink_frame, font=vfont,
                    justify='center', exportselection=False)
drink_box.grid(row=0, column=0, sticky='nsew')
for o in drinks:
    drink_box.insert('end', o[1])
drink_box.configure(justify=RIGHT)


def get_drinks(event):
    drinks_item = db.get_item_by_name(drink_box.get(ACTIVE))
    drink_id = drinks_item[0]
    drink_price = drinks_item[2]
    receipt_id = int(entry_frame.get())
    result = db.get_from_receipt(receipt_id, drink_id)
    if len(result) == 0:
        db.insert_to_receipt(receipt_id, drink_id, 1, drink_price)
    else:
        db.increase_count(receipt_id, drink_id)
    insert_into_listbox(receipt_id)


def get_products(event, product_box):
    product_item = db.get_item_by_name(product_box.get(ACTIVE))
    product_id = product_item[0]
    product_price = product_item[2]
    receipt_id = int(entry_frame.get())
    result = db.get_from_receipt(receipt_id, product_id)
    if len(result) == 0:
        db.insert_to_receipt(receipt_id, product_id, 1, product_price)
    else:
        db.increase_count(receipt_id, product_id)
    insert_into_listbox(receipt_id)


drink_box.bind('<Double-Button>',
                lambda event: get_products(event, product_box=drink_box))

food_frame = LabelFrame(menu_frame, text='غذا ها', font=vfont)
food_frame.grid(row=0, column=1, sticky='nsew')
food_frame.columnconfigure(0, weight=1)
food_frame.rowconfigure(0, weight=1)
food_box = Listbox(food_frame, font=vfont,
                    justify='center', exportselection=False)
food_box.grid(row=0, column=0, sticky='nsew')
for a in foods:
    food_box.insert('end', a[1])

food_box.configure(justify=RIGHT)
food_box.bind('<Double-Button>',
                lambda event: get_products(event, product_box=food_box))

# ********************************************************************************** دکمه ها  #
button_frame = LabelFrame(window, font=vfont, padx=5, pady=5)
button_frame.grid(row=1, column=1, padx=5, pady=5)


def window_handle():
    window.destroy()


exit_button = Button(button_frame, text='خروج',
                    font=vfont, command=window_handle)
exit_button.grid(row=0, column=0)


def calc():
    call(['calc.exe'])


calculate_button = Button(
    button_frame, text='محاسبه قیمت', font=vfont, command=calc)
calculate_button.grid(row=0, column=1)
window.mainloop()
db.close()
