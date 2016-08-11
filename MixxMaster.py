#import and Tkinter header
from Tkinter import *
import time
import threading
import pickle
import os
import math
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

#building elements
class Buttons(object):
    def __init__(self, button_txt, cost_txt, upgrade_txt, gain_txt, upgrade_cost_txt, cost_data, name, gain_data, upgrade_data):
        self.button_txt = button_txt
        self.cost_txt = cost_txt
        self.upgrade_txt = upgrade_txt
        self.gain_txt = gain_txt
        self.upgrade_cost_txt = upgrade_cost_txt
        self.cost_data = cost_data
        self.name = name
        self.gain_data = gain_data
        self.upgrade_data = upgrade_data  
    def pieces(self):
        self.frame = Frame(win, bg = bgcolor, borderwidth = 2, relief = RIDGE, width = 385, height = 74)
        self.button = Button(self.frame, text = self.button_txt, highlightbackground = bgcolor, command = lambda: add_to_target('fans', self.cost_data, self.name))
        self.count = Label(self.frame, text = "Owned: 0", bg = bgcolor, fg = 'white', font = 'Helvetica')
        self.cost_display = Label(self.frame, text = self.cost_txt, bg = bgcolor, fg = 'white', font = 'Helvetica')
        self.upgrade_button = Button(self.frame, text = self.upgrade_txt, highlightbackground = bgcolor, command = lambda: upgrade_target('fans', self.gain_data, self.upgrade_data, self.name))
        self.gain_label = Label(self.frame, text = self.gain_txt, bg = bgcolor, fg = 'white', font = 'Helvetica')
        self.upgrade_cost_label = Label(self.frame, text = self.upgrade_cost_txt, bg = bgcolor, fg = 'white', font = 'Helvetica')
    def update(self):
        self.cost_display.configure(text = "Cost: " + break_point(data[self.cost_data]))
        self.count.configure(text = 'Owned: ' + break_point(data[self.name]))
        self.gain_label.configure(text = '+' + break_point(data[self.gain_data]) + ' fans/sec')
        self.upgrade_cost_label.configure(text = 'Cost: ' + break_point(data[self.upgrade_data]))
    def inside(self):
        self.button.grid(row = 0, column = 0)
        self.cost_display.grid(row = 1, column = 0)
        self.count.grid(row = 2, column = 0)
        self.upgrade_button.grid(row = 0, column = 1)
        self.gain_label.grid(row = 2, column = 1)
        self.upgrade_cost_label.grid(row = 1, column = 1)
        
jingle = Buttons('Make a jingle', 'Cost: 15', "Double your jingles' output", '+0.1 fans/sec', 'Cost: 100', 'jingle_cost', 'jingle', 'jingle_gain', 'jingle_upgrade_cost')
jingle.pieces()

song = Buttons("Finish a song", "Cost: 100", "Double your songs' output", '+0.5 fans/sec', 'Cost: 1,000', 'song_cost', 'song', 'song_gain', 'song_upgrade_cost')
song.pieces()

video = Buttons("Get your own music video", "Cost: 1,100", "Double your videos' output", '+4 fans/sec', 'Cost: 11,000', 'video_cost', 'video', 'video_gain', 'video_upgrade_cost')
video.pieces()

album = Buttons("Drop an album", "Cost: 12,000", "Double your albums' output", '+10 fans/sec', 'Cost: 120,000', 'album_cost', 'album', 'album_gain', 'album_upgrade_cost')
album.pieces()

gig = Buttons("Get a small gig", "Cost: 130,000", "Double your gigs' output", '+40 fans/sec', 'Cost: 1,300,000', 'gig_cost', 'gig', 'gig_gain', 'gig_upgrade_cost')
gig.pieces()

festival = Buttons("Play at a local festival", "Cost: 1,100", "Double your festivals' output", '+4 fans/sec', 'Cost: 11,000', 'festival_cost', 'festival', 'festival_gain', 'festival_upgrade_cost')
festival.pieces()

headliner = Buttons("Headline a concert", "Cost: 1,100", "Double your headliners' output", '+4 fans/sec', 'Cost: 11,000', 'headliner_cost', 'headliner', 'headliner_gain', 'headliner_upgrade_cost')
headliner.pieces()

tour = Buttons("Go on a concert tour", "Cost: 1,100", "Double your tours' output", '+4 fans/sec', 'Cost: 11,000', 'tour_cost', 'tour', 'tour_gain', 'tour_upgrade_cost')
tour.pieces()

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
    fans_display.configure(text = break_point(data['fans']) + ' fans')
    
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
    fans_display.configure(text = break_point(data['fans']) + ' fans')
    count_timer = threading.Timer(1, update_count)
    count_timer.start()
    
#update displays
def break_point(input):
    if input >= 10**21:
        if str(input)[-30:-27] == '000':
            return (str(input)[:-30] + ' nonillion')
        return (str(input)[:-30] + '.' + str(input)[-30:-27] + ' nonillion')
    if input >= 10**21:
        if str(input)[-27:-24] == '000':
            return (str(input)[:-27] + ' octillion')
        return (str(input)[:-27] + '.' + str(input)[-27:-24] + ' octillion')
    if input >= 10**21:
        if str(input)[-24:-21] == '000':
            return (str(input)[:-24] + ' septillion')
        return (str(input)[:-24] + '.' + str(input)[-24:-21] + ' septillion')
    if input >= 10**21:
        if str(input)[-21:-18] == '000':
            return (str(input)[:-21] + ' sextillion')
        return (str(input)[:-21] + '.' + str(input)[-21:-18] + ' sextillion')
    if input >= 10**18:
        if str(input)[-18:-15] == '000':
            return (str(input)[:-18] + ' quintillion')
        return (str(input)[:-18] + '.' + str(input)[-18:-15] + ' quintillion')
    if input >= 10**15:
        if str(input)[-15:-12] == '000':
            return (str(input)[:-15] + ' quadrillion')
        return (str(input)[:-15] + '.' + str(input)[-15:-12] + ' quadrillion')
    if input >= 10**12:
        if str(input)[-12:-9] == '000':
            return (str(input)[:-12] + ' trillion')
        return (str(input)[:-12] + '.' + str(input)[-12:-9] + ' trillion')
    if input >= 10**9:
        if str(input)[-9:-6] == '000':
            return (str(input)[:-9] + ' billion')
        return (str(input)[:-9] + '.' + str(input)[-9:-6] + ' billion')
    if input >= 10**6:
        if str(input)[-6:-3] == '000':
            return (str(input)[:-6] + ' million')
        return (str(input)[:-6] + '.' + str(input)[-6:-3] + ' million')
    return str('{:,}'.format(input))

def update_displays():
    fans_per_sec_display.configure(text = break_point(data['fans_per_sec']) + ' total fans/sec')
    lyrics_gain_label.configure(text = '+' + break_point(data['lyrics']) + ' fans/click')
    lyrics_upgrade_cost_label.configure(text = 'Cost: ' + break_point(data['lyrics_upgrade_cost']))
    jingle.update()
    song.update()
    video.update()
    album.update()
    gig.update()
    festival.update()
    headliner.update()
    tour.update()
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
header_frame.grid(row = 0 , column = 0, columnspan = 3, sticky = W, pady = (0, 200))
fans_display.grid(row = 1, column = 0)
lyrics_frame.grid(row = 2, column = 0)
jingle.frame.grid_propagate(0)
jingle.frame.grid(row = 1, column = 1, sticky = W, padx = 5, pady = 5)
song.frame.grid_propagate(0)
song.frame.grid(row = 1, column = 2, sticky = W, padx = 5, pady = 5)
video.frame.grid_propagate(0)
video.frame.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
album.frame.grid_propagate(0)
album.frame.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)
gig.frame.grid_propagate(0)
gig.frame.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)
festival.frame.grid_propagate(0)
festival.frame.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)
headliner.frame.grid_propagate(0)
headliner.frame.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)
tour.frame.grid_propagate(0)
tour.frame.grid(row = 4, column = 2, sticky = W, padx = 5, pady = 5)
footer_frame.grid(row = 3, column = 0, rowspan = 2)

#inside frames
header_label.grid(row = 0, column = 0)
fans_per_sec_display.grid(row = 0, column = 0, columnspan = 2)
big_button.grid(row = 1, column = 0)
lyrics_upgrade_button.grid(row = 1, column = 1)
lyrics_gain_label.grid(row = 2, column = 0, columnspan = 2)
lyrics_upgrade_cost_label.grid(row = 3, column = 0, columnspan = 2)
jingle.inside()
song.inside()
video.inside()
album.inside()
gig.inside()
festival.inside()
headliner.inside()
tour.inside()
save_button.grid(row = 4, column = 0, pady = (20, 0))
info_label.grid(row = 1, column = 0)
prestige_button.grid(row = 2, column = 0)
multiplier_label.grid(row = 3, column = 0)

load() #loads saved data
update_count() #starting update for fan count
win.mainloop()
