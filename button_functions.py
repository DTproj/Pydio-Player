import random
from tkinter import filedialog as fdg
from pygame import mixer, time, event, QUIT
from threading import Thread


mixer.init()
c_track = 0
tracklist = []
loop_set = False
random_set = False

#
# placeholder
#

def hello():
    print("Hello World")
#
# volume setting
#

def vol_fnc(vol_change, v_label):
    curr_volume = mixer.music.get_volume()
    mixer.music.set_volume(curr_volume + vol_change)
    v_label.configure(text=f"{int(mixer.music.get_volume()*100)}%")

#
# base button functions
#

def pause_btn_fnc(pl_btn, pz_btn):
    pl_btn.configure(bg="black", fg="light green")
    pz_btn.configure(bg="light green", fg="black")
    mixer.music.pause()

def play_btn_fnc(pl_btn, pz_btn):
    pl_btn.configure(bg="light green", fg="black")
    pz_btn.configure(bg="black", fg="light green")
    mixer.music.unpause()

def next_btn_fnc():
    global c_track
    global tracklist
    if c_track < len(tracklist) - 1:
        c_track += 1
        play_track(tracklist[c_track])

def prev_btn_fnc():
    global c_track
    global tracklist
    if c_track > 0:
        c_track -= 1
        play_track(tracklist[c_track])

#
# play settings buttons
#

def rand_btn_fnc(r_btn):
    global random_set
    if random_set is False:
        random_set = True
        r_btn.configure(bg="light green", fg="black")
    else:
        random_set = False
        r_btn.configure(bg="black", fg="light green")

def loop_btn_fnc(l_btn):
    global loop_set
    if loop_set is False:
        loop_set = True
        l_btn.configure(bg="light green", fg="black")
    else:
        loop_set = False
        l_btn.configure(bg="black", fg="light green")

#
# open button
#

def open_btn_fnc(pl_btn):
    global tracklist
    global c_track
    tracklist = list(fdg.askopenfilenames())
    pl_btn.configure(bg="light green", fg="black")
    if random_set is False:
        c_track = 0
        play_track(tracklist[0])
    else:
        r_track = random.randint(0,len(tracklist))
        c_track = r_track
        play_track(tracklist[r_track])

#
# playing the track
#

def play_track(track):
    mixer.music.load(track)
    mixer.music.play()

#
# to be added: automated playlist
#

def music_timer():
    global c_track
    global tracklist




