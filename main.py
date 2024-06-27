from tkinter import *
from tkinter.font import *

window = Tk()
window.title("مدیریت رستوران")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")
window.state('zoomed')
window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=3)
window.rowconfigure(0, weight=1)
vfont = Font(family="B Nazanin", size=16)

# ********************************************************************************** صورت حساب #

receipt_frame = LabelFrame(window,text='صورت حساب' ,font=vfont, bg="green")
receipt_frame.grid(row=0,column=0,sticky='nsew')

# ********************************************************************************** منو محصولات #

menu_frame = LabelFrame(window,text='منو محصولات' ,font=vfont, bg="blue")
menu_frame.grid(row=0,column=1,sticky='nsew')

# ********************************************************************************** دکمه ها  #
button_frame = LabelFrame(window ,font=vfont, bg="red")
button_frame.grid(row=1,column=1)

exit_button = Button(button_frame,text='خروج' ,font=vfont)
exit_button.grid(row=0,column=0)

calculate_button = Button(button_frame,text='محاسبه قیمت' ,font=vfont)
calculate_button.grid(row=0,column=1)
window.mainloop()
