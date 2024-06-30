# Restaurant-management

This is a simple restaurant management system using Tkinter, a Python library for creating graphical user interfaces (GUIs). The program has a window with three main frames: `receipt_frame`, `menu_frame`, and `button_frame`.

### 1. `receipt_frame`

This frame contains an entry field for entering the receipt number, a listbox for displaying the items in the receipt, and buttons for adding, deleting, and modifying items in the receipt.

### 2. `menu_frame`

This frame contains two listboxes for displaying the available drinks and foods, and buttons for adding items to the receipt.

### 3. `button_frame`

This frame contains two buttons for exiting the program and calculating the total price of the receipt.

The program connects to a MySQL database to store and manage the data. It creates a database called `RESTAURANT` and tables called `MENU` and `RECEIPT`. It also creates a view called `MENU_RECEIPT` to display the items in the receipt.

The program inserts some sample data into the `MENU` table and creates a simple GUI for adding, deleting, and modifying items in the receipt. It also provides a way to calculate the total price of the receipt.

### To run the program, you need to have Python and Tkinter installed on your computer. You also need to have a MySQL database server running and accessible from your computer.
