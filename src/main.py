#import
import turtle, random, winsound, webbrowser, sys, base64, string, gc, json, ctypes, os, time,urllib, requests
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import *
import sv_ttk
import tkinter.messagebox
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
if os.path.isfile(os.path.join(application_path, "settings.json")):
    pass
elif not os.path.isfile(os.path.join(application_path, "settings.json")):
    with open("settings.json", 'w+') as file:
        file.write('{"lastskin":1, "lastmusic":0, "lastauto":0, "lastboost":0, "lasttrail":0, "lastcons":false, "lastspeed":5, "lastrgb":0, "lastbgcolor":[0, 0, 0], "lasttrailcolor":[255, 0, 0]}')
        file.close()
else:
    pass
def apply2():
    global console_toggle
    if console_toggle==1:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
    else:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    console_toggle = not console_toggle
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
style = ttk.Style()
style.theme_use('vista')
style.configure('TButton', background = '#131313', foreground = 'white')
style.map('TButton', background=[('active','#343434')])
#varset
n=0
o=1
trailed=0
speed=2
boostvar=tk.IntVar()
rgbvar=tk.IntVar()
skin=1
music=0
Autovar=tk.IntVar()
Trailvar=tk.IntVar()
loaded=0
console_toggle = 0
data=0
settings=0
current="1.15"
url="https://youtu.be/dQw4w9WgXcQ"
last_key = None
act="hax.bind('<KeyPress>', keypress_handler)"
hax = 0
colr = (255, 0, 0)
clbg = (0, 0, 0)
cl = tk.StringVar()
cl2 = tk.StringVar()
le=Label()
txt = string.ascii_letters + string.digits
cod = ''.join(random.choice(txt) for i in range(16))
cod16 = base64.b16encode(cod.encode('utf-8'))
cod16 = cod16.decode("utf-8")
password_entry = Entry()
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
    elif skin==17:
        bg = PhotoImage(file = "ronaldo2.gif")
    elif skin==127:
        bg = PhotoImage(file = "skin50.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    btt()
#loadsettings
def loadsettings():
    global settings
    with open("settings.json", "r") as settingsfile:
        global settings
        try:
            global settings, music, skin, Autovar, boostvar, Trailvar, console_toggle, speed, rgbvar, clbg, colr
            settings = json.load(settingsfile)
            music=settings["lastmusic"]
            skin=settings["lastskin"]
            Autovar=settings["lastauto"]
            boostvar=settings["lastboost"]
            Trailvar=settings["lasttrail"]
            console_toggle=settings["lastcons"]
            speed=settings["lastspeed"]
            rgbvar=settings["lastrgb"]
            clbg=settings["lastbgcolor"]
            colr=settings["lasttrailcolor"]
            apply2()
        except:
            tkinter.messagebox.showinfo("Config file error", "Invalid config file detected! Attempted to reset")
            with open("settings.json", 'w+') as rsettingfile:
                rsettingfile.write('{"lastskin":1, "lastmusic":0, "lastauto":0, "lastboost":0, "lasttrail":0, "lastcons":false, "lastspeed":5, "lastrgb":0, "lastbgcolor":[0, 0, 0], "lasttrailcolor":[255, 0, 0]}')
                rsettingfile.close()
def savesettings():
    global music, skin, Autovar, boostvar, Trailvar, console_toggle, speed, rgbvar, clbg, colr
    if str(type(Autovar)) == "<class 'tkinter.IntVar'>":
        settingssave = {
                    "lastskin": skin,
                    "lastmusic": music,
                    "lastauto": Autovar.get(),
                    "lastboost": boostvar.get(),
                    "lasttrail": Trailvar.get(),
                    "lastcons": console_toggle,
                    "lastspeed": speed,
                    "lastrgb": rgbvar.get(),
                    "lastbgcolor":clbg,
                    "lasttrailcolor":colr,
            }
    else:
        settingssave = {
                    "lastskin": skin,
                    "lastmusic": music,
                    "lastauto": Autovar,
                    "lastboost": boostvar,
                    "lasttrail": Trailvar,
                    "lastcons": console_toggle,
                    "lastspeed": speed,
                    "lastrgb": rgbvar,
                    "lastbgcolor":clbg,
                    "lasttrailcolor":colr,
            }
    with open("settings.json", 'w') as wsettingfile:
        json.dump(settingssave, wsettingfile)
def resetsettings():
    with open("settings.json", 'w+') as wsettingfile:
        wsettingfile.write('{"lastskin":1, "lastmusic":0, "lastauto":0, "lastboost":0, "lasttrail":0, "lastcons":false, "lastspeed":5, "lastrgb":0, "lastbgcolor":[0, 0, 0], "lasttrailcolor":[255, 0, 0]}')
        wsettingfile.close()
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
def ronaldo2():
    global skin
    skin=17
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
def ronaldo2():
    global skin
    skin=17
    bgfg()
    btt()
def rndskn():
    global skin
    skin=random.randint(1,17)
    bgfg()
    btt()
#corefeature
hostdata=""
def start():
    root.quit()
def updatecheck():
    global hostdata
    hosts = urllib.request.urlopen('https://enderminecraft.github.io/ver.txt')
    hostdata = hosts.read()
    if (str(hostdata.strip().decode('utf-8')) == current):
        tkinter.messagebox.showinfo(" ", "App is up to date!")
    elif (str(hostdata.strip().decode('utf-8')) != current):
        msg_box = tk.messagebox.askquestion("Update", "App is not up to date! App is on version " + current + " but lastest version is " + str(hostdata.strip().decode('utf-8')) + "!.Do you want to update?")
        if msg_box == 'yes':
            def upd():
                newVersion = requests.get("https://github.com/enderMinecraft/AmogusCLICK/releases/latest/download/Installer.exe")
                open("installer.exe", "wb").write(newVersion.content)
                qsn = msg_box = tk.messagebox.askquestion(" ", "Download complete! Would you want to install update right now?")
                if qsn == 'yes':
                    os.system("start .\installer.exe")
                    os.kill(os.getpid(), True)
                if qsn == 'no':
                    updthread.Terminate()
            updthread = threading.Thread(target=upd)
            updthread.start()
#optionalfeature
def hidden():
    tkinter.messagebox.showinfo("hi", "hi")
def myth():
        tkinter.messagebox.showinfo("369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369",  "369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369" )
def about():
    abt = tkinter.Toplevel(None)
    abt.title("About")
    abt.geometry('310x200')
    abt.resizable(False, False)
    i = Label(abt, text = "AmogusClick",font=("Segoe UI", 15))
    i.pack(expand=True)
    i = Label(abt, text = "Version " + current + "\n EnderMinecraft")
    i.pack(expand=True)
    i = Label(abt, text = "Website: \n https://github.com/EnderMinecraft/AmogusCLICK")
    i.pack(expand=True)
    button = ttk.Button(abt, text="Check for update", command=updatecheck)
    button.pack(side=BOTTOM)
def helpme():
    tkinter.messagebox.showinfo("Help","Choose Difficulty & Skin and press start. Your goal is reach as much point as possible by clicking the image")
def rig():
    webbrowser.open_new(url)
#filesave
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
    button.place(x=310, y=400)
    button = ttk.Button(root, text="Easy", command=ez)
    button.place(x=70, y=60)
    button = ttk.Button(root, text="Normal", command=norm)
    button.place(x=160, y=60)
    button = ttk.Button(root, text="Hard", command=hard)
    button.place(x=250, y=60)
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
skinmenu.add_radiobutton(label="Ronaldo2", command=ronaldo2)
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
savemenu.add_command(label="Load Progress", command=load)
savemenu.add_command(label="Reset Progress", command=resetsavefile)
savemenu.add_command(label="Load Settings", command=loadsettings)
savemenu.add_command(label="Save Settings", command=savesettings)
savemenu.add_command(label="Reset Settings", command=resetsettings)
menubar.add_cascade(label="Savefile", menu=savemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=helpme)
helpmenu.add_command(label="DO NOT CLICK", command=rig)
helpmenu.add_command(label="Myth", command=myth)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

#hiddenlock
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
#settingswindow
def callback1(box, arg):
    global colr
    global le
    arg = arg.get()
    if len(arg) != 7:
        le = Label(hax, text = "Invalid Hex value\n(e.g. #42e0f5)", fg="#ff1605", bd=1)
        le.place(x=90, y=50)
        le.after(1000, le.destroy)
        box.delete(0, tk.END)
    else:
       colr = h2rgb(arg)

def callback2(box, arg):
    global clbg
    global le
    arg = arg.get()
    if len(arg) != 7:
        le = Label(hax, text = "Invalid Hex value\n(e.g. #42e0f5)", fg="#ff1605", bd=1)
        le.place(x=90, y=50)
        le.after(1000, le.destroy)
        box.delete(0, END)
    else:
       clbg = h2rgb(arg)

def h2rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
def randomcl1(r, g ,b):
    global colr
    colr = (r, g ,b)
    hexcl1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    l1 = Label(hax, text = "     ", bd = 0, bg = hexcl1)
    l1.place(x=282, y=3)
    
def randomcl2(r, g ,b):
    global clbg
    clbg = (r, g, b)
    hexcl2 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    l1 = Label(hax, text = "     ", bd = 0, bg = hexcl2)
    l1.place(x=282, y=33)

def hece():
    global hax
    global music
    global speed
    global act
    hax = tkinter.Toplevel(None)
    hax.title("Settings")
    hax.geometry('310x200')
    hax.resizable(False, False)
    Dev = Menu(hax)
    hax.config(menu=Dev)
    hskin = Menu(Dev, tearoff=0)
    hskin.add_radiobutton(label="Skin1", command=skinsc1)
    hskin.add_radiobutton(label="Skin2", command=skinsc2)
    hskin.add_radiobutton(label="Skin3", command=skinsc3)
    Dev.add_cascade(label="Secret Skin", menu=hskin, underline=0)
    themes = Menu(Dev, tearoff=0)
    themes.add_radiobutton(label="Windows Default", command=style.theme_use('vista'))
    themes.add_radiobutton(label="Dark Theme", command=style.theme_use('alt'))
    themes.add_radiobutton(label="Clam", command=style.theme_use('clam'))
    themes.add_radiobutton(label="Classic Theme", command=style.theme_use('winnative'))
    themes.add_radiobutton(label="Default TTK", command=style.theme_use('default'))
    themes.add_radiobutton(label="XP native", command=style.theme_use('xpnative'))
    Dev.add_cascade(label="Themes", menu=themes, underline=0)
    l = Label(hax, text = speed, bd = 0)
    l.place(x=140, y=86)
    def apply():
        global speed
        speed = round(wspeed.get())
        l = Label(hax, text = speed)
        l.place(x=140, y=86)
    l = Label(hax, text = "Customize trail color:", bd=0)
    l.place(x=70, y=0)
    btn = tk.Button(hax, text=u'\u2705', command=lambda: callback1(color_entry, cl), borderwidth=0, fg="#05ff09", font=("Segoe UI Emoji", 10))
    btn.place(x=240, y=-1)
    btn = tk.Button(hax, text='\U0001F504', command=lambda: randomcl1(random.randint(0,255), random.randint(0,255), random.randint(0,255)), borderwidth=0, font=("Segoe UI Emoji", 10), fg="#0078D7")
    btn.place(x=260, y=-1)
    color_entry=ttk.Entry(hax, textvariable=cl, width=6)
    color_entry.place(x=190, y=0)

    l2 = Label(hax, text = "Customize BG color:", bd=0)
    l2.place(x=70, y=30)
    btn2 = tk.Button(hax, text='✅', command=lambda: callback2(bg_entry, cl2), borderwidth=0, fg="#05ff09", font=("Segoe UI Emoji", 10))
    btn2.place(x=240, y=30)
    btn = tk.Button(hax, text='\U0001F504', command=lambda: randomcl2(random.randint(0,255), random.randint(0,255), random.randint(0,255)), borderwidth=0, font=("Segoe UI Emoji", 10), fg="#0078D7")
    btn.place(x=260, y=30)
    bg_entry=ttk.Entry(hax, textvariable=cl2, width=6)
    bg_entry.place(x=190, y=30)
    
    separator = ttk.Separator(hax, orient='vertical')
    separator.place(relx=0.2, rely=0, relheight=0.4)
    button = tk.Button(hax, text="✅", command=apply, borderwidth=0, fg="#05ff09")
    button.place(x=110, y=85)
    button = ttk.Button(hax, text="Show console", command=apply2)
    button.place(x=220, y=170)
    button = ttk.Button(hax, text="Clear command", command=lambda: cmd_entry.delete(0, END))
    button.place(x=113, y=170)
    boostchk = ttk.Checkbutton(hax, text='Boost',variable=boostvar, onvalue=1, offvalue=0)
    boostchk.place(x=0, y=40)
    boostchk = ttk.Checkbutton(hax, text='Trail',variable=Trailvar, onvalue=1, offvalue=0)
    boostchk.place(x=0, y=20)
    boostchk = ttk.Checkbutton(hax, text='Auto',variable=Autovar, onvalue=1, offvalue=0)
    boostchk.place(x=0, y=0)
    boostchk = ttk.Checkbutton(hax, text='RGB',variable=rgbvar, onvalue=1, offvalue=0)
    boostchk.place(x=0, y=60)
    wspeed = ttk.Scale(hax, from_=0, to=10, orient=HORIZONTAL)
    wspeed.place(x=0, y=85)
    cmd_entry=ttk.Entry(hax,width=40)
    cmd_entry.place(x=0, y=133)
    #if there are more custom var,put it inside string below
    l = Label(hax, text = "Enter debug command below!", bd=0)
    l.place(x=0, y=111)
    button3 = ttk.Button(hax, text="Run command!", command=lambda: exec("global bg, label1, label2, speed, boostvar, skin, music, Autovar, Trailvar, url, loaded, txt, cod, cod16, console_toggle, root, data, rgbvar\n"+cmd_entry.get()))
    button3.place(x=5, y=170)
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
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
gc.collect()
wn=turtle.Screen()
wn.colormode(255)
canvas = wn.getcanvas()
rotwn = canvas.winfo_toplevel()
def on_close():
    global running
    running = 0
rotwn.protocol("WM_DELETE_WINDOW", on_close)
wn.title(0)
wn.bgcolor(clbg)
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
turtle.register_shape('ronaldo2.gif')
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
elif str(type(boostvar)) == "<class 'tkinter.IntVar'>":
    if (boostvar.get()==1):
        n=200
        o=999
    else:
        n=0
        o=1
elif str(type(boostvar)) == "<class 'int'>":
    if (boostvar==1):
        n=200
        o=999
    else:
        n=0
        o=1
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
elif (skin==17):
    turtle.shape("ronaldo2.gif")
    img = tkinter.Image("photo", file = "ronaldo2.gif")
    turtle._Screen._root.iconphoto(True, img)
turtle.penup()
if str(type(Trailvar)) == "<class 'tkinter.IntVar'>":
    if(Trailvar.get()==1):
        trailed=1
        turtle.color(colr)
        turtle.pendown()
    elif(Trailvar.get()==0):
        turtle.penup()
else:
    if(Trailvar==1):
        trailed=1
        turtle.color(colr)
        turtle.pendown()
    elif(Trailvar==0):
        turtle.penup()
if (str(type(rgbvar)) == "<class 'tkinter.IntVar'>" and trailed == 1):
    if (rgbvar.get()==1):
        turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    else:
        pass
elif (str(type(rgbvar)) == "<class 'int'>" and trailed == 1):
    if (rgbvar==1):
        turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
else:
    pass
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
            global o
            a=random.randint(-600,600)
            b=random.randint(-400,400)
            turtle.setposition(a, b)
            if(skin==127):
                n=n*7
            elif str(type(boostvar)) == "<class 'tkinter.IntVar'>":
                if (boostvar.get()==1):
                    n=n*o
                else:
                    turtle.title(n)
            elif str(type(boostvar)) == "<class 'int'>":
                if (boostvar==1):
                    n=n*o
                else:
                    turtle.title(n)
            else:
                n=n+o
            n=n+o
            turtle.title(n)
            if (str(type(rgbvar)) == "<class 'tkinter.IntVar'>" and trailed == 1):
                if (rgbvar.get()==1):
                    t_end = time.time() + 0.0005
                    while time.time() < t_end:
                        turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
                else:
                    pass
            elif (str(type(rgbvar)) == "<class 'int'>" and trailed == 1):
                if (rgbvar==1):
                    t_end = time.time() + 0.0005
                    while time.time() < t_end:
                        turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
                else:
                    pass
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
    if str(type(Autovar)) == "<class 'tkinter.IntVar'>":
        if (Autovar.get()==1):
            turtle.onclick(fxn(xin,yin))
        else:
            turtle.onclick(fxn)
    else:
        if (Autovar==1):
            turtle.onclick(fxn(xin,yin))
        else:
            turtle.onclick(fxn)
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
        skin.add_radiobutton(label="Ronaldo2", command=lambda:turtle.shape("rol2.gif"))
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
        savemenu = Menu(menubar, tearoff=0)
        savemenu.add_command(label="Reset Progress", command=resetsavefile)
        savemenu.add_command(label="Save Settings", command=savesettings)
        savemenu.add_command(label="Reset Settings", command=resetsettings)
        menubar.add_cascade(label="Savefile", menu=savemenu)
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
