#import
import turtle, random, winsound, webbrowser, sys, base64, string, gc
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
exitvar=0
def on_exit():
    root.destroy()
    sys.exit()
root.protocol("WM_DELETE_WINDOW", on_exit)
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
    global music
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
        music=5
    elif skin==13:
        bg = PhotoImage(file = "chip.gif")
        music=4
    elif skin==14:
        bg = PhotoImage(file = "potato.gif")
    elif skin==15:
        bg = PhotoImage(file = "brick.gif")
        music=6
    elif skin==16:
        bg = PhotoImage(file = "cat.gif")
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
def chip():
    global skin
    skin=13
    bgfg()
    btt()
def potato():
    global skin
    skin=14
    bgfg()
    btt()
def brick():
    global skin
    skin=15
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
def cat():
    global skin
    skin=16
    bgfg()
    btt()
#miscFunc
def hidden():
    tkinter.messagebox.showinfo("hi", "hi")
def myth():
        tkinter.messagebox.showinfo("369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369",  "369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369" )
def about():
    tkinter.messagebox.showinfo("About","Made with fun by EnderMCDev")
def helpme():
    tkinter.messagebox.showinfo("Help","Choose Difficulty & Skin and press start. Your goal is reach as much point as possible by clicking the image")
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
def mch():
    global music
    music=4
def mad():
    global music
    music=5
def mbr():
    global music
    music=6
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
skinmenu.add_radiobutton(label="Chip", command=chip)
skinmenu.add_radiobutton(label="Potato", command=potato)
skinmenu.add_radiobutton(label="Brick", command=brick)
skinmenu.add_radiobutton(label="Cat", command=cat)
menubar.add_cascade(label="Skin", menu=skinmenu)

musicmenu = Menu(menubar, tearoff=0)
musicmenu.add_radiobutton(label="CTAC(Default)", command=md)
musicmenu.add_radiobutton(label="Rick", command=mr)
musicmenu.add_radiobutton(label="MONO", command=mm)
musicmenu.add_radiobutton(label="Ronaldo", command=mro)
musicmenu.add_radiobutton(label="Potato&Chips", command=mch)
musicmenu.add_radiobutton(label="Chad", command=mad)
musicmenu.add_radiobutton(label="Brick", command=mbr)
menubar.add_cascade(label="Music", menu=musicmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=helpme)
helpmenu.add_command(label="DO NOT CLICK", command=rig)
helpmenu.add_command(label="Myth", command=myth)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

#p2wset
txt = string.ascii_letters + string.digits
cod = ''.join(random.choice(txt) for i in range(16))
print(cod)
cod16 = base64.b16encode(cod.encode('utf-8'))
cod16 = cod16.decode("utf-8")
password_entry = Entry()
def test():
    global password_entry, value
    value = str(password_entry.get())
    if value == cod:
        skinhax()
        tkinter.messagebox.showinfo("Correct","Got it man!")
    elif value == "SHOW":
        tkinter.messagebox.showinfo("ACTCODE",cod)
    else:
        tkinter.messagebox.showinfo("Invalid","Try to crack? Not that easy")
def box():
    global password_entry
    rootbox = tkinter.Toplevel()
    rootbox.title("Enter Activate code")
    rootbox.geometry('400x150')
    rootbox.resizable(False, False)
    signin = ttk.Frame(rootbox)
    signin.pack(padx=5, pady=5, fill='x', expand=False)
    password_label = ttk.Label(signin, text="Enable Code:")
    password_label.pack(fill='x', expand=True)
    password_entry = ttk.Entry(signin, show="*")
    password_entry.pack(fill='x', expand=True)
    login_button = ttk.Button(signin, text="Check", command=test)
    login_button.pack(fill='x', expand=True, pady=10)
    reqb = ttk.Button(signin, text="Request Code", command=lambda:tk.messagebox.showinfo("RequestCode", cod16))
    reqb.pack(fill='x', expand=True, pady=10)
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

#devmenu
HAXmenu = Menu(menubar, tearoff=0)
HAXmenu.add_command(label="HAX", command=box)
HAXmenu.add_command(label="MENU", command=lambda: hece())
menubar.add_cascade(label="HAX", menu=HAXmenu)
root.config(menu=menubar)
root.mainloop()
#screen
gc.collect()
wn=turtle.Screen()
canvas = wn.getcanvas()  # or, equivalently: turtle.getcanvas()
rotwn = canvas.winfo_toplevel()
def on_close():
    global running
    running = 0
rotwn.protocol("WM_DELETE_WINDOW", on_close)
wn.title(0)
wn.bgcolor("black")
running = 1
paused = 0
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
turtle.register_shape('chip.gif')
turtle.register_shape('potato.gif')
turtle.register_shape('brick.gif')
turtle.register_shape('cat.gif')
wn.setup(1000,700)
if(music==0):
    winsound.PlaySound("main.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==1):
    winsound.PlaySound("mono.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==2):
    winsound.PlaySound("rick.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==3):
    winsound.PlaySound("rol.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==4):
    winsound.PlaySound("chip.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==5):
    winsound.PlaySound("chad.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==6):
    winsound.PlaySound("brick.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
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
elif (skin==13):
    turtle.shape("chip.gif")
    img = tkinter.Image("photo", file = "chip.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==14):
    turtle.shape("potato.gif")
    img = tkinter.Image("photo", file = "potato.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==15):
    turtle.shape("brick.gif")
    img = tkinter.Image("photo", file = "brick.gif")
    turtle._Screen._root.iconphoto(True, img)
elif (skin==16):
    turtle.shape("cat.gif")
    img = tkinter.Image("photo", file = "cat.gif")
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
xin=random.randint(-3, 7)
yin=random.randint(-2, 3)
while running == 1:
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
        wn.bye()
    def fxn(a, b):
        if (paused == 0):
            global n
            a=random.randint(-600,600)
            b=random.randint(-400,400)
            turtle.setposition(a, b)
            if(skin==127):
                n=n*7
            elif (boost==1):
                n=n*o
            else:
                n=n+o
            turtle.title(n)
        else:
            pass
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
        wn.bye()
    x = turtle.xcor()
    y = turtle.ycor()
    if (paused==0):
        xm = x+xin+4
        ym = y+yin+2
    else:
        pass
    if (running==0):
        turtle.bye()
        break
        wn.bye()
    if (paused==0):
        turtle.setposition(xm, ym)
    else:
        pass
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
        wn.bye()
    if (ym>=350 or ym<=-350, xm>=800 or xm<=-800):
        xin=xin*-0.4
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        break
        wn.bye()
    if (xm>=800 or xm<=-800, ym>=350 or ym<=-350):
        yin=yin*-0.6
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
        wn.bye()
    if (Auto==1):
        turtle.onclick(fxn(xin,yin))
    else:
        turtle.onclick(fxn)
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
        wn.bye()
    def reset():
        turtle.speed(0)
        turtle.setposition(0,0)
        turtle.speed(speed)
    def pause():
        global n
        global paused
        global running
        pause = tkinter.Toplevel()
        paused = 1
        def cl():
            global paused
            paused = 0
            pause.destroy()
        pause.protocol("WM_DELETE_WINDOW", cl)
        def center_window(width=400, height=200):
            screen_width = pause.winfo_screenwidth()
            screen_height = pause.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            pause.geometry('%dx%d+%d+%d' % (width, height, x, y))
        center_window(400,200)
        pause.title("                                                Paused")
        pause.resizable(False, False)
        menubar = Menu(pause)
        pause.config(menu=menubar)
        diff = Menu(menubar, tearoff=0)
        diff.add_radiobutton(label="Easy", command=lambda:turtle.speed(2))
        diff.add_radiobutton(label="Normal", command=lambda:turtle.speed(5))
        diff.add_radiobutton(label="Hard", command=lambda:turtle.speed(10))
        menubar.add_cascade(label="Difficulty", menu=diff)
        skin = Menu(menubar, tearoff=0)
        skin.add_radiobutton(label="Pmogus(Default)", command=lambda:turtle.shape("skin1.gif"))
        skin.add_radiobutton(label="Pimogus", command=lambda:turtle.shape("skin2.gif"))
        skin.add_radiobutton(label="Bmogus", command=lambda:turtle.shape("skin3.gif"))
        skin.add_radiobutton(label="RMOGUS", command=lambda:turtle.shape("skin4.gif"))
        skin.add_radiobutton(label="Egg", command=lambda:turtle.shape("egg.gif"))
        skin.add_radiobutton(label="Golden Egg", command=lambda:turtle.shape("gegg.gif"))
        skin.add_radiobutton(label="MONO", command=lambda:turtle.shape("mono.gif"))
        skin.add_radiobutton(label="Ronaldo", command=lambda:turtle.shape("ronaldo.gif"))
        skin.add_radiobutton(label="GigaChad", command=lambda:turtle.shape("chad.gif"))
        skin.add_radiobutton(label="Chip", command=lambda:turtle.shape("chip.gif"))
        skin.add_radiobutton(label="Potato", command=lambda:turtle.shape("potato.gif"))
        skin.add_radiobutton(label="Brick", command=lambda:turtle.shape("brick.gif"))
        skin.add_radiobutton(label="Brick", command=lambda:turtle.shape("cat.gif"))
        menubar.add_cascade(label="Skin", menu=skin)
        music = Menu(menubar, tearoff=0)
        music.add_radiobutton(label="CTAC(Default)", command=lambda:winsound.PlaySound('main.wav', winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="MONO", command=lambda:winsound.PlaySound('mono.wav', winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="Rick", command=lambda:winsound.PlaySound('rick.wav', winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="Ronaldo", command=lambda:winsound.PlaySound('rol.wav', winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="Potato&Chips", command=lambda:winsound.PlaySound('chip.wav', winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="Chad", command=lambda:winsound.PlaySound('chad.wav', winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="Brick", command=lambda:winsound.PlaySound('brick.wav', winsound.SND_ASYNC | winsound.SND_LOOP))
        menubar.add_cascade(label="Music", menu=music)
        def rpl():
            global n
            turtle.speed(0)
            turtle.setpos(0, 0)
            n=0
            wn.title(n)
            turtle.speed(speed)
        def end():
            global running
            running = 0
            cl()
        style = ttk.Style()
        button = ttk.Button(pause, text="Continue", command=cl, style="cn.TButton")
        button.place(x=110, y=0)
        button = ttk.Button(pause, text="Restart", command=rpl, style="rs.TButton")
        button.place(x=110, y=50)
        button = ttk.Button(pause, text="Exit", command=end, style="end.TButton")
        button.place(x=110, y=100)
        style.configure('cn.TButton', font=(None, 20), foreground="blue4")
        style.configure('rs.TButton', font=(None, 20), foreground="green4")
        style.configure('end.TButton', font=(None, 20), foreground="red4")
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
        wn.bye()
    if (paused == 0):
        wn.onkeypress(reset, "r")
        wn.onkeypress(pause, "Escape")
        wn.listen()
    else:
        pass
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
        wn.bye()
gc.collect()
