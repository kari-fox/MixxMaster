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
big_button = Button(win, text = "Write a lyric - +1 fans/click", command = lambda: click())
jingle_button = Button(win, text = "Make a jingle - +0.1 fans/sec", command = lambda: add_to_target('fans', 'jingle_cost', 'jingle'))
jingle_count = Label(win, text = "0")
jingle_cost_display = Label(win, text = "Cost - 15")
song_button = Button(win, text = "Finish a song - +0.5 fans/sec", command = lambda: add_to_target('fans', 'song_cost', 'song'))
song_count = Label(win, text = "0")
song_cost_display = Label(win, text = "Cost - 100")
video_button = Button(win, text = "Get your own music video - +4 fans/sec", command = lambda: add_to_target('fans', 'video_cost', 'video'))
video_count = Label(win, text = "0")
video_cost_display = Label(win, text = "Cost - 500")
album_button = Button(win, text = "Drop an album - +10 fans/sec", command = lambda: add_to_target('fans', 'album_cost', 'album'))
album_count = Label(win, text = "0")
album_cost_display = Label(win, text = "Cost - 3,000")
save_button = Button(win, text = "Save and Quit", command = lambda: save())
load_button = Button(win, text = "Load Save State", command = lambda: load())

#button click
def click():
    data['fans'] += data['lyrics']
    update_displays()
    
#adding buildings
def building_add(fans, cost, building):
    if fans >= cost:
        fans -= cost
        building += 1
        cost = round(cost * (1.07**building), 1)
        return fans, cost, building
def add_to_target(k1, k2, k3):
    data[k1], data[k2], data[k3] = building_add(data[k1], data[k2], data[k3])
    update_displays()
        
#update fan amount
def update_count():
    global t
    data['fans'] = (data['jingle'] * data['jingle_gain']) + (data['song'] * data['song_gain']) + (data['video'] * data['video_gain']) + (data['album'] * data['album_gain']) + data['fans']
    update_displays()
    t = threading.Timer(1, update_count)
    t.start()
    
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
    t.cancel()
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