#import
import turtle, random, winsound, webbrowser, sys, base64, string, gc, json, ctypes, os
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
console_toggle = 0
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)
if os.path.isfile(os.path.join(application_path, "savefile.json")):
    pass
elif not os.path.isfile(os.path.join(application_path, "savefile.json")):
    with open("savefile.json", 'w+') as file:
        file.write('{"highscore":0}')
        file.close()
else:
    pass
loaded=0
#tk
root = tkinter.Tk()
root.geometry('400x450')
root.title("Main menu")
root.resizable(False, False)
root.iconbitmap('icon.ico')
def on_exit():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
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
boostvar=tk.IntVar()
skin=1
music=0
Autovar=tk.IntVar()
Trailvar=tk.IntVar()
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
def rndskn():
    global skin
    skin=random.randint(1,16)
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
def read():
    global data
    with open("savefile.json", "r") as infile:
        global data
        try:
            global data
            data = json.load(infile)
        except:
            tkinter.messagebox.showinfo("Savefile error", "Invalid savefile detected")
            with open("savefile.json", 'w+') as file:
                file.write('{"highscore":0}')
                file.close()
    infile.close()
def resetsavefile():
    resetsvf = {
                "highscore": 0,
            }
    with open("savefile.json", "w") as outfile:
                json.dump(resetsvf, outfile)
    read()
read()
def load():
    read()
    global loaded
    global data
    loaded = 1
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
skinmenu.add_radiobutton(label="Random", command=rndskn)
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

savemenu = Menu(menubar, tearoff=0)
savemenu.add_command(label="Load", command=load)
savemenu.add_command(label="Reset", command=resetsavefile)
menubar.add_cascade(label="Savefile", menu=savemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=helpme)
helpmenu.add_command(label="DO NOT CLICK", command=rig)
helpmenu.add_command(label="Myth", command=myth)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

#p2wset
txt = string.ascii_letters + string.digits
cod = ''.join(random.choice(txt) for i in range(16))
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
last_key = None
act="hax.bind('<KeyPress>', keypress_handler)"
hax = 0
def hece():
    global hax
    global music
    global speed
    global act
    hax = tkinter.Toplevel(None)
    hax.title("Settings")
    hax.geometry('250x200')
    hax.resizable(False, False)
    Dev = Menu(hax)
    hax.config(menu=Dev)
    hskin = Menu(Dev, tearoff=0)
    hskin.add_radiobutton(label="Skin1", command=skinsc1)
    hskin.add_radiobutton(label="Skin2", command=skinsc2)
    hskin.add_radiobutton(label="Skin3", command=skinsc3)
    Dev.add_cascade(label="Secret Skin", menu=hskin, underline=0)
    wspeed = ttk.Scale(hax, from_=0, to=10, orient=HORIZONTAL)
    wspeed.place(x=0, y=85)
    l = Label(hax, text = speed)
    l.place(x=200, y=85)
    def apply2():
        global console_toggle
        if console_toggle==1:
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
        else:
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        console_toggle = not console_toggle
    def apply():
        global speed
        speed = round(wspeed.get())
        l = Label(hax, text = speed)
        l.place(x=50, y=54)
    button = ttk.Button(hax, text="Apply speed", command=apply)
    button.place(x=110, y=85)
    button = ttk.Button(hax, text="Show console", command=apply2)
    button.place(x=100, y=0)
    boostchk = ttk.Checkbutton(hax, text='Boost',variable=boostvar, onvalue=1, offvalue=0)
    boostchk.place(x=0, y=40)
    boostchk = ttk.Checkbutton(hax, text='Trail',variable=Trailvar, onvalue=1, offvalue=0)
    boostchk.place(x=0, y=20)
    boostchk = ttk.Checkbutton(hax, text='Auto',variable=Autovar, onvalue=1, offvalue=0)
    boostchk.place(x=0, y=0)
    cmd_entry=ttk.Entry(hax,width=40)
    cmd_entry.place(x=0, y=133)
    #if there are more custom var,put it inside string below
    l = Label(hax, text = "Enter debug command below!")
    l.place(x=0, y=111)
    button3 = ttk.Button(hax, text="Run command!", command=lambda: exec("global bg, label1, label2, speed, boostvar, skin, music, Autovar, Trailvar, url, loaded, txt, cod, cod16, console_toggle, root, data\n"+cmd_entry.get()))
    button3.place(x=80, y=170)
    def keypress_handler(event):
        global last_key
        global act
        key_pressed = event.keysym
        if key_pressed == 'space':
            if last_key == 'Shift_L':
                global act
                hidden()
                act=1
        last_key = key_pressed
    exec(act)
#devmenu
HAXmenu = Menu(menubar, tearoff=0)
HAXmenu.add_command(label="somesecretskin:)", command=box)
HAXmenu.add_command(label="Settings", command=lambda: hece())
menubar.add_cascade(label="Extra", menu=HAXmenu)
root.config(menu=menubar)
root.mainloop()
#screen
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
gc.collect()
wn=turtle.Screen()
canvas = wn.getcanvas()
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
elif (boostvar.get()==1):
    n=200
    o=999
else:
    n=0
    o=1
if (loaded==1):
    n=n+int(data["highscore"])
else:
    pass
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
if(Trailvar.get()==1):
    turtle.color('red')
    turtle.pendown()
elif(Trailvar.get()==0):
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
            elif (boostvar.get()==1):
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
    if (Autovar.get()==1):
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
    def save():
            savefile = {
                "highscore": n,
            }
            with open("savefile.json", "w") as outfile:
                json.dump(savefile, outfile)
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
        skin.add_radiobutton(label="Cat", command=lambda:turtle.shape("cat.gif"))
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
        button.place(x=110, y=150)
        button = ttk.Button(pause, text="Save", command=save, style="save.TButton")
        button.place(x=110, y=100)
        style.configure('cn.TButton', font=(None, 20), foreground="skyblue")
        style.configure('rs.TButton', font=(None, 20), foreground="mediumaquamarine")
        style.configure('end.TButton', font=(None, 20), foreground="orangered")
        style.configure('save.TButton', font=(None, 20), foreground="orange")
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
