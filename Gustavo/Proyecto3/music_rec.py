import tkinter
from tkinter import messagebox


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

def choose():
    print("Im in browse :D")
    # gens = tkinter.Toplevel(window)
    for gen in genders:
        intvar_gen[gen] = tkinter.IntVar()
        c = tkinter.Checkbutton(window, text=gen, variable=intvar_gen[gen])
        c.pack()
        checkbut_list.append(c)
    

def submit():
    print("Im in test")
    for key, value in intvar_gen.items():
        if value.get() > 0:
            print('selected: ', key)

window = tkinter.Tk() # create window
window.title("Music recommender")
window.geometry('350x625')

intvar_gen = {}
checkbut_list = []
genders = openCSV() # all genders

lbl = tkinter.Label(window, text="Select music")
lbl.pack()

btn1 = tkinter.Button(window, text="Select Genders", command=choose) # open csv or something
btn1.pack()

btn2 = tkinter.Button(window, text="Test Genders", command=submit)
btn2.pack()

window.mainloop() # display

print(genders) # print all the genders in our data

