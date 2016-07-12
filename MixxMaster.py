#import and Tkinter header
from Tkinter import *
import time
import threading
import pickle
import os
import math
bg_image = os.path.join('images', 'bg.gif')
header_image = os.path.join('images', 'header.gif')
frame_image1 = os.path.join('images', 'framebg.gif')
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
frame1 = PhotoImage(file = frame_image1)

#initializing variables
data = {'fans': 0, 'fans_per_sec': 0, 'jingle': 0, 'song': 0, 'video': 0, 'album': 0, 'gig': 0, 'festival': 0, 'headliner': 0, 'tour': 0, 'lyrics': 1, 'lyrics_upgrade_cost': 50, 'jingle_cost': 15, 'jingle_gain': .1, 'jingle_upgrade_cost': 100, 'song_cost': 100, 'song_gain': 1, 'song_upgrade_cost': 1000, 'video_cost': 1100, 'video_gain': 8, 'video_upgrade_cost': 11000, 'album_cost': 12000, 'album_gain': 47, 'album_upgrade_cost': 120000, 'gig_cost': 130000, 'gig_gain': 260, 'gig_upgrade_cost': 1300000, 'festival_cost': 1400000, 'festival_gain': 1400, 'festival_upgrade_cost': 14000000, 'headliner_cost': 20000000, 'headliner_gain': 7800, 'headliner_upgrade_cost': 200000000, 'tour_cost': 330000000, 'tour_gain': 44000, 'tour_upgrade_cost': 3300000000, 'multiplier': 1, 'forever_fans': 0, 'prestige': 0}

#header elements
header_frame = Frame(win)
header_label = Label(header_frame, image = header)

#lyrics elements
lyrics_frame = Frame(win, bg = bgcolor)
fans_display = Label(win, text = "0 fans", font = ('Helvetica', 30), bg = bgcolor, fg = 'white')
fans_per_sec_display = Label(lyrics_frame, text = '0 total fans/sec', bg = bgcolor, fg = 'white', font = 'Helvetica')
big_button = Button(lyrics_frame, text = "Write a lyric", command = lambda: click(), highlightbackground = bgcolor)
lyrics_upgrade_button = Button(lyrics_frame, text = "Double your lyrics' output", command = lambda: upgrade_target('fans', 'lyrics', 'lyrics_upgrade_cost', 'lyrics'), highlightbackground = bgcolor)
lyrics_gain_label = Label(lyrics_frame, text = '+1 fans/click', bg = bgcolor, fg = 'white', font = 'Helvetica')
lyrics_upgrade_cost_label = Label(lyrics_frame, text = 'Cost: 100', bg = bgcolor, fg = 'white', font = 'Helvetica')

#jingle elements
jingle_frame = Frame(win, bg = bgcolor, borderwidth = 2, relief = RIDGE)
jingle_frame_label = Label(jingle_frame, image = frame1, bg = bgcolor)
jingle_frame_label.place(x=0, y=0, relwidth=1, relheight=1)
jingle_button = Button(jingle_frame, text = "Make a jingle", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'jingle_cost', 'jingle'))
jingle_count = Label(jingle_frame, text = "Owned: 0", bg = bgcolor, fg = 'white', font = 'Helvetica')
jingle_cost_display = Label(jingle_frame, text = "Cost: 15", bg = bgcolor, fg = 'white', font = 'Helvetica')
jingle_upgrade_button = Button(jingle_frame, text = "Double your jingles' output", highlightbackground = bgcolor, command = lambda: upgrade_target('fans', 'jingle_gain', 'jingle_upgrade_cost', 'jingle'))
jingle_gain_label = Label(jingle_frame, text = '+0.1 fans/sec', bg = bgcolor, fg = 'white', font = 'Helvetica')
jingle_upgrade_cost_label = Label(jingle_frame, text = 'Cost: 100', bg = bgcolor, fg = 'white', font = 'Helvetica')

#song elements
song_frame = Frame(win, bg = bgcolor, borderwidth = 2, relief = RIDGE)
song_frame_label = Label(song_frame, image = frame1, bg = bgcolor)
song_frame_label.place(x=0, y=0, relwidth=1, relheight=1)
song_button = Button(song_frame, text = "Finish a song", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'song_cost', 'song'))
song_count = Label(song_frame, text = "Owned: 0", bg = bgcolor, fg = 'white', font = 'Helvetica')
song_cost_display = Label(song_frame, text = "Cost: 100", bg = bgcolor, fg = 'white', font = 'Helvetica')
song_upgrade_button = Button(song_frame, text = "Double your songs' output", highlightbackground = bgcolor, command = lambda: upgrade_target('fans', 'song_gain', 'song_upgrade_cost', 'song'))
song_gain_label = Label(song_frame, text = '+0.5 fans/sec', bg = bgcolor, fg = 'white', font = 'Helvetica')
song_upgrade_cost_label = Label(song_frame, text = 'Cost: 1,000', bg = bgcolor, fg = 'white', font = 'Helvetica')

# video elements
video_frame = Frame(win, bg = bgcolor, borderwidth = 2, relief = RIDGE)
video_frame_label = Label(video_frame, image = frame1, bg = bgcolor)
video_frame_label.place(x=0, y=0, relwidth=1, relheight=1)
video_button = Button(video_frame, text = "Get your own music video", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'video_cost', 'video'))
video_count = Label(video_frame, text = "Owned: 0", bg = bgcolor, fg = 'white', font = 'Helvetica')
video_cost_display = Label(video_frame, text = "Cost: 1,100", bg = bgcolor, fg = 'white', font = 'Helvetica')
video_upgrade_button = Button(video_frame, text = "Double your videos' output", highlightbackground = bgcolor, command = lambda: upgrade_target('fans', 'video_gain', 'video_upgrade_cost', 'video'))
video_gain_label = Label(video_frame, text = '+4 fans/sec', bg = bgcolor, fg = 'white', font = 'Helvetica')
video_upgrade_cost_label = Label(video_frame, text = 'Cost: 11,000', bg = bgcolor, fg = 'white', font = 'Helvetica')

#album elements
album_frame = Frame(win, bg = bgcolor, borderwidth = 2, relief = RIDGE)
album_frame_label = Label(album_frame, image = frame1, bg = bgcolor)
album_frame_label.place(x=0, y=0, relwidth=1, relheight=1)
album_button = Button(album_frame, text = "Drop an album", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'album_cost', 'album'))
album_count = Label(album_frame, text = "Owned: 0", bg = bgcolor, fg = 'white', font = 'Helvetica')
album_cost_display = Label(album_frame, text = "Cost: 12,000", bg = bgcolor, fg = 'white', font = 'Helvetica')
album_upgrade_button = Button(album_frame, text = "Double your albums' output", highlightbackground = bgcolor, command = lambda: upgrade_target('fans', 'album_gain', 'album_upgrade_cost', 'album'))
album_gain_label = Label(album_frame, text = '+10 fans/sec', bg = bgcolor, fg = 'white', font = 'Helvetica')
album_upgrade_cost_label = Label(album_frame, text = 'Cost: 120,000', bg = bgcolor, fg = 'white', font = 'Helvetica')

#gig elements
gig_frame = Frame(win, bg = bgcolor, borderwidth = 2, relief = RIDGE)
gig_frame_label = Label(gig_frame, image = frame1, bg = bgcolor)
gig_frame_label.place(x=0, y=0, relwidth=1, relheight=1)
gig_button = Button(gig_frame, text = "Get a small gig", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'gig_cost', 'gig'))
gig_count = Label(gig_frame, text = "Owned: 0", bg = bgcolor, fg = 'white', font = 'Helvetica')
gig_cost_display = Label(gig_frame, text = "Cost: 130,000", bg = bgcolor, fg = 'white', font = 'Helvetica')
gig_upgrade_button = Button(gig_frame, text = "Double your gigs' output", highlightbackground = bgcolor, command = lambda: upgrade_target('fans', 'gig_gain', 'gig_upgrade_cost', 'gig'))
gig_gain_label = Label(gig_frame, text = '+40 fans/sec', bg = bgcolor, fg = 'white', font = 'Helvetica')
gig_upgrade_cost_label = Label(gig_frame, text = 'Cost: 1,300,000', bg = bgcolor, fg = 'white', font = 'Helvetica')

#festival elements
festival_frame = Frame(win, bg = bgcolor, borderwidth = 2, relief = RIDGE)
festival_frame_label = Label(festival_frame, image = frame1, bg = bgcolor)
festival_frame_label.place(x=0, y=0, relwidth=1, relheight=1)
festival_button = Button(festival_frame, text = "Play at a local festival", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'festival_cost', 'festival'))
festival_count = Label(festival_frame, text = "Owned: 0", bg = bgcolor, fg = 'white', font = 'Helvetica')
festival_cost_display = Label(festival_frame, text = "Cost: 1,400,000", bg = bgcolor, fg = 'white', font = 'Helvetica')
festival_upgrade_button = Button(festival_frame, text = "Double your festivals' output", highlightbackground = bgcolor, command = lambda: upgrade_target('fans', 'festival_gain', 'festival_upgrade_cost', 'festival'))
festival_gain_label = Label(festival_frame, text = '+100 fans/sec', bg = bgcolor, fg = 'white', font = 'Helvetica')
festival_upgrade_cost_label = Label(festival_frame, text = 'Cost: 14,000,000', bg = bgcolor, fg = 'white', font = 'Helvetica')

#headliner elements
headliner_frame = Frame(win, bg = bgcolor, borderwidth = 2, relief = RIDGE)
headliner_frame_label = Label(headliner_frame, image = frame1, bg = bgcolor)
headliner_frame_label.place(x=0, y=0, relwidth=1, relheight=1)
headliner_button = Button(headliner_frame, text = "Headline a concert", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'headliner_cost', 'headliner'))
headliner_count = Label(headliner_frame, text = "Owned: 0", bg = bgcolor, fg = 'white', font = 'Helvetica')
headliner_cost_display = Label(headliner_frame, text = "Cost: 20,000,000", bg = bgcolor, fg = 'white', font = 'Helvetica')
headliner_upgrade_button = Button(headliner_frame, text = "Double your headliners' output", highlightbackground = bgcolor, command = lambda: upgrade_target('fans', 'headliner_gain', 'headliner_upgrade_cost', 'headliner'))
headliner_gain_label = Label(headliner_frame, text = '+7,800 fans/sec', bg = bgcolor, fg = 'white', font = 'Helvetica')
headliner_upgrade_cost_label = Label(headliner_frame, text = 'Cost: 200,000,000', bg = bgcolor, fg = 'white', font = 'Helvetica')

#tour elements
tour_frame = Frame(win, bg = bgcolor, borderwidth = 2, relief = RIDGE)
tour_frame_label = Label(tour_frame, image = frame1, bg = bgcolor)
tour_frame_label.place(x=0, y=0, relwidth=1, relheight=1)
tour_button = Button(tour_frame, text = "Go on a concert tour", highlightbackground = bgcolor, command = lambda: add_to_target('fans', 'tour_cost', 'tour'))
tour_count = Label(tour_frame, text = "Owned: 0", bg = bgcolor, fg = 'white', font = 'Helvetica')
tour_cost_display = Label(tour_frame, text = "Cost: 330,000,000", bg = bgcolor, fg = 'white', font = 'Helvetica')
tour_upgrade_button = Button(tour_frame, text = "Double your tours' output", highlightbackground = bgcolor, command = lambda: upgrade_target('fans', 'tour_gain', 'tour_upgrade_cost', 'tour'))
tour_gain_label = Label(tour_frame, text = '+44,000 fans/sec', bg = bgcolor, fg = 'white', font = 'Helvetica')
tour_upgrade_cost_label = Label(tour_frame, text = 'Cost: 3,300,000,000', bg = bgcolor, fg = 'white', font = 'Helvetica')

#footer elements
footer_frame = Frame(win, bg = bgcolor)
save_button = Button(footer_frame, text = "Save and Quit", command = lambda: quit(), highlightbackground = bgcolor)
info_label = Label(footer_frame, text = 'Welcome to MixxMaster!', font = ('Helvetica', 20), bg = bgcolor, fg = 'white')
prestige_button = Button(footer_frame, text = 'Fall from Grace!', command = lambda: maybe(), highlightbackground = bgcolor)
multiplier_label = Label(footer_frame, text = '0 hits', bg = bgcolor, fg = 'white', font = 'Helvetica')

#button click
def click():
    data['fans'] += data['lyrics']
    data['forever_fans'] += data['lyrics']
    fans_display.configure(text = '{:,}'.format(data['fans']) + ' fans')
    
#adding buildings
def add_to_target(k1, k2, k3):
    data[k1], data[k2], data[k3] = building_add(data[k1], data[k2], data[k3], k3)
    update_fans_per_sec()
    update_displays()
def building_add(fans, cost, building, name):
    if fans >= cost:
        fans -= cost
        building += 1
        cost = int(cost * (1.07**building))
        info_label.configure(text = 'Got a ' + name)
    else:
        info_label.configure(text = 'Need more fans!')
    return fans, cost, building
#upgrading buildings
def upgrade_target(k1, k2, k3, k4):
    data[k1], data[k2], data[k3] = upgrade_multiplier(data[k1], data[k2], data[k3], k4)
    update_fans_per_sec()
    update_displays()
def upgrade_multiplier(fans, gain, cost, name):
    if fans >= cost:
        fans -= cost
        gain = int(gain * 2)
        cost = cost * 3
        if name == 'lyrics':
            info_label.configure(text = 'Upgraded your ' + name)
        else:
            info_label.configure(text = 'Upgraded your ' + name + 's')
    else:
        info_label.configure(text = 'Need more fans!')
    return fans, gain, cost
        
#update fan amount
def update_fans_per_sec():
    data['fans_per_sec'] = int(data['multiplier'] * ((data['jingle'] * data['jingle_gain']) + (data['song'] * data['song_gain']) + (data['video'] * data['video_gain']) + (data['album'] * data['album_gain']) + (data['gig'] * data['gig_gain']) + (data['festival'] * data['festival_gain']) + (data['headliner'] * data['headliner_gain']) + (data['tour'] * data['tour_gain'])))

def update_count():
    global count_timer
    data['fans'] = data['fans'] + data['fans_per_sec']
    data['forever_fans'] += data['fans_per_sec']
    fans_display.configure(text = '{:,}'.format(data['fans']) + ' fans')
    count_timer = threading.Timer(1, update_count)
    count_timer.start()
    
#update displays
def update_displays():
    fans_per_sec_display.configure(text = '{:,}'.format(data['fans_per_sec']) + ' total fans/sec')
    lyrics_gain_label.configure(text = '+' + '{:,}'.format(data['lyrics']) + ' fans/click')
    lyrics_upgrade_cost_label.configure(text = 'Cost: ' + '{:,}'.format(data['lyrics_upgrade_cost']))
    jingle_cost_display.configure(text = "Cost: " + '{:,}'.format(data['jingle_cost']))
    jingle_count.configure(text = 'Owned: ' + '{:,}'.format(data['jingle']))
    jingle_gain_label.configure(text = '+' + '{:,}'.format(data['jingle_gain']) + ' fans/sec')
    jingle_upgrade_cost_label.configure(text = 'Cost: ' + '{:,}'.format(data['jingle_upgrade_cost']))
    song_cost_display.configure(text = "Cost: " + '{:,}'.format(data['song_cost']))
    song_count.configure(text = 'Owned: ' + '{:,}'.format(data['song']))
    song_gain_label.configure(text = '+' + '{:,}'.format(data['song_gain']) + ' fans/sec')
    song_upgrade_cost_label.configure(text = 'Cost: ' + '{:,}'.format(data['song_upgrade_cost']))
    video_cost_display.configure(text = "Cost: " + '{:,}'.format(data['video_cost']))
    video_count.configure(text = 'Owned: ' + '{:,}'.format(data['video']))
    video_gain_label.configure(text = '+' + '{:,}'.format(data['video_gain']) + ' fans/sec')
    video_upgrade_cost_label.configure(text = 'Cost: ' + '{:,}'.format(data['video_upgrade_cost']))
    album_cost_display.configure(text = "Cost: " + '{:,}'.format(data['album_cost']))
    album_count.configure(text = 'Owned: ' + '{:,}'.format(data['album']))
    album_gain_label.configure(text = '+' + '{:,}'.format(data['album_gain']) + ' fans/sec')
    album_upgrade_cost_label.configure(text = 'Cost: ' + '{:,}'.format(data['album_upgrade_cost']))
    gig_cost_display.configure(text = "Cost: " + '{:,}'.format(data['gig_cost']))
    gig_count.configure(text = 'Owned: ' + '{:,}'.format(data['gig']))
    gig_gain_label.configure(text = '+' + '{:,}'.format(data['gig_gain']) + ' fans/sec')
    gig_upgrade_cost_label.configure(text = 'Cost: ' + '{:,}'.format(data['gig_upgrade_cost']))
    festival_cost_display.configure(text = "Cost: " + '{:,}'.format(data['festival_cost']))
    festival_count.configure(text = 'Owned: ' + '{:,}'.format(data['festival']))
    festival_gain_label.configure(text = '+' + '{:,}'.format(data['festival_gain']) + ' fans/sec')
    festival_upgrade_cost_label.configure(text = 'Cost: ' + '{:,}'.format(data['festival_upgrade_cost']))
    headliner_cost_display.configure(text = "Cost: " + '{:,}'.format(data['headliner_cost']))
    headliner_count.configure(text = 'Owned: ' + '{:,}'.format(data['headliner']))
    headliner_gain_label.configure(text = '+' + '{:,}'.format(data['headliner_gain']) + ' fans/sec')
    headliner_upgrade_cost_label.configure(text = 'Cost: ' + '{:,}'.format(data['headliner_upgrade_cost']))
    tour_cost_display.configure(text = "Cost: " + '{:,}'.format(data['tour_cost']))
    tour_count.configure(text = 'Owned: ' + '{:,}'.format(data['tour']))
    tour_gain_label.configure(text = '+' + '{:,}'.format(data['tour_gain']) + ' fans/sec')
    tour_upgrade_cost_label.configure(text = 'Cost: ' + '{:,}'.format(data['tour_upgrade_cost']))
    multiplier_label.configure(text = str(data['prestige']) + ' hits!')

#prestige system    
def maybe():
    earn = int(math.floor((data['forever_fans']/(10**13))**(1./3)))
    modal = Toplevel(bg = bgcolor)
    modal.geometry('%dx%d%+d%+d' % (350, 200, 378, 263))
    desc_label = Message(modal, aspect = 300, text = '', fg = 'white', bg = bgcolor)
    desc_label.configure(text = 'Falling from grace will restart your music career, but a handful of diehard fans continue to listen to your greatest hits. Every hit you produce gives you an extra 1 percent of your total fans/sec. Are you ready to crash and burn? You will earn ' + str(earn)+ ' hits now.')
    yes_button = Button(modal, text = 'Yes', highlightbackground = bgcolor, command = lambda: prestige())
    no_button = Button(modal, text = 'No', highlightbackground = bgcolor, command = modal.destroy)
    desc_label.pack()
    yes_button.pack()
    no_button.pack()
    modal.transient(win)
    modal.grab_set()
    win.wait_window(modal)
    
def prestige():
    data['forever_fans'] += data['fans']
    data['prestige'] = int(math.floor((data['forever_fans']/(10**13))**(1./3)))
    data['multiplier'] = data['multiplier'] + (data['prestige']/100.)
    data['fans'] = 0
    data['fans_per_sec'] = 0
    data['jingle'] = 0
    data['song'] = 0
    data['video'] = 0
    data['album'] = 0
    data['gig'] = 0
    data['festival'] = 0
    data['headliner'] = 0
    data['tour'] = 0
    data['lyrics'] = 10
    data['song_gain'] = 10
    data['lyrics_upgrade_cost'] = 500
    data['jingle_cost'] = 150
    data['jingle_gain'] = 1
    data['jingle_upgrade_cost'] = 1000
    data['song_cost'] = 1000
    data['song_upgrade_cost'] = 10000
    data['video_cost'] = 11000
    data['video_gain'] = 80
    data['video_upgrade_cost'] = 110000
    data['album_cost'] = 120000
    data['album_gain'] = 470
    data['album_upgrade_cost'] = 1200000
    data['gig_cost'] = 1300000
    data['gig_gain'] = 2600
    data['gig_upgrade_cost'] = 13000000
    data['festival_cost'] = 14000000
    data['festival_gain'] = 14000
    data['festival_upgrade_cost'] = 140000000
    data['headliner_cost'] = 200000000
    data['headliner_gain'] = 78000
    data['headliner_upgrade_cost'] = 2000000000
    data['tour_cost'] = 3300000000
    data['tour_gain'] = 440000
    data['tour_upgrade_cost'] = 33000000000
    info_label.configure(text = 'Reset the game!')
    update_displays()
    
#save and quit
def save():
    fileObject = open('savefile.dat', 'w')
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
    fileObject = open('savefile.dat', 'r')
    data.update(pickle.load(fileObject))
    fileObject.close()
    update_displays()
    autosave()

#tkinter window build
#frames
win.grid_columnconfigure(0, weight=1, uniform="fred")
win.grid_columnconfigure(1, weight=1, uniform="fred")
win.grid_columnconfigure(2, weight=1, uniform="fred")
header_frame.grid(row = 0 , column = 0, columnspan = 3, sticky = W, pady = (0, 200))
fans_display.grid(row = 1, column = 0, pady = 10)
lyrics_frame.grid(row = 2, column  = 0)
jingle_frame.grid(row = 1, column = 1, sticky = W, pady = 5)
song_frame.grid(row = 1, column = 2, pady = 5)
video_frame.grid(row = 2, column = 1, pady = 5)
album_frame.grid(row = 2, column = 2, pady = 5)
gig_frame.grid(row = 3, column = 1, pady = 5)
festival_frame.grid(row = 3, column = 2, pady = 5)
headliner_frame.grid(row = 4, column = 1, pady = 5)
tour_frame.grid(row = 4, column = 2, pady = 5)
footer_frame.grid(row = 3, column = 0, rowspan = 2)

#inside frames
header_label.grid(row = 0, column = 0)
fans_per_sec_display.grid(row = 0, column = 0, columnspan = 2)
big_button.grid(row = 1, column = 0)
lyrics_upgrade_button.grid(row = 1, column = 1)
lyrics_gain_label.grid(row = 2, column = 0, columnspan = 2)
lyrics_upgrade_cost_label.grid(row = 3, column = 0, columnspan = 2)
jingle_button.grid(row = 0, column = 0)
jingle_cost_display.grid(row = 1, column = 0)
jingle_count.grid(row = 2, column = 0)
jingle_upgrade_button.grid(row = 0, column = 1)
jingle_gain_label.grid(row = 2, column = 1)
jingle_upgrade_cost_label.grid(row = 1, column = 1)
song_button.grid(row = 0, column = 0)
song_cost_display.grid(row = 1, column = 0)
song_count.grid(row = 2, column = 0)
song_upgrade_button.grid(row = 0, column = 1)
song_gain_label.grid(row = 2, column = 1)
song_upgrade_cost_label.grid(row = 1, column = 1)
video_button.grid(row = 0, column = 0)
video_cost_display.grid(row = 1, column = 0)
video_count.grid(row = 2, column = 0)
video_upgrade_button.grid(row = 0, column = 1)
video_gain_label.grid(row = 2, column = 1)
video_upgrade_cost_label.grid(row = 1, column = 1)
album_button.grid(row = 0, column = 0)
album_cost_display.grid(row = 1, column = 0)
album_count.grid(row = 2, column = 0)
album_upgrade_button.grid(row = 0, column = 1)
album_gain_label.grid(row = 2, column = 1)
album_upgrade_cost_label.grid(row = 1, column = 1)
gig_button.grid(row = 0, column = 0)
gig_cost_display.grid(row = 1, column = 0)
gig_count.grid(row = 2, column = 0)
gig_upgrade_button.grid(row = 0, column = 1)
gig_gain_label.grid(row = 2, column = 1)
gig_upgrade_cost_label.grid(row = 1, column = 1)
festival_button.grid(row = 0, column = 0)
festival_cost_display.grid(row = 1, column = 0)
festival_count.grid(row = 2, column = 0)
festival_upgrade_button.grid(row = 0, column = 1)
festival_gain_label.grid(row = 2, column = 1)
festival_upgrade_cost_label.grid(row = 1, column = 1)
headliner_button.grid(row = 0, column = 0)
headliner_cost_display.grid(row = 1, column = 0)
headliner_count.grid(row = 2, column = 0)
headliner_upgrade_button.grid(row = 0, column = 1)
headliner_gain_label.grid(row = 2, column = 1)
headliner_upgrade_cost_label.grid(row = 1, column = 1)
tour_button.grid(row = 0, column = 0)
tour_cost_display.grid(row = 1, column = 0)
tour_count.grid(row = 2, column = 0)
tour_upgrade_button.grid(row = 0, column = 1)
tour_gain_label.grid(row = 2, column = 1)
tour_upgrade_cost_label.grid(row = 1, column = 1)
save_button.grid(row = 4, column = 0, pady = (20, 0))
info_label.grid(row = 1, column = 0)
prestige_button.grid(row = 2, column = 0)
multiplier_label.grid(row = 3, column = 0)

load() #loads saved data
update_count() #starting update for fan count
win.mainloop()
