#Tkinter header
from Tkinter import *
import time
import threading
win = Tk()
win.wm_title("MixxMaster")

#initializing variables
fans = 0
lyrics = 1
jingle = 0
song = 0
video = 0
jingle_cost = 15
song_cost = 100
video_cost = 500

#tkinter elements
fans_label = Label(win, text = "Number of fans")
fans_display = Label(win, text = "0")
big_button = Button(win, text = "Write a lyric - +1 fans/click", command = lambda: click(lyrics))
jingle_button = Button(win, text = "Make a jingle - +0.1 fans/sec", command = lambda: jingle_add())
jingle_count = Label(win, text = "0")
jingle_cost_display = Label(win, text = "Cost - 15")
song_button = Button(win, text = "Finish a song - +0.5 fans/sec", command = lambda: song_add())
song_count = Label(win, text = "0")
song_cost_display = Label(win, text = "Cost - 100")
video_button = Button(win, text = "Get your own music video - +4 fans/sec", command = lambda: video_add())
video_count = Label(win, text = "0")
video_cost_display = Label(win, text = "Cost - 500")

#button click
def click(lyrics):
    global fans
    fans += lyrics
    fans_display.configure(text = str(fans))
    fans_display.update_idletasks()

#adding buildings
def jingle_add():
    global fans
    global jingle
    global jingle_cost
    if fans >= jingle_cost:
        fans -= jingle_cost
        jingle_cost = round(jingle_cost * (1.07**jingle), 1)
        jingle += 1
        jingle_cost_display.configure(text = "Cost - "+str(jingle_cost))
        jingle_cost_display.update_idletasks()
        jingle_count.configure(text = str(jingle))
        jingle_count.update_idletasks()
def song_add():
    global fans
    global song
    global song_cost
    if fans >= song_cost:
        fans -= song_cost
        song_cost = round(song_cost * (1.07**song), 1)
        song += 1
        song_cost_display.configure(text = "Cost - "+str(song_cost))
        song_cost_display.update_idletasks()
        song_count.configure(text = str(song))
        song_count.update_idletasks()
def video_add():
    global fans
    global video
    global video_cost
    if fans >= video_cost:
        fans -= video_cost
        video_cost = round(video_cost * (1.07**video), 1)
        video += 1
        video_cost_display.configure(text = "Cost - "+str(video_cost))
        video_cost_display.update_idletasks()
        video_count.configure(text = str(video))
        video_count.update_idletasks()
        
#update fan amount every second
def update_count():
    global fans
    global jingle
    global song
    fans += (jingle * .1)
    fans += (song * .5)
    fans += (video * 4)
    fans_display.configure(text = str(fans))
    fans_display.update_idletasks()
    threading.Timer(1, update_count).start()

#tkinter arrangement
big_button.grid(row = 1, column = 0)
fans_label.grid(row = 2, column = 0)
fans_display.grid(row = 3, column = 0)
jingle_button.grid(row = 1, column = 1)
jingle_cost_display.grid(row = 2, column = 1)
jingle_count.grid(row = 3, column = 1)
song_button.grid(row = 1, column = 2)
song_cost_display.grid(row = 2, column = 2)
song_count.grid(row = 3, column = 2)
video_button.grid(row = 1, column = 3)
video_cost_display.grid(row = 2, column = 3)
video_count.grid(row = 3, column = 3)

update_count() #starting update for fan count
win.mainloop()