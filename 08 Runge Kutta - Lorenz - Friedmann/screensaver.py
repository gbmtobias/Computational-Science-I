from Tkinter import *
from scipy.integrate import odeint
from numpy import arange

screen = Tk()
wd, ht = screen.winfo_screenwidth(), screen.winfo_screenheight()
screen.geometry("%dx%d+0+0"%(wd, ht))
screen.attributes("-fullscreen", 1)
canv = Canvas(screen, height = ht, width = wd, background = "black")
canv.pack()

# stretch factors and offsets
stretchX = 15;
stretchY = 15;
offsetX = 600;
offsetY = 370;

time = 0
timeStep = 0.04

def func(y, t):
    return [-rho*y[0]+rho*y[1], r*y[0]-y[1]-y[0]*y[2], y[1]*y[0]-b*y[2]]
    
rho = 10
r = 28
b = 8/3.

y0 = [20, 7, 27]
    
def frame(y0, time, timeStep):
    
    startOffset = 4
    
    t = arange(time, time + timeStep, timeStep/startOffset)
    y = odeint(func, y0, t)
    
    #canv.delete("all")   
    
    for i in range(len(y)-1):
        canv.create_line(offsetX + y[i][0]*stretchX, offsetY +y[i][1]*stretchY,
                         offsetX + y[i+1][0]*stretchX, offsetY + y[i+1][1]*stretchY, fill = "#FFD700" )
    
    screen.after(1, frame, y[startOffset-1], time+timeStep, timeStep)
    
screen.after(1, frame, y0, time, timeStep)

canv.update()

screen.mainloop()
