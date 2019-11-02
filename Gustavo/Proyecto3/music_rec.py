from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import tkinter

class Music:
    def __init__(self, gender, artist, name, popularity, acousticness,
                 danceability, duration, energy, instrumentalness, liveness,
                 loudness, mode, speechiness, tempo, time_signature, valence):
        self.gender = gender
        self.artist = artist
        self.name = name
        self.popularity = popularity
        self.acousticness = acousticness
        self.danceability = danceability
        self.duration = duration
        self.energy = energy
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.tempo = tempo
        self.time_signature = time_signature
        self.valence = valence

'''this reads the file with data, first only gives us the genders
TODO: create objects of music_files and append to its gender, it will make it
easier to browse'''
def openCSV():
    genders = []
    f = open("SpotifyFeatures.csv", "r", encoding='utf-8-sig')
    for line in f:
        s = line.split(',')
        gen = s[0]
        if gen in genders:
            continue
        else:
            genders.append(gen)
    genders.sort()
    return genders

def readAgain(like):
    songs = {}
    f = open("SpotifyFeatures.csv", "r", encoding='utf-8-sig')
    for line in f:
        s = line.split(',')
        gen = s[0]
        if gen not in like:
            continue
        else:
            songs[s[2]] = s
    # print(songs)
    return songs

'''this display all the checkbuttons with the label of the gender.'''
def choose():
    for gen in genders:
        intvar_gen[gen] = tkinter.IntVar()
        c = tkinter.Checkbutton(window, text=gen, variable=intvar_gen[gen])
        c.pack()
        checkbut_list.append(c)
    
'''this add to the likeable_gen the genders the user likes, then, it deletes all
the checkbuttons.'''
def submit():
    likeable = []
    if len(intvar_gen) == 0:
        messagebox.showinfo("Error", "You need to choose a gender")
    for key, value in intvar_gen.items():
        if value.get() > 0:
            likeable_gen.append(key)
            print('selected: ', key)
    intvar_gen.clear()
    for cb in checkbut_list: # This cleans the checkbuttons after submit
        cb.destroy()
    checkbut_list.clear()
    songs = readAgain(likeable_gen)
    gens = tkinter.Toplevel(window)
    pickSongs(songs, gens)

def pickSongs(songs, gens):
    new_songs = []
    for x in songs:
        new_songs.append(x)
    fav_songs = []
    combo1 = Combobox(gens, state="readonly")
    combo1['values']=new_songs
    combo1.current(1)
    combo1.pack()
    combo2 = Combobox(gens)
    combo2['values']=new_songs
    combo2.current(1)
    combo2.pack()
    combo3 = Combobox(gens)
    combo3['values']=new_songs
    combo3.current(1)
    combo3.pack()
    combo4 = Combobox(gens)
    combo4['values']=new_songs
    combo4.current(1)
    combo4.pack()
    combo5 = Combobox(gens)
    combo5['values']=new_songs
    combo5.current(1)
    combo5.pack()
    accept = tkinter.Button(gens, text="Submit Songs")
    accept.pack()

window = tkinter.Tk() # create window
window.title("Music recommender")
window.geometry('350x625')

intvar_gen = {}
checkbut_list = []
genders = openCSV() # all genders
likeable_gen = [] # likeable genders

lbl = tkinter.Label(window, text="Select music")
lbl.pack()

btn1 = tkinter.Button(window, text="Select Genders", command=choose) # open csv or something
btn1.pack()

btn2 = tkinter.Button(window, text="Submit Genders", command=submit)
btn2.pack()

window.mainloop() # display

# print(genders) # print all the genders in our data

