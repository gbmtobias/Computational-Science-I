from time import time
from Tkinter import *
from math import pi, sin, cos

def getColor(cv):
    
    if cv == 0:
        color = "black"
    elif cv < 0.1:
        color = "darkblue"
    elif cv < 0.2:
        color = "mediumblue"
    elif cv < 0.3:
        color = "cyan"
    elif cv < 0.4:
        color = "mediumspringgreen"
    elif cv < 0.5:
        color = "green"
    elif cv < 0.6:
        color = "yellowgreen"
    elif cv < 0.7:
        color = "yellow"
    elif cv < 0.8:
        color = "orange"
    elif cv < 0.9:
        color = "orangered"
    else:
        color = "red"
		
    return color

master = Tk()

mapWidth = 794
mapHeight = 397

backgroundImage = PhotoImage(file = "WorldMap794x397.gif")

w = Canvas(master, width=mapWidth, height=mapHeight)
w.create_image(0, 0, image = backgroundImage, anchor = NW)
w.pack()

t = int(time()) - 1332331200

delta = t/(3600 * 24 * 365.25) * 2 * pi
I = 23.4 * pi / 180

dayTime = 3.583333333333333/24*2*pi # 15:35 GMT

x = np.array([1, 0, 0])

for i in range(37) :
    
    latitude = i * 5 - 90
    l = latitude * pi / 180
    
    for j in range(73) :
        
        longitude = j * 5 - 180
        
        sigma = dayTime + longitude * pi / 180 + delta
        
        R1 = np.matrix( ((cos(l), 0, -sin(l)), (0, 1, 0), (sin(l), 0, cos(l))) )
        
        R2 = np.matrix( ((cos(sigma), sin(sigma), 0), (-sin(sigma), cos(sigma), 0), (0, 0, 1)) )
        
        R3 = np.matrix( ((1, 0, 0), (0, cos(I), sin(I)), (0, -sin(I), cos(I))) )
        
        R4 = np.matrix( ((cos(-delta), sin(-delta), 0), (-sin(-delta), cos(-delta), 0), (0, 0, 1)) )
        
        dayLight = x * R4 * R3 * R2 * R1
        
        xCord = (longitude+180) * 1.0 / 360 * mapWidth
        yCord = (latitude+90) * 1.0 / 180 * mapHeight
        
        w.create_oval(xCord-2, yCord-2, xCord+2, yCord+2, fill = getColor(max(dayLight.item(0), 0)))
        
mainloop()