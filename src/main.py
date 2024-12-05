#import
import turtle, random, winsound, webbrowser, sys, base64, string, gc, json, ctypes, os,urllib, requests, threading, subprocess, re
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from tkinter import colorchooser
from pathlib import Path
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
if getattr(sys, 'frozen', False):
    bin_path = os.path.dirname(sys.executable)
elif __file__:
    bin_path = os.path.dirname(__file__)
newpath = os.path.join(os.environ['LOCALAPPDATA'], "AmogusClick")    
Path(newpath).mkdir(parents=True, exist_ok=True)
if os.path.isfile(os.path.join(newpath, "savefile.json")):
    pass
elif not os.path.isfile(os.path.join(newpath, "savefile.json")):
    with open(os.path.join(newpath, "savefile.json"), 'w+') as file:
        file.write('{"highscore":0}')
        file.close()
if os.path.isfile(os.path.join(newpath, "settings.json")):
    pass
elif not os.path.isfile(os.path.join(newpath, "settings.json")):
    with open(os.path.join(newpath, "settings.json"), 'w+') as file:
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
root.iconbitmap(os.path.join(bin_path, "icon.ico"))
def on_exit():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
    root.destroy()
    sys.exit()
root.protocol("WM_DELETE_WINDOW", on_exit)
#bglabelset
bg = PhotoImage(file = os.path.join(bin_path, "skin1.gif"))
label1 = Label(root, image = bg)
label1.place(x = 0,y = -1)
label2= Label(root, image = bg)
label2.place(x = 0,y = 240)
l = Label(root, text = "Gamemode is EASY", bg="indigo", fg='#FFFFFF')
l.pack()
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
current="1.19"
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
cod16 = base64.b16encode(cod.encode('utf-8')).decode("utf-8")
password_entry = Entry()
#bgfunc
def bgfg():
    global bg
    global label1
    global label2
    label1.destroy()
    label2.destroy()
    if skin==1:
        bg = PhotoImage(file = os.path.join(bin_path,"skin1.gif"))
    elif skin==2:
        bg = PhotoImage(file = os.path.join(bin_path,"skin2.gif"))
    elif skin==3:
        bg = PhotoImage(file = os.path.join(bin_path,"skin3.gif"))
    elif skin==4:
        bg = PhotoImage(file = os.path.join(bin_path,"skin4.gif"))
    elif skin==5:
        bg = PhotoImage(file = os.path.join(bin_path,"egg.gif"))
    elif skin==6:
        bg = PhotoImage(file = os.path.join(bin_path,"gegg.gif"))
    elif skin==10:
        bg = PhotoImage(file = os.path.join(bin_path,"mono.gif"))
    elif skin==11:
        bg = PhotoImage(file = os.path.join(bin_path,"ronaldo.gif"))
    elif skin==12:
        bg = PhotoImage(file = os.path.join(bin_path,"chad.gif"))
    elif skin==13:
        bg = PhotoImage(file = os.path.join(bin_path,"chip.gif"))
    elif skin==14:
        bg = PhotoImage(file = os.path.join(bin_path,"potato.gif"))
    elif skin==15:
        bg = PhotoImage(file = os.path.join(bin_path,"brick.gif"))
    elif skin==16:
        bg = PhotoImage(file = os.path.join(bin_path,"cat.gif"))
    elif skin==17:
        bg = PhotoImage(file = os.path.join(bin_path,"ronaldo2.gif"))
    elif skin==127:
        bg = PhotoImage(file = os.path.join(bin_path,"skin50.gif"))
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    btt()
#loadsettings
def loadsettings():
    global settings
    with open(os.path.join(newpath, "settings.json"), "r") as settingsfile:
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
            with open(os.path.join(newpath, "settings.json"), 'w+') as rsettingfile:
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
    with open(os.path.join(newpath, "settings.json"), 'w') as wsettingfile:
        json.dump(settingssave, wsettingfile)
def resetsettings():
    with open(os.path.join(newpath, "settings.json"), 'w+') as wsettingfile:
        wsettingfile.write('{"lastskin":1, "lastmusic":0, "lastauto":0, "lastboost":0, "lasttrail":0, "lastcons":false, "lastspeed":5, "lastrgb":0, "lastbgcolor":[0, 0, 0], "lasttrailcolor":[255, 0, 0]}')
        wsettingfile.close()
#skinfunc
def genskin(id):
    global skin
    global music
    if id not in [7,8,9]:
        skin = id
        bgfg()
        btt()
    elif id == 7 :
        skin = id
        music= 2
    elif id == 8 :
        skin = id
    elif id == 9 :
        skin = id
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
                open(os.path.join(newpath, "installer.exe"), "wb").write(newVersion.content)
                qsn = msg_box = tk.messagebox.askquestion(" ", "Download complete! Would you want to install update right now?")
                if qsn == 'yes':
                    os.system("start %Localappdata%\\AmogusClick\\installer.exe")
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
    with open(os.path.join(newpath, "savefile.json"), "r") as infile:
        global data
        try:
            global data
            data = json.load(infile)
        except:
            tkinter.messagebox.showinfo("Savefile error", "Invalid savefile detected")
            with open(os.path.join(newpath, "savefile.json"), 'w+') as file:
                file.write('{"highscore":0}')
                file.close()
    infile.close()
def resetsavefile():
    resetsvf = {
                "highscore": 0,
            }
    with open(os.path.join(newpath, "savefile.json"), "w") as outfile:
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
def genm(id):
    global music
    music = id
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
skinmenu.add_radiobutton(label="Pmogus(Default)", command= lambda: genskin(1))
skinmenu.add_radiobutton(label="Pimogus", command=lambda: genskin(2))
skinmenu.add_radiobutton(label="Bmogus", command=lambda: genskin(3))
skinmenu.add_radiobutton(label="RMOGUS", command=lambda: genskin(4))
skinmenu.add_radiobutton(label="Egg", command=lambda: genskin(5))
skinmenu.add_radiobutton(label="Golden Egg", command=lambda: genskin(6))
skinmenu.add_radiobutton(label="MONO", command=lambda: genskin(10))
skinmenu.add_radiobutton(label="Ronaldo", command=lambda: genskin(11))
skinmenu.add_radiobutton(label="GigaChad", command=lambda: genskin(12))
skinmenu.add_radiobutton(label="Chip", command=lambda: genskin(13))
skinmenu.add_radiobutton(label="Potato", command=lambda: genskin(14))
skinmenu.add_radiobutton(label="Brick", command=lambda: genskin(15))
skinmenu.add_radiobutton(label="Cat", command=lambda: genskin(16))
skinmenu.add_radiobutton(label="Ronaldo2", command=lambda: genskin(17))
skinmenu.add_radiobutton(label="Random", command=rndskn)
menubar.add_cascade(label="Skin", menu=skinmenu)

musicmenu = Menu(menubar, tearoff=0)
musicmenu.add_radiobutton(label="CTAC(Default)", command=lambda:genm(0))
musicmenu.add_radiobutton(label="Rick", command=lambda:genm(2))
musicmenu.add_radiobutton(label="MONO", command=lambda:genm(1))
musicmenu.add_radiobutton(label="Ronaldo", command=lambda:genm(3))
musicmenu.add_radiobutton(label="Potato&Chips", command=lambda:genm(4))
musicmenu.add_radiobutton(label="Chad", command=lambda:genm(5))
musicmenu.add_radiobutton(label="Brick", command=lambda:genm(6))
menubar.add_cascade(label="Music", menu=musicmenu)

savemenu = Menu(menubar, tearoff=0)
savemenu.add_command(label="Load Progress", command=load)
savemenu.add_command(label="Reset Progress", command=resetsavefile)
savemenu.add_command(label="Load Settings", command=loadsettings)
savemenu.add_command(label="Save Settings", command=savesettings)
savemenu.add_command(label="Reset Settings", command=resetsettings)
savemenu.add_command(label="Open Savefile Folder", command=lambda: subprocess.Popen("explorer " + newpath))
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
        genskin(127)
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
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', arg)
    if match:
        colr = h2rgb(arg)
        l1 = Label(hax, text = "     ", bd = 0, bg = arg)
        l1.place(x=282, y=3)
        l1.bind("<Button-1>", lambda e:colorpicker1())
    else:
        le = Label(hax, text = "Invalid Hex value\n(e.g. #42e0f5)", fg="#ff1605", bd=1)
        le.place(x=90, y=50)
        le.after(1000, le.destroy)
        box.delete(0, tk.END)
def callback2(box, arg):
    global clbg
    global le
    arg = arg.get()
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', arg)
    if match:
        clbg = h2rgb(arg)
        l2 = Label(hax, text = "     ", bd = 0, bg = arg)
        l2.place(x=282, y=33)
        l2.bind("<Button-1>", lambda e:colorpicker2())
    else:
        le = Label(hax, text = "Invalid Hex value\n(e.g. #42e0f5)", fg="#ff1605", bd=1)
        le.place(x=90, y=50)
        le.after(1000, le.destroy)
        box.delete(0, END)
def h2rgb(value):
    #hex2rgb converter
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
#randomlypickcolor
def randomcl1(r, g ,b):
    global colr
    colr = (r, g ,b)
    hexcl1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    l1 = Label(hax, text = "     ", bd = 0, bg = hexcl1)
    l1.place(x=282, y=3)
    l1.bind("<Button-1>", lambda e:colorpicker1())   
def randomcl2(r, g ,b):
    global clbg
    clbg = (r, g, b)
    hexcl2 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    l2 = Label(hax, text = "     ", bd = 0, bg = hexcl2)
    l2.place(x=282, y=33)
    l2.bind("<Button-1>", lambda e:colorpicker2())
#colorpicker
def colorpicker1():
    global colr
    color_code = colorchooser.askcolor(title ="Choose color") 
    if color_code[1] == None:
        pass
    else:    
        hexcl1= color_code[1]
        l1 = Label(hax, text = "     ", bd = 0, bg = hexcl1)
        l1.place(x=282, y=3)
        l1.bind("<Button-1>", lambda e:colorpicker1())
    if color_code[0] == None:
        pass
    else:    
        colr = color_code[0]
def colorpicker2():
    global clbg
    color_code = colorchooser.askcolor(title ="Choose color")
    if color_code[1] == None:
        pass
    else:    
        hexcl2= color_code[1]
        l2 = Label(hax, text = "     ", bd = 0, bg = hexcl2)
        l2.place(x=282, y=33)
        l2.bind("<Button-1>", lambda e:colorpicker2())
    if color_code[0] == None:
        pass
    else:    
        clbg = color_code[0]

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
    hskin.add_radiobutton(label="Skin1", command=lambda : genskin(7))
    hskin.add_radiobutton(label="Skin2", command=lambda : genskin(8))
    hskin.add_radiobutton(label="Skin3", command=lambda : genskin(9))
    Dev.add_cascade(label="Secret Skin", menu=hskin, underline=0)
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
    l1 = Label(hax, text = "     ", bd = 0, bg = "#ffffff")
    l1.place(x=282, y=3)
    l2 = Label(hax, text = "     ", bd = 0, bg = "#000000")
    l2.place(x=282, y=33)
    
    l1.bind("<Button-1>", lambda e:colorpicker1())
    l2.bind("<Button-1>", lambda e:colorpicker2())
    
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
    button3 = ttk.Button(hax, text="Run command!", command=lambda: exec("global bg, label1, label2, speed, boostvar, o, skin, music, Autovar, Trailvar, url, loaded, txt, cod, cod16, console_toggle, root, data, rgbvar\n"+cmd_entry.get()))
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
turtle.register_shape(os.path.join(bin_path,'skin1.gif'))
turtle.register_shape(os.path.join(bin_path,'skin2.gif'))
turtle.register_shape(os.path.join(bin_path,'skin3.gif'))
turtle.register_shape(os.path.join(bin_path,'skin4.gif'))
turtle.register_shape(os.path.join(bin_path,'egg.gif'))
turtle.register_shape(os.path.join(bin_path,'gegg.gif'))
turtle.register_shape(os.path.join(bin_path,'mono.gif'))
turtle.register_shape(os.path.join(bin_path,'skin50.gif'))
turtle.register_shape(os.path.join(bin_path,'rick.gif'))
turtle.register_shape(os.path.join(bin_path,'ronaldo.gif'))
turtle.register_shape(os.path.join(bin_path,'chad.gif'))
turtle.register_shape(os.path.join(bin_path,'chip.gif'))
turtle.register_shape(os.path.join(bin_path,'potato.gif'))
turtle.register_shape(os.path.join(bin_path,'brick.gif'))
turtle.register_shape(os.path.join(bin_path,'cat.gif'))
turtle.register_shape(os.path.join(bin_path,'ronaldo2.gif'))
wn.setup(1000,700)
if(music==0):
    winsound.PlaySound(os.path.join(bin_path,"main.wav"), winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==1):
    winsound.PlaySound(os.path.join(bin_path,"mono.wav"), winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==2):
    winsound.PlaySound(os.path.join(bin_path,"rick.wav"), winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==3):
    winsound.PlaySound(os.path.join(bin_path,"rol.wav"), winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==4):
    winsound.PlaySound(os.path.join(bin_path,"chip.wav"), winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==5):
    winsound.PlaySound(os.path.join(bin_path,"chad.wav"), winsound.SND_ASYNC | winsound.SND_LOOP)
elif(music==6):
    winsound.PlaySound(os.path.join(bin_path,"brick.wav"), winsound.SND_ASYNC | winsound.SND_LOOP)
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
    turtle.shape(os.path.join(bin_path,"skin1.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"skin1.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==2):
    turtle.shape(os.path.join(bin_path,"skin2.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"skin2.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==3):
    turtle.shape(os.path.join(bin_path,"skin3.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"skin3.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==4):
    turtle.shape(os.path.join(bin_path,"skin4.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"skin4.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==5):
    turtle.shape(os.path.join(bin_path,"egg.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"egg.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==6):
    turtle.shape(os.path.join(bin_path,"gegg.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"gegg.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==7):
    turtle.shape(os.path.join(bin_path,"rick.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"rick.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==8):
    turtle.shape(os.path.join(bin_path,"gegg.gif"))
elif (skin==9):
    turtle.shape(os.path.join(bin_path,"gegg.gif"))
elif (skin==127):
    turtle.shape(os.path.join(bin_path,"skin50.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"skin50.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==10):
    turtle.shape(os.path.join(bin_path,"mono.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"mono.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==11):
    turtle.shape(os.path.join(bin_path,"ronaldo.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"ronaldo.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==12):
    turtle.shape(os.path.join(bin_path,"chad.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"chad.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==13):
    turtle.shape(os.path.join(bin_path,"chip.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"chip.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==14):
    turtle.shape(os.path.join(bin_path,"potato.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"potato.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==15):
    turtle.shape(os.path.join(bin_path,"brick.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"brick.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==16):
    turtle.shape(os.path.join(bin_path,"cat.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"cat.gif"))
    turtle._Screen._root.iconphoto(True, img)
elif (skin==17):
    turtle.shape(os.path.join(bin_path,"ronaldo2.gif"))
    img = tkinter.Image("photo", file = os.path.join(bin_path,"ronaldo2.gif"))
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
    def fxn(a, b):
        if (paused == 0):
            global n
            global o
            a=random.randint(round(-wn.window_width()/2),round(wn.window_width()/2))
            b=random.randint(round(-wn.window_height()/2),round(wn.window_height()/2))
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
                    turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
                else:
                    pass
            elif (str(type(rgbvar)) == "<class 'int'>" and trailed == 1):
                if (rgbvar==1):
                    turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
                else:
                    pass
        else:
            pass
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
    x = turtle.xcor()
    y = turtle.ycor()
    if (paused==0):
        xm = x+xin
        ym = y+yin
    else:
        pass
    if (running==0):
        turtle.bye()
        break
    if (paused==0):
        turtle.setposition(xm, ym)
    else:
        pass
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
    if turtle.xcor() >= wn.window_width()/2 or turtle.xcor() <=-wn.window_width()/2:
        xin = xin * -1
    if turtle.ycor() >= wn.window_height()/2 or turtle.ycor() <=-wn.window_height()/2:
        yin = yin * -1
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        break
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
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
    def reset():
        turtle.speed(0)
        turtle.setposition(0,0)
        turtle.speed(speed)
    def save():
            savefile = {
                "highscore": n,
            }
            with open(os.path.join(newpath, "savefile.json"), "w") as outfile:
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
        skin.add_radiobutton(label="Pmogus(Default)", command=lambda:turtle.shape(os.path.join(bin_path,"skin1.gif")))
        skin.add_radiobutton(label="Pimogus", command=lambda:turtle.shape(os.path.join(bin_path,"skin2.gif")))
        skin.add_radiobutton(label="Bmogus", command=lambda:turtle.shape(os.path.join(bin_path,"skin3.gif")))
        skin.add_radiobutton(label="RMOGUS", command=lambda:turtle.shape(os.path.join(bin_path,"skin4.gif")))
        skin.add_radiobutton(label="Egg", command=lambda:turtle.shape(os.path.join(bin_path,"egg.gif")))
        skin.add_radiobutton(label="Golden Egg", command=lambda:turtle.shape(os.path.join(bin_path,"gegg.gif")))
        skin.add_radiobutton(label="MONO", command=lambda:turtle.shape(os.path.join(bin_path,"mono.gif")))
        skin.add_radiobutton(label="Ronaldo", command=lambda:turtle.shape(os.path.join(bin_path,"ronaldo.gif")))
        skin.add_radiobutton(label="GigaChad", command=lambda:turtle.shape(os.path.join(bin_path,"chad.gif")))
        skin.add_radiobutton(label="Chip", command=lambda:turtle.shape(os.path.join(bin_path,"chip.gif")))
        skin.add_radiobutton(label="Potato", command=lambda:turtle.shape(os.path.join(bin_path,"potato.gif")))
        skin.add_radiobutton(label="Brick", command=lambda:turtle.shape(os.path.join(bin_path,"brick.gif")))
        skin.add_radiobutton(label="Cat", command=lambda:turtle.shape(os.path.join(bin_path,"cat.gif")))
        skin.add_radiobutton(label="Ronaldo2", command=lambda:turtle.shape(os.path.join(bin_path,"ronaldo2.gif")))
        menubar.add_cascade(label="Skin", menu=skin)
        music = Menu(menubar, tearoff=0)
        music.add_radiobutton(label="CTAC(Default)", command=lambda:winsound.PlaySound(os.path.join(bin_path,'main.wav'), winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="MONO", command=lambda:winsound.PlaySound(os.path.join(bin_path,'mono.wav'), winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="Rick", command=lambda:winsound.PlaySound(os.path.join(bin_path,'rick.wav'), winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="Ronaldo", command=lambda:winsound.PlaySound(os.path.join(bin_path,'rol.wav'), winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="Potato&Chips", command=lambda:winsound.PlaySound(os.path.join(bin_path,'chip.wav'), winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="Chad", command=lambda:winsound.PlaySound(os.path.join(bin_path,'chad.wav'), winsound.SND_ASYNC | winsound.SND_LOOP))
        music.add_radiobutton(label="Brick", command=lambda:winsound.PlaySound(os.path.join(bin_path,'brick.wav'), winsound.SND_ASYNC | winsound.SND_LOOP))
        menubar.add_cascade(label="Music", menu=music)
        savemenu = Menu(menubar, tearoff=0)
        savemenu.add_command(label="Reset Progress", command=resetsavefile)
        savemenu.add_command(label="Save Settings", command=savesettings)
        savemenu.add_command(label="Reset Settings", command=resetsettings)
        savemenu.add_command(label="Open Save Folder", command=lambda: subprocess.Popen("explorer " + newpath))
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


