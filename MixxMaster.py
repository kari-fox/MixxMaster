#import and Tkinter header
from Tkinter import *
import time
import threading
import pickle
win = Tk()
win.wm_title("MixxMaster")
bg = PhotoImage(file = "/Users/kariselph/Desktop/MixxMaster/images/bg.gif")
w = bg.width()
h = bg.height()
win.geometry('%dx%d+0+0' % (w,h))
background_label = Label(win, image = bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#initializing variables
data = {'fans': 0, 'lyrics': 1, 'jingle': 0, 'song': 0, 'video': 0, 'jingle_cost': 15, 'song_cost': 100, 'video_cost': 500, 'album': 0, 'album_cost': 3000, 'jingle_gain': .1, 'song_gain': .5, 'video_gain': 4, 'album_gain': 10}

#tkinter elements
fans_label = Label(win, text = "Number of fans")
fans_display = Label(win, text = "0")
big_button = Button(win, text = "Write a lyric - +1 fans/click", command = lambda: click(data['fans'], data['lyrics']))
jingle_button = Button(win, text = "Make a jingle - +0.1 fans/sec", command = lambda: data['fans'], data['jingle_cost'], data['jingle'] = jingle_add(data['fans'], data['jingle_cost'], data['jingle']))
jingle_count = Label(win, text = "0")
jingle_cost_display = Label(win, text = "Cost - 15")
song_button = Button(win, text = "Finish a song - +0.5 fans/sec", command = lambda: song_add())
song_count = Label(win, text = "0")
song_cost_display = Label(win, text = "Cost - 100")
video_button = Button(win, text = "Get your own music video - +4 fans/sec", command = lambda: video_add())
video_count = Label(win, text = "0")
video_cost_display = Label(win, text = "Cost - 500")
album_button = Button(win, text = "Drop an album - +10 fans/sec", command = lambda: album_add())
album_count = Label(win, text = "0")
album_cost_display = Label(win, text = "Cost - 3,000")
save_button = Button(win, text = "Save and Quit", command = lambda: save())
load_button = Button(win, text = "Load Save State", command = lambda: load())

#button click
def click(fans, lyrics):
    fans += lyrics
    data['fans'] = fans
    update_displays()
    
#adding buildings
def jingle_add(fans, cost, building):
    if fans >= cost:
        fans -= cost
        cost = round(cost * (1.07**building), 1)
        building += 1
        return fans, cost, building
def song_add():
    if data['fans'] >= data['song_cost']:
        data['fans'] -= data['song_cost']
        data['song_cost'] = round(data['song_cost'] * (1.07**data['song']), 1)
        data['song'] += 1
        update_displays()
def video_add():
    if data['fans'] >= data['video_cost']:
        data['fans'] -= data['video_cost']
        data['video_cost'] = round(data['video_cost'] * (1.07**data['video']), 1)
        data['video'] += 1
        update_displays()
def album_add():
    if data['fans'] >= data['album_cost']:
        data['fans'] -= data['album_cost']
        data['album_cost'] = round(data['album_cost'] * (1.07**data['album']), 1)
        data['album'] += 1
        update_displays()
        
#update fan amount
def update_count():
    data['fans'] = (data['jingle'] * data['jingle_gain']) + (data['song'] * data['song_gain']) + (data['video'] * data['video_gain']) + (data['album'] * data['album_gain']) + data['fans']
    update_displays()
    threading.Timer(1, update_count).start()
    
#update displays
def update_displays():
    fans_display.configure(text = str(data['fans']))
    jingle_cost_display.configure(text = "Cost - "+str(data['jingle_cost']))
    jingle_count.configure(text = str(data['jingle']))
    song_cost_display.configure(text = "Cost - "+str(data['song_cost']))
    song_count.configure(text = str(data['song']))
    video_cost_display.configure(text = "Cost - "+str(data['video_cost']))
    video_count.configure(text = str(data['video']))
    album_cost_display.configure(text = "Cost - "+str(data['album_cost']))
    album_count.configure(text = str(data['album']))

#save and quit
def save():
    fileObject = open('/Users/kariselph/Desktop/MixxMaster/savefile.dat', 'wb')
    pickle.dump(data, fileObject)
    fileObject.close()
    win.destroy()

#load save state
def load():
    fileObject = open('/Users/kariselph/Desktop/MixxMaster/savefile.dat', 'rb')
    data.update(pickle.load(fileObject))
    fileObject.close()
    update_displays()

#tkinter window build
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
album_button.grid(row = 1, column = 4)
album_cost_display.grid(row = 2, column = 4)
album_count.grid(row = 3, column = 4)
save_button.grid(row = 4, column = 0)
load_button.grid(row = 4, column = 1)

update_count() #starting update for fan count
win.mainloop()