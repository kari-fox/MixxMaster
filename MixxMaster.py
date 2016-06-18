from Tkinter import *
import time
import threading
win = Tk()
win.wm_title("MixxMaster")

count = 0
clicking = 1
building1 = 0
building2 = 0
b1_cost = 15
b2_cost = 100
display_count = Label(win, text = "0")
big_button = Button(win, text = "Click me!", command = lambda: click(clicking))
b1 = Button(win, text = "Building 1", command = lambda: building1_add())
b1_count = Label(win, text = "0")
b1_cost_display = Label(win, text = "Cost - 15")
b2 = Button(win, text = "Building 2", command = lambda: building2_add())
b2_count = Label(win, text = "0")
b2_cost_display = Label(win, text = "Cost - 100")
def click(clicking):
    global count
    count += clicking
    display_count.configure(text = str(count))
    display_count.update_idletasks()
def building1_add():
    global count
    global building1
    global b1_cost
    if count >= b1_cost:
        count -= b1_cost
        b1_cost = round(b1_cost * (1.07**building1), 1)
        building1 += 1
        b1_cost_display.configure(text = "Cost - "+str(b1_cost))
        b1_cost_display.update_idletasks()
        b1_count.configure(text = str(building1))
        b1_count.update_idletasks()
def building2_add():
    global count
    global building2
    global b2_cost
    if count >= b2_cost:
        count -= b2_cost
        b2_cost = round(b2_cost * (1.07**building2), 1)
        building2 += 1
        b2_cost_display.configure(text = "Cost - "+str(b2_cost))
        b2_cost_display.update_idletasks()
        b2_count.configure(text = str(building2))
        b2_count.update_idletasks()
def update_count():
    global count
    global building1
    global building2
    count += (building1 * .1)
    count += (building2 * .5)
    display_count.configure(text = str(count))
    display_count.update_idletasks()
    threading.Timer(1, update_count).start()

big_button.grid(row = 1, column = 0)
display_count.grid(row = 2, column = 0)
b1.grid(row = 1, column = 1)
b1_cost_display.grid(row = 2, column = 1)
b1_count.grid(row = 3, column = 1)
b2.grid(row = 1, column = 2)
b2_cost_display.grid(row = 2, column = 2)
b2_count.grid(row = 3, column = 2)
update_count()
win.mainloop()