from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import tkinter

class Music:
    def __init__(self, gender, artist, name, ide, popularity, acousticness,
                 danceability, duration, energy, instrumentalness, key,
                 liveness, loudness, mode, speechiness, tempo, time_signature,
                 valence):
        self.gender = gender
        self.artist = artist
        self.name = name
        self.ide = ide
        self.popularity = popularity
        self.acousticness = acousticness
        self.danceability = danceability
        self.duration = duration
        self.energy = energy
        self.instrumentalness = instrumentalness
        self.key = key
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

'''Im so stupid, so we need to read the file, the advantage is that now we can
choose the lines we need. We take a list of genders the user like, and display
another window, so he/she can choose a song they like.'''
def readAgain(like):
    songs = {}
    f = open("SpotifyFeatures.csv", "r", encoding='utf-8-sig')
    for line in f:
        s = line.split(',')
        gen = s[0]
        if gen not in like:
            continue
        else:
            if len(s) > 18: # we have songs like "word word, word"
                continue
            else:
                songs[s[2]] = s
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
    global songs_dic
    songs_dic = readAgain(likeable_gen) # all the songs of the liked genders
    for x in songs_dic:
        all_songs.append(x)
    all_songs.sort()
    pickSongs()

'''This creates a new window with comboboxes with all the songs of the genders 
the user likes.
TODO: make an accept button, so we can save the songs they prefer.'''
def pickSongs():
    combo1['values']=all_songs
    combo1.current(1)
    combo1.pack()
    combo2['values']=all_songs
    combo2.current(1)
    combo2.pack()
    combo3['values']=all_songs
    combo3.current(1)
    combo3.pack()
    combo4['values']=all_songs
    combo4.current(1)
    combo4.pack()
    combo5['values']=all_songs
    combo5.current(1)
    combo5.pack()
    accept = tkinter.Button(window, text="Submit Songs", command=score)
    accept.pack()

def score():
    # print(songs_dic)
    s1 = combo1.get()
    s2 = combo2.get()
    s3 = combo3.get()
    s4 = combo4.get()
    s5 = combo5.get()
    fav_songs.append(s1)
    fav_songs.append(s2)
    fav_songs.append(s3)
    fav_songs.append(s4)
    fav_songs.append(s5)
    prom_acu = (float(songs_dic[s1][5])+float(songs_dic[s2][5])+float(songs_dic[s3][5])+float(songs_dic[s4][5])+float(songs_dic[s5][5]))/5
    prom_dan = (float(songs_dic[s1][6])+float(songs_dic[s2][6])+float(songs_dic[s3][6])+float(songs_dic[s4][6])+float(songs_dic[s5][6]))/5
    prom_ene = (float(songs_dic[s1][8])+float(songs_dic[s2][8])+float(songs_dic[s3][8])+float(songs_dic[s4][8])+float(songs_dic[s5][8]))/5
    prom_ins = (float(songs_dic[s1][9])+float(songs_dic[s2][9])+float(songs_dic[s3][9])+float(songs_dic[s4][9])+float(songs_dic[s5][9]))/5
    prom_liv = (float(songs_dic[s1][11])+float(songs_dic[s2][11])+float(songs_dic[s3][11])+float(songs_dic[s4][11])+float(songs_dic[s5][11]))/5
    prom_lou = (float(songs_dic[s1][12])+float(songs_dic[s2][12])+float(songs_dic[s3][12])+float(songs_dic[s4][12])+float(songs_dic[s5][12]))/5
    prom_spe = (float(songs_dic[s1][14])+float(songs_dic[s2][14])+float(songs_dic[s3][14])+float(songs_dic[s4][14])+float(songs_dic[s5][14]))/5
    prom_tem = (float(songs_dic[s1][15])+float(songs_dic[s2][15])+float(songs_dic[s3][15])+float(songs_dic[s4][15])+float(songs_dic[s5][15]))/5
    prom_val = (float(songs_dic[s1][17])+float(songs_dic[s2][17])+float(songs_dic[s3][17])+float(songs_dic[s4][17])+float(songs_dic[s5][17]))/5
    print(prom_acu) # 0
    print(prom_dan) # 1
    print(prom_ene) # 2
    print(prom_ins) # 3
    print(prom_liv) # 4
    print(prom_lou) # 5
    print(prom_spe) # 6
    print(prom_tem) # 7
    print(prom_val) # 8
    values = [prom_acu, prom_dan, prom_ene, prom_ins, prom_liv, prom_lou,
              prom_spe, prom_tem, prom_val]
    print(values)
    look4Songs(values)
    # print(fav_songs)

def look4Songs(values):
    p_acu = values[0] # the values we need
    p_dan = values[1]
    p_ene = values[2]
    p_ins = values[3]
    p_liv = values[4]
    p_lou = values[5]
    p_spe = values[6]
    p_tem = values[7]
    p_val = values[8]
    maybe = []
    for x in all_songs:
        acu = float(songs_dic[x][5]) # the values to compare
        dan = float(songs_dic[x][6])
        ene = float(songs_dic[x][8])
        ins = float(songs_dic[x][9])
        liv = float(songs_dic[x][11])
        lou = float(songs_dic[x][12])
        spe = float(songs_dic[x][14])
        tem = float(songs_dic[x][15])
        val = float(songs_dic[x][17])
        t_acu = (p_acu-acu)
        t_dan = (p_dan-dan)
        t_ene = (p_ene-ene)
        t_ins = (p_ins-ins)
        t_liv = (p_liv-liv)
        t_lou = (p_lou-lou)
        t_spe = (p_spe-spe)
        t_tem = (p_tem-tem)
        t_val = (p_val-val)
        tot = t_acu+t_dan+t_ene+t_ins+t_liv+t_lou+t_spe+t_tem+t_val
        z = (abs(tot), x)
        maybe.append(z)
        maybe.sort()
    songs_recommended = tkinter.Toplevel(window)
    for i in range(5):
        pair = maybe[i]
        print(maybe[i])
        song = pair[1]
        artist = songs_dic[song][1]
        print(artist)
        song_data = song + "  FROM  " + artist
        # print(song_data)
        lbl = tkinter.Label(songs_recommended, text=song_data)
        lbl.pack()
        # print(maybe[i])
    # print("HELOOOO")
    

window = tkinter.Tk() # create window
window.title("Music recommender")
window.geometry('350x625')

intvar_gen = {}
checkbut_list = []
genders = openCSV() # all genders
likeable_gen = [] # likeable genders
all_songs = [] # all the songs we have with a specific gender
fav_songs = [] # the FAV songs
songs_dic = {}

lbl = tkinter.Label(window, text="Select music")
lbl.pack()

btn1 = tkinter.Button(window, text="Select Genders", command=choose) # open csv or something
btn1.pack()

btn2 = tkinter.Button(window, text="Submit Genders", command=submit)
btn2.pack()

combo1 = Combobox(window, state="readonly")
combo2 = Combobox(window, state="readonly")
combo3 = Combobox(window, state="readonly")
combo4 = Combobox(window, state="readonly")
combo5 = Combobox(window, state="readonly")

window.mainloop() # display

# print(genders) # print all the genders in our data
