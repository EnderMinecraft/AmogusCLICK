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
root.geometry('400x450')
root.title("Main menu")
root.resizable(False, False)
root.iconbitmap('icon.ico')
#bglabelset
bg = PhotoImage(file = "skin1.gif")
label1 = Label(root, image = bg)
label1.place(x = 0,y = -1)
label2= Label(root, image = bg)
label2.place(x = 0,y = 240)
l = Label(root, text = "Gamemode is EASY", bg="indigo", fg='#FFFFFF')
l.pack()
#varset
speed=2
boost=0
skin=1
music=0
Auto=0
Trail=0
#bgfunc
def bgfg():
    global bg
    global label1
    global label2
    label1.destroy()
    label2.destroy()
    if skin==1:
        bg = PhotoImage(file = "skin1.gif")
    elif skin==2:
        bg = PhotoImage(file = "skin2.gif")
    elif skin==3:
        bg = PhotoImage(file = "skin3.gif")
    elif skin==4:
        bg = PhotoImage(file = "skin4.gif")
    elif skin==5:
        bg = PhotoImage(file = "egg.gif")
    elif skin==6:
        bg = PhotoImage(file = "gegg.gif")
    elif skin==10:
        bg = PhotoImage(file = "mono.gif")
        music=1
    elif skin==11:
        bg = PhotoImage(file = "ronaldo.gif")
        music=3
    elif skin==12:
        bg = PhotoImage(file = "chad.gif")
    elif skin==127:
        bg = PhotoImage(file = "skin50.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    btt()
#skinfunc
def skin1():
    global skin
    skin=1
    bgfg()
    btt()
def skin2():
    global skin
    skin=2
    bgfg()
    btt()
def skin3():
    global skin
    skin=3
    bgfg()
    btt()
def skin4():
    global skin
    skin=4
    bgfg()
    btt()
def egg():
    global skin
    skin=5
    bgfg()
    btt()
def gegg():
    global skin
    skin=6
    bgfg()
    btt()
def skinhax():
    global skin
    skin=127
    bgfg()
    btt()
def mono():
    global skin
    skin=10
    bgfg()
    btt()
def ronaldo():
    global skin
    skin=11
    bgfg()
    btt()
def chad():
    global skin
    skin=12
    bgfg()
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
        l = Label(root, text = "Gamemode is EASY", bg="indigo", fg='#FFFFFF')
        l.pack()
def norm():
        global speed
        speed=5
        global l
        l.destroy()
        l = Label(root, text = "Gamemode is NORMAL", bg="indigo", fg='#FFFFFF')
        l.pack()
def hard():
        global speed
        speed=10
        global l
        l.destroy()
        l = Label(root, text = "Gamemode is HARD", bg="indigo", fg='#FFFFFF')
        l.pack()

#musicfunc
def md():
    global music
    music=0
def mm():
    global music
    music=1
def mr():
    global music
    music=2
def mro():
    global music
    music=3

#inzsetupbutton
def btt():
    button = ttk.Button(root, text="Myth", command=myth)
    button.place(x=320, y=400)
    button = ttk.Button(root, text="Easy", command=ez)
    button.place(x=80, y=60)
    button = ttk.Button(root, text="Normal", command=norm)
    button.place(x=160, y=60)
    button = ttk.Button(root, text="Hard", command=hard)
    button.place(x=240, y=60)
    button = ttk.Button(root, text="START", command=root.destroy)
    button.place(x=160, y=150)
btt()

#setupmenubar
menubar = Menu(root)
diffmenu = Menu(menubar, tearoff=0)
diffmenu.add_radiobutton(label="Easy", command=ez)
diffmenu.add_radiobutton(label="Normal", command=norm)
diffmenu.add_radiobutton(label="Hard", command=hard)
menubar.add_cascade(label="Difficulty", menu=diffmenu)

skinmenu = Menu(menubar, tearoff=0)
skinmenu.add_radiobutton(label="Pmogus(Default)", command=skin1)
skinmenu.add_radiobutton(label="Pimogus", command=skin2)
skinmenu.add_radiobutton(label="Bmogus", command=skin3)
skinmenu.add_radiobutton(label="RMOGUS", command=skin4)
skinmenu.add_radiobutton(label="Egg", command=egg)
skinmenu.add_radiobutton(label="Golden Egg", command=gegg)
skinmenu.add_radiobutton(label="MONO", command=mono)
skinmenu.add_radiobutton(label="Ronaldo", command=ronaldo)
skinmenu.add_radiobutton(label="GigaChad", command=chad)
menubar.add_cascade(label="Skin", menu=skinmenu)

musicmenu = Menu(menubar, tearoff=0)
musicmenu.add_radiobutton(label="CTAC(Default)", command=md)
musicmenu.add_radiobutton(label="Rick", command=mr)
musicmenu.add_radiobutton(label="MONO", command=mm)
musicmenu.add_radiobutton(label="Ronaldo", command=mro)
menubar.add_cascade(label="Music", menu=musicmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=helpme)
helpmenu.add_command(label="DO NOT CLICK", command=rig)
helpmenu.add_command(label="Myth", command=myth)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

#p2wset
crr = "adb"
passwordvar = tk.StringVar()
def test():
    chk = passwordvar.get()
    if chk == crr:
        skinhax()
        tkinter.messagebox.showinfo("Correct","Got it man!")
    else:
        tkinter.messagebox.showinfo("Invalid","Try to crack? Not that easy")
def box():
    global passwordvar
    rootbox = tkinter.Toplevel()
    rootbox.title("Enter Activate code")
    rootbox.geometry('400x100')
    signin = ttk.Frame(rootbox)
    signin.pack(padx=5, pady=5, fill='x', expand=False)
    password_label = ttk.Label(signin, text="Enable Code:")
    password_label.pack(fill='x', expand=True)
    password_entry = ttk.Entry(signin, textvariable = passwordvar, show="*")
    passwordvar = tk.StringVar()
    password_entry.pack(fill='x', expand=True)
    login_button = ttk.Button(signin, text="Check", command=test)
    login_button.pack(fill='x', expand=True, pady=10)
#devwindow
ldb = Label()
lds = Label()
ldt = Label()
lda = Label()
lcr = Label()
hax = 0
def hece():
    global ld
    global hax
    hax = tkinter.Toplevel(None)
    hax.title("Dev Menu")
    hax.geometry('600x450')
    hax.resizable(False, False)
    Dev = Menu(hax)
    hax.config(menu=Dev)
    hskin = Menu(Dev, tearoff=0)
    hskin.add_radiobutton(label="Skin1", command=skinsc1)
    hskin.add_radiobutton(label="Skin2", command=skinsc2)
    hskin.add_radiobutton(label="Skin3", command=skinsc3)
    Dev.add_cascade(label="Secret Skin", menu=hskin, underline=0)
    ldb = Label(hax, text = "Boost:Off", bg="indigo", fg='#FFFFFF')
    ldb.place(x=160, y=0)
    lds = Label(hax, text = speed, bg="indigo", fg='#FFFFFF')
    lds.place(x=160, y=30)
    ldt = Label(hax, text = "Trail:Off", bg="indigo", fg='#FFFFFF')
    ldt.place(x=160, y=60)
    lda = Label(hax, text = "Auto:Off", bg="indigo", fg='#FFFFFF')
    lda.place(x=160, y=90)
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
    button = ttk.Button(hax, text="Enable Auto", command=Auto)
    button.place(x=0, y=90)
    button = ttk.Button(hax, text="Disable Auto", command=Nauto)
    button.place(x=80, y=90)
    button = ttk.Button(hax, text="crr", command=crack)
    button.place(x=0, y=420)
#devfunc
def boost():
    global boost
    global ldb
    if(boost==1):
        ldb.destroy()
        ldb = Label(hax, text = "Boost:On", bg="indigo", fg='#FFFFFF')
        ldb.place(x=160, y=0)
    elif(boost==0):
        boost=1
        ldb.destroy()
        ldb = Label(hax, text = "Boost:On", bg="indigo", fg='#FFFFFF')
        ldb.place(x=160, y=0)
    else:
        boost=1
def noboost():
    global boost
    global ldb
    if(boost==0):
        ldb.destroy()
        ldb = Label(hax, text = "Boost:Off", bg="indigo", fg='#FFFFFF')
        ldb.place(x=160, y=0)
    elif(boost==1):
        boost=0
        ldb.destroy()
        ldb = Label(hax, text = "Boost:Off", bg="indigo", fg='#FFFFFF')
        ldb.place(x=160, y=0)
    else:
        boost=0
def Trail():
    global Trail
    global ldt
    if(Trail==1):
        ldt.destroy()
        ldt = Label(hax, text = "Trail:On", bg="indigo", fg='#FFFFFF')
        ldt.place(x=160, y=60)
    elif(Trail==0):
        Trail=1
        ldt.destroy()
        ldt = Label(hax, text = "Trail:On", bg="indigo", fg='#FFFFFF')
        ldt.place(x=160, y=60)
    else:
        Trail=1
def Notrail():
    global Trail
    global ldt
    if(Trail==0):
        ldt.destroy()
        ldt = Label(hax, text = "Trail:Off", bg="indigo", fg='#FFFFFF')
        ldt.place(x=160, y=60)
    elif(Trail==1):
        Trail=0
        ldt.destroy()
        ldt = Label(hax, text = "Trail:Off", bg="indigo", fg='#FFFFFF')
        ldt.place(x=160, y=60)
    else:
        Trail=0
def pspeed():
    global speed
    global lds
    speed=speed+1
    if(speed<10):
        lds.destroy()
        lds = Label(hax, text = speed, bg="indigo", fg='#FFFFFF')
        lds.place(x=160, y=30)
    elif (speed>=11):
        lds.destroy()
        lds = Label(hax, text = "Cant higher", bg="indigo", fg='#FFFFFF')
        lds.place(x=160, y=30)
        speed=0
def nspeed():
    global speed
    global lds
    speed=speed-1
    if(speed>0):
        lds.destroy()
        lds = Label(hax, text = speed, bg="indigo", fg='#FFFFFF')
        lds.place(x=160, y=30)
    elif (speed<=0):
        lds.destroy()
        lds = Label(hax, text = "Cant lower", bg="indigo", fg='#FFFFFF')
        lds.place(x=160, y=30)
        speed=1
def Auto():
    global Auto
    global lda
    if(Auto==1):
        lda.destroy()
        lda = Label(hax, text = "Auto:On", bg="indigo", fg='#FFFFFF')
        lda.place(x=160, y=90)
    elif(Trail==0):
        Auto=1
        lda.destroy()
        lda = Label(hax, text = "Auto:On", bg="indigo", fg='#FFFFFF')
        lda.place(x=160, y=90)
    else:
        Auto=1
def Nauto():
    global Auto
    global lda
    if(Auto==0):
        lda.destroy()
        lda = Label(hax, text = "Auto:Off", bg="indigo", fg='#FFFFFF')
        lda.place(x=160, y=90)
    elif(Auto==1):
        Auto=0
        lda.destroy()
        lda = Label(hax, text = "Auto:Off", bg="indigo", fg='#FFFFFF')
        lda.place(x=160, y=90)
    else:
        Auto=0
def crack():
        global passwordvar
        global lcr
        passwordvar.set('adb')
        lcr.destroy()
        lcr = Label(hax, text = "Cracked", bg="indigo", fg='#FFFFFF')
        lcr.place(x=80, y=420)

#devmenu
HAXmenu = Menu(menubar, tearoff=0)
HAXmenu.add_command(label="HAX", command=box)
HAXmenu.add_command(label="MENU", command=lambda: hece())
menubar.add_cascade(label="HAX", menu=HAXmenu)
root.config(menu=menubar)
root.mainloop()

#screen
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
turtle.register_shape('ronaldo.gif')
turtle.register_shape('chad.gif')
wn.setup(1000,700)
if(music==0):
    winsound.PlaySound("main.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==1):
    winsound.PlaySound("mono.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==2):
    winsound.PlaySound("rick.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==3):
    winsound.PlaySound("rol.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
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
    img = tkinter.Image("photo", file = "skin1.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==2):
    turtle.shape("skin2.gif")
    img = tkinter.Image("photo", file = "skin2.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==3):
    turtle.shape("skin3.gif")
    img = tkinter.Image("photo", file = "skin3.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==4):
    turtle.shape("skin4.gif")
    img = tkinter.Image("photo", file = "skin4.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==5):
    turtle.shape("egg.gif")
    img = tkinter.Image("photo", file = "egg.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==6):
    turtle.shape("gegg.gif")
    img = tkinter.Image("photo", file = "gegg.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==7):
    turtle.shape("rick.gif")
    img = tkinter.Image("photo", file = "rick.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==8):
    turtle.shape("gegg.gif")
elif (skin==9):
    turtle.shape("gegg.gif")
elif (skin==127):
    turtle.shape("skin50.gif")
    img = tkinter.Image("photo", file = "skin50.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==10):
    turtle.shape("mono.gif")
    img = tkinter.Image("photo", file = "mono.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==11):
    turtle.shape("ronaldo.gif")
    img = tkinter.Image("photo", file = "ronaldo.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==12):
    turtle.shape("chad.gif")
    img = tkinter.Image("photo", file = "chad.gif")
    turtle._Screen._root.iconphoto(True, img)
turtle.shapesize(50,50)
turtle.penup()
if(Trail==1):
    turtle.color('red')
    turtle.pendown()
elif(Trail==0):
    turtle.penup()
turtle.speed(speed)

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
                    n=n*7
                elif (boost==1):
                    n=n*o
                else:
                    n=n+o
                turtle.title(n)
        x = turtle.xcor()
        y = turtle.ycor()
        xm = x+xin+4
        ym = y+yin+2
        turtle.setposition(xm, ym)
        if (ym>=350 or ym<=-350, xm>=800 or xm<=-800):
            xin=xin*-0.4
        if (xm>=800 or xm<=-800, ym>=350 or ym<=-350):
            yin=yin*-0.6
        if (Auto==1):
            turtle.onclick(fxn(xin,yin))
        else:
            turtle.onclick(fxn)
        def reset():
            turtle.speed(0)
            turtle.setposition(0,0)
            turtle.speed(speed)
        wn.onkey(reset, "r")
        wn.listen()
