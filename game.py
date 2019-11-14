import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
from enum import Enum
import random

#CONSTANTS
WINDOW_TITLE = "Game of Life"
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300

GS_PAUSE = True
FILL_SEED_CHANCE = 0.05

window = tk.Tk()
#WINDOW STUFF
window.title(WINDOW_TITLE)
window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
window.configure(background='grey')
window.resizable = False

#CELL_UPDATE_ENUM
class CellUpdate(Enum):
    KEEP = 1
    KILL = 2
    NEW = 3

#DISPLAY CLASS
class Display:

    def __init__(self, load):
        self.point_list = []
        self.update_list = []
        if load == None:
            self.data = np.zeros((WINDOW_HEIGHT, WINDOW_WIDTH), dtype=np.uint8)
            for y in range(WINDOW_HEIGHT):
                for x in range(WINDOW_WIDTH):
                    if random.random() < FILL_SEED_CHANCE:
                        self.data[y][x] = 255
            self.image = Image.fromarray(self.data, "L")
        
        #append image to tk img and build display for user
        self.img = ImageTk.PhotoImage(self.image)
        self.panel = tk.Label(window, image=self.img)
        
        self.panel.bind("<Button-1>", self.click)
        
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")

    def click(self, event):
        print("clicked at", event.x, event.y)

    def tick(self):
        pass

display = Display(None)

while True:
    
    window.update_idletasks()
    window.update()