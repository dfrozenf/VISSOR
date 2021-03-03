from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()

with open(filename) as file:
    next(file)
    next(file)
    channels = file.readline()
    next(file)
    raw = file.readlines()
    for i in raw:
        i = [j.rstrip() for j in i]
        i = [i.split('\t') for i in i]