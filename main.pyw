#import
import turtle
import random
import winsound
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox

#tk
root = tkinter.Tk()
root.title("Main Menu")
root.geometry('400x450')
root.resizable(False, False)

#bglabelset
bg = PhotoImage(file = "skin1.gif")
label1 = Label(root, image = bg)
label1.place(x = 0,y = -1)
label2= Label(root, image = bg)
label2.place(x = 0,y = 240)
l = Label(root, text = "Gamemode is EASY", bg="grey")
l.config(font =("Calibri", 14))
l.pack()

#varset
speed=2
boost=0
skin=1
music=0

#skinfunc
def skin1():
    global skin
    global bg
    global label1
    global label2
    skin=1
    bg = PhotoImage(file = "skin1.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    btt()
def skin2():
    global skin
    global bg
    global label1
    global label2
    skin=2
    bg = PhotoImage(file = "skin2.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    btt()
def skin3():
    global skin
    global bg
    global label1
    global label2
    skin=3
    bg = PhotoImage(file = "skin3.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    btt()
def skin4():
    global skin
    global bg
    global label1
    global label2
    skin=4
    bg = PhotoImage(file = "skin4.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    btt()
def egg():
    global skin
    global bg
    global label1
    global label2
    skin=5
    bg = PhotoImage(file = "egg.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    btt()
def gegg():
    global skin
    global bg
    global label1
    global label2
    skin=6
    bg = PhotoImage(file = "gegg.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    btt()
def skinhax():
    global skin
    global bg
    global label1
    global label2
    skin=127
    bg = PhotoImage(file = "skin50.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    btt()
def mono():
    global skin
    global bg
    global label1
    global label2
    global music
    skin=10
    music=1
    bg = PhotoImage(file = "mono.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    btt()
def skinsc1():
        global skin
        global music
        skin=7
        music=2
def skinsc2():
        global skin
        skin=8
def skinsc3():
        global skin
        skin=9

#miscFunc
def hidden():
    tkinter.messagebox.showinfo("hi", "hi")
def myth():
     tkinter.messagebox.showinfo("369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369",  "369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369" )
def about():
    tkinter.messagebox.showinfo("About","Made with fun by EnderMCDev")
def helpme():
    tkinter.messagebox.showinfo("Help","Choose Mode&Skin and press start.Your goal is reach as much point as possible by clicking the image")
def start():
    root.quit()
url="https://youtu.be/dQw4w9WgXcQ"
def rig():
    webbrowser.open_new(url)

#difffunc
def ez():
        global speed
        speed=2
        global l
        l.destroy()
        l = Label(root, text = "Gamemode is EASY", bg="grey")
        l.config(font =("Calibri", 14))
        l.pack()
def norm():
        global speed
        speed=5
        global l
        l.destroy()
        l = Label(root, text = "Gamemode is NORMAL", bg="grey")
        l.config(font =("Calibri", 14))
        l.pack()
def hard():
        global speed
        speed=10
        global l
        l.destroy()
        l = Label(root, text = "Gamemode is HARD", bg="grey")
        l.config(font =("Calibri", 14))
        l.pack()

#inzbutton
def btt():
    button = ttk.Button(root, text="Myth", command=myth)
    button.place(x=320, y=420)
    button = ttk.Button(root, text="Easy", command=ez)
    button.place(x=85, y=60)
    button = ttk.Button(root, text="Normal", command=norm)
    button.place(x=160, y=60)
    button = ttk.Button(root, text="Hard", command=hard)
    button.place(x=235, y=60)
    button = ttk.Button(root, text="START", command=root.destroy)
    button.place(x=160, y=150)
btt()

#setupmenubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Easy", command=ez)
filemenu.add_command(label="Normal", command=norm)
filemenu.add_command(label="Hard", command=hard)
menubar.add_cascade(label="Difficulty", menu=filemenu)

skinmenu = Menu(menubar, tearoff=0)
skinmenu.add_command(label="Pmogus(Default)", command=skin1)
skinmenu.add_command(label="Pimogus", command=skin2)
skinmenu.add_command(label="Bmogus", command=skin3)
skinmenu.add_command(label="RMOGUS", command=skin4)
skinmenu.add_command(label="Egg", command=egg)
skinmenu.add_command(label="Golden Egg", command=gegg)
skinmenu.add_command(label="MONO", command=mono)
menubar.add_cascade(label="Skin", menu=skinmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=helpme)
helpmenu.add_command(label="DO NOT CLICK", command=rig)
helpmenu.add_command(label="Myth", command=myth)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

#p2wset
password = tk.StringVar()
true = 124
def test():
    if (tk.StringVar() == true):
        skinhax()
def s():
    signin = ttk.Frame(root)
    signin.pack(padx=5, pady=5, fill='x', expand=False)
    password_label = ttk.Label(signin, text="Enable Code:")
    password_label.pack(fill='x', expand=True)
    password_entry = ttk.Entry(signin, textvariable=password, show="*")
    password_entry.pack(fill='x', expand=True)
    login_button = ttk.Button(signin, text="Login", command=skinhax)
    login_button.pack(fill='x', expand=True, pady=10)

#devfunc
Trail=0
def boost():
    global boost
    if(boost==1):
        tkinter.messagebox.showinfo("Already Enabled","Already Enabled")
    elif(boost==0):
        boost=1
        tkinter.messagebox.showinfo("Enabled","Enabled")
    else:
        boost=1
def noboost():
    global boost
    if(boost==0):
        tkinter.messagebox.showinfo("Already Disabled","Already Disabled")
    elif(boost==1):
        boost=0
        tkinter.messagebox.showinfo("Disabled","Disabled")
    else:
        boost=0    
def Trail():
    global Trail
    if(Trail==1):
        tkinter.messagebox.showinfo("Already Enabled","Already Enabled")
    elif(Trail==0):
        Trail=1
        tkinter.messagebox.showinfo("Enabled","Enabled")
    else:
        Trail=1
def Notrail():
    global Trail
    if(Trail==0):
        tkinter.messagebox.showinfo("Already Disabled","Already Disabled")
    elif(Trail==1):
        Trail=0
        tkinter.messagebox.showinfo("Disabled","Disabled")
    else:
        Trail=0
def pspeed():
        global speed
        speed=speed+1
        if(speed<10):
            tkinter.messagebox.showinfo("Speed is",speed)
        elif (speed>=10):
            tkinter.messagebox.showinfo("Err","Cannot Larger")
            speed=10
def nspeed():
        global speed
        speed=speed-1
        if(speed>0):
            tkinter.messagebox.showinfo("Speed is",speed)
        elif (speed<=0):
            tkinter.messagebox.showinfo("Err","Cannot Smaller")
            speed=0

#devwindow
def New_Window():
    hax = tk.Toplevel()
    hax.title("Dev Menu")
    hax.geometry('600x450')
    hax.resizable(False, False)
    Dev = Menu(hax)
    hax.config(menu=Dev)
    hskin = Menu(Dev, tearoff=0)
    hskin.add_command(label="Skin1", command=skinsc1)
    hskin.add_command(label="Skin2", command=skinsc2)
    hskin.add_command(label="Skin3", command=skinsc3)
    Dev.add_cascade(label="Secret Skin", menu=hskin, underline=0)
    button = ttk.Button(hax, text="Boost", command=boost)
    button.place(x=80, y=0)
    button = ttk.Button(hax, text="Noboost", command=noboost)
    button.place(x=0, y=0)
    button = ttk.Button(hax, text="+1 Speed", command=pspeed)
    button.place(x=0, y=30)
    button = ttk.Button(hax, text="-1 Speed", command=nspeed)
    button.place(x=80, y=30)
    button = ttk.Button(hax, text="Trail", command=Trail)
    button.place(x=0, y=60)
    button = ttk.Button(hax, text="NoTrail", command=Notrail)
    button.place(x=80, y=60)

#devmenu
HAXmenu = Menu(menubar, tearoff=0)
HAXmenu.add_command(label="HAX", command=s)
HAXmenu.add_command(label="MENU", command=lambda: New_Window())
menubar.add_cascade(label="HAX", menu=HAXmenu)
root.config(menu=menubar)
root.mainloop()

#screen
turtle.TurtleScreen._RUNNING=True
wn=turtle.Screen()
wn.title(0)
wn.bgcolor("black")
turtle.register_shape('skin1.gif')
turtle.register_shape('skin2.gif')
turtle.register_shape('skin3.gif')
turtle.register_shape('skin4.gif')
turtle.register_shape('egg.gif')
turtle.register_shape('gegg.gif')
turtle.register_shape('mono.gif')
turtle.register_shape('skin50.gif')
turtle.register_shape('rick.gif')
wn.setup(1000,700)
if(music==0):
    winsound.PlaySound("main.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==1):
    winsound.PlaySound("mono.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==2):
    winsound.PlaySound("rick.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
if (skin==127):
    n=500000
    o=127
elif (boost==1):
    n=200
    o=999
else:
    n=0
    o=1
wn.title(n)
#asset
if (skin==1):
    turtle.shape("skin1.gif")
elif (skin==2):
    turtle.shape("skin2.gif")
elif (skin==3):
    turtle.shape("skin3.gif")
elif (skin==4):
    turtle.shape("skin4.gif")
elif (skin==5):
    turtle.shape("egg.gif")
elif (skin==6):
    turtle.shape("gegg.gif")
elif (skin==7):
    turtle.shape("rick.gif")
elif (skin==8):
    turtle.shape("gegg.gif")
elif (skin==9):
    turtle.shape("gegg.gif")
elif (skin==127):
    turtle.shape("skin50.gif")
elif (skin==10):
    turtle.shape("mono.gif")
turtle.shapesize(50,50)
turtle.penup()
if(Trail==1):
    turtle.color('red')
    turtle.pendown()
elif(Trail==0):
    turtle.penup()
turtle.speed(speed)
rnd1=random.randint(1,5)
rnd2=random.randint(2,9)
#boundnclk
xin=random.randint(0, 7)
yin=random.randint(0, 3)
while True:
        def fxn(a,b):
                global n
                a=random.randint(-300,10)
                b=random.randint(10,300)
                turtle.setposition(a,b)
                if(skin==127):
                    n=n*2
                elif (boost==1):
                    n=n*o
                else:
                    n=n+o
                turtle.title(n)
        x = turtle.xcor()
        y = turtle.ycor()
        xm = x+xin+rnd1
        ym = y+yin+rnd2
        turtle.setposition(xm, ym)
        if (xm==400 or xm==-400):
            xin=xin*-0.4
            rnd1=rnd1*-0.3
        if (ym==500 or ym==-500):
            yin=yin*-0.6
            rnd2=rnd2*-0.5
        turtle.onclick(fxn)
