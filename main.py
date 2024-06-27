from tkinter import *
from tkinter.font import *

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
