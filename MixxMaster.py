#import and Tkinter header
from Tkinter import *
import time
import threading
import pickle
import os
bg_image = os.path.join('images', 'bg.gif')
header_image = os.path.join('images', 'header.gif')
win = Tk()
win.wm_title("MixxMaster")
bg = PhotoImage(file = bg_image)
w = bg.width()
h = bg.height()
win.geometry('%dx%d+0+0' % (w,h))
background_label = Label(win, image = bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
bgcolor = '#10111E'
header = PhotoImage(file = header_image)

#initializing variables
data = {'fans': 0, 'lyrics': 1, 'jingle': 0, 'song': 0, 'video': 0, 'jingle_cost': 15, 'song_cost': 100, 'video_cost': 500, 'album': 0, 'album_cost': 3000, 'jingle_gain': .1, 'song_gain': .5, 'video_gain': 4, 'album_gain': 10, 'gig': 0, 'gig_cost': 10000, 'gig_gain': 40}

#header elements
header_frame = Frame(win, height = 250)
header_label = Label(header_frame, image = header)

#lyrics elements
fans_label = Label(win, text = "Number of fans", bg = bgcolor, fg = 'white')
fans_display = Label(win, text = "0", bg = bgcolor, fg = 'white')
big_button = Button(win, text = "Write a lyric - +1 fans/click", highlightbackground = bgcolor, command = lambda: click())

#jingle elements
jingle_frame = Frame(win, bg = bgcolor)
jingle_button = Button(jingle_frame, text = "Make a jingle - +0.1 fans/sec", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'jingle_cost', 'jingle'))
jingle_count = Label(jingle_frame, text = "0", bg = bgcolor, fg = 'white')
jingle_cost_display = Label(jingle_frame, text = "Cost - 15", bg = bgcolor, fg = 'white')

#song elements
song_frame = Frame(win, bg = bgcolor)
song_button = Button(song_frame, text = "Finish a song - +0.5 fans/sec", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'song_cost', 'song'))
song_count = Label(song_frame, text = "0", bg = bgcolor, fg = 'white')
song_cost_display = Label(song_frame, text = "Cost - 100", bg = bgcolor, fg = 'white')

# video elements
video_frame = Frame(win, bg = bgcolor)
video_button = Button(video_frame, text = "Get your own music video - +4 fans/sec", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'video_cost', 'video'))
video_count = Label(video_frame, text = "0", bg = bgcolor, fg = 'white')
video_cost_display = Label(video_frame, text = "Cost - 500", bg = bgcolor, fg = 'white')

#album elements
album_frame = Frame(win, bg = bgcolor)
album_button = Button(album_frame, text = "Drop an album - +10 fans/sec", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'album_cost', 'album'))
album_count = Label(album_frame, text = "0", bg = bgcolor, fg = 'white')
album_cost_display = Label(album_frame, text = "Cost - 3,000", bg = bgcolor, fg = 'white')

#gig elements
gig_frame = Frame(win, bg = bgcolor)
gig_button = Button(gig_frame, text = "Get a gig - +40 fans/sec", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'gig_cost', 'gig'))
gig_count = Label(gig_frame, text = "0", bg = bgcolor, fg = 'white')
gig_cost_display = Label(gig_frame, text = "Cost - 10,000", bg = bgcolor, fg = 'white')

#footer elements
save_button = Button(win, text = "Save and Quit", highlightbackground = bgcolor, command = lambda: quit())
load_button = Button(win, text = "Load Save State", highlightbackground = bgcolor, command = lambda: load())
info_label = Label(win, text = '', bg = bgcolor, fg = 'white')

#button click
def click():
    data['fans'] += data['lyrics']
    update_displays()
    
#adding buildings
def building_add(fans, cost, building, name):
    if fans >= cost:
        fans -= cost
        building += 1
        cost = round(cost * (1.07**building), 1)
        info_label.configure(text = 'Bought a ' + name)
    else:
        info_label.configure(text = 'Need more fans!')
    return fans, cost, building
def add_to_target(k1, k2, k3):
    data[k1], data[k2], data[k3] = building_add(data[k1], data[k2], data[k3], k3)
    update_displays()
        
#update fan amount
def update_count():
    global count_timer
    data['fans'] = (data['jingle'] * data['jingle_gain']) + (data['song'] * data['song_gain']) + (data['video'] * data['video_gain']) + (data['album'] * data['album_gain']) + data['fans']
    update_displays()
    count_timer = threading.Timer(1, update_count)
    count_timer.start()
    
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
    gig_cost_display.configure(text = "Cost - "+str(data['gig_cost']))
    gig_count.configure(text = str(data['gig']))

#save and quit
def save():
    fileObject = open('savefile.dat', 'wb')
    pickle.dump(data, fileObject)
    fileObject.close()

def quit():
    count_timer.cancel()
    save_timer.cancel()
    save()
    win.destroy()
    
def autosave():
    info_label.configure(text = 'Saving...')
    global save_timer
    save()
    time.sleep(5)
    info_label.configure(text = '')
    save_timer = threading.Timer(30, autosave)
    save_timer.start()
    
#load save state
def load():
    fileObject = open('savefile.dat', 'rb')
    data.update(pickle.load(fileObject))
    fileObject.close()
    update_displays()
    autosave()

#tkinter window build
#frames
win.grid_columnconfigure(0, weight=1, uniform="fred")
win.grid_columnconfigure(1, weight=1, uniform="fred")
win.grid_columnconfigure(2, weight=1, uniform="fred")
header_frame.grid(row = 0 , column = 0, columnspan = 3, sticky = W, pady = (0, 195))
big_button.grid(row = 1, column = 0)
fans_label.grid(row = 1, column = 1)
fans_display.grid(row = 1, column = 2)
jingle_frame.grid(row = 2, column = 0)
song_frame.grid(row = 2, column = 1)
video_frame.grid(row = 2, column = 2)
album_frame.grid(row = 3, column = 0)
gig_frame.grid(row = 3, column = 1)
save_button.grid(row = 4, column = 0)
load_button.grid(row = 4, column = 1)
info_label.grid(row = 4, column = 2)
#inside frames
header_label.grid(row = 0, column = 0)
jingle_button.grid(row = 0, column = 0)
jingle_cost_display.grid(row = 1, column = 0)
jingle_count.grid(row = 2, column = 0)
song_button.grid(row = 0, column = 0)
song_cost_display.grid(row = 1, column = 0)
song_count.grid(row = 2, column = 0)
video_button.grid(row = 0, column = 0)
video_cost_display.grid(row = 1, column = 0)
video_count.grid(row = 2, column = 0)
album_button.grid(row = 0, column = 0)
album_cost_display.grid(row = 1, column = 0)
album_count.grid(row = 2, column = 0)
gig_button.grid(row = 0, column = 0)
gig_cost_display.grid(row = 1, column = 0)
gig_count.grid(row = 2, column = 0)

update_count() #starting update for fan count
win.mainloop()