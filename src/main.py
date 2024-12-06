#import
import turtle, random, winsound, webbrowser, sys, base64, string, gc, json, ctypes, os,urllib, requests, threading, subprocess, re, tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import colorchooser
from pathlib import Path
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
if getattr(sys, 'frozen', False):
    bin_path = os.path.dirname(sys.executable)
elif __file__:
    bin_path = os.path.dirname(__file__)
localappdata_path = os.path.join(os.environ['LOCALAPPDATA'], "AmogusClick")    
Path(localappdata_path).mkdir(parents=True, exist_ok=True)
if os.path.isfile(os.path.join(localappdata_path, "savefile.json")):
    pass
elif not os.path.isfile(os.path.join(localappdata_path, "savefile.json")):
    with open(os.path.join(localappdata_path, "savefile.json"), 'w+') as file:
        file.write('{"highscore":0}')
        file.close()
if os.path.isfile(os.path.join(localappdata_path, "settings.json")):
    pass
elif not os.path.isfile(os.path.join(localappdata_path, "settings.json")):
    with open(os.path.join(localappdata_path, "settings.json"), 'w+') as file:
        file.write('{"lastskin":1, "lastmusic":0, "lastauto":0, "lastboost":0, "lasttrail":0, "lastcons":false, "lastspeed":5, "lastrgb":0, "lastbgcolor":[0, 0, 0], "lasttrailcolor":[255, 0, 0]}')
        file.close()
else:
    pass
def show_hide_console():
    global console_toggled
    if console_toggled==1:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
    else:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    console_toggled = not console_toggled
startwindow = tkinter.Tk()
startwindow.geometry('400x450')
startwindow.title("Main menu")
startwindow.resizable(False, False)
startwindow.iconbitmap(os.path.join(bin_path, "icon.ico"))
def on_exit():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
    startwindow.destroy()
    sys.exit()
startwindow.protocol("WM_DELETE_WINDOW", on_exit)
background_image = PhotoImage(file = os.path.join(bin_path, "skin1.gif"))
upper_half_image = Label(startwindow, image = background_image)
upper_half_image.place(x = 0,y = -1)
bottom_half_image= Label(startwindow, image = background_image)
bottom_half_image.place(x = 0,y = 240)
difficulty_label = Label(startwindow, text = "Gamemode is EASY", bg="indigo", fg='#FFFFFF')
difficulty_label.pack()
last_key = None
music=0
loaded=0
console_toggled = 0
data=0
settings=0
current_point=0
trail=0
setting_menu = 0
point_multiplier=1
skin=1
speed=2
current_version="1.19.1"
url="https://youtu.be/dQw4w9WgXcQ"
keypresseasteregg="setting_menu.bind('<KeyPress>', keypress_handler)"
lastest_version=""
trail_color = (255, 0, 0)
background_color = (0, 0, 0)
activation_key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
request_key = base64.b16encode(activation_key.encode('utf-8')).decode("utf-8")
automated=tk.IntVar()
trail_state=tk.IntVar()
boosted=tk.IntVar()
rgb_trail_state=tk.IntVar()
trail_color_inputed_hex = tk.StringVar()
background_color_inputed_hex = tk.StringVar()
le=Label()
password_entry = Entry()
def set_background_image():
    global background_image
    global upper_half_image
    global bottom_half_image
    upper_half_image.destroy()
    bottom_half_image.destroy()
    if skin==1:
        background_image = PhotoImage(file = os.path.join(bin_path,"skin1.gif"))
    elif skin==2:
        background_image = PhotoImage(file = os.path.join(bin_path,"skin2.gif"))
    elif skin==3:
        background_image = PhotoImage(file = os.path.join(bin_path,"skin3.gif"))
    elif skin==4:
        background_image = PhotoImage(file = os.path.join(bin_path,"skin4.gif"))
    elif skin==5:
        background_image = PhotoImage(file = os.path.join(bin_path,"egg.gif"))
    elif skin==6:
        background_image = PhotoImage(file = os.path.join(bin_path,"gegg.gif"))
    elif skin==10:
        background_image = PhotoImage(file = os.path.join(bin_path,"mono.gif"))
    elif skin==11:
        background_image = PhotoImage(file = os.path.join(bin_path,"ronaldo.gif"))
    elif skin==12:
        background_image = PhotoImage(file = os.path.join(bin_path,"chad.gif"))
    elif skin==13:
        background_image = PhotoImage(file = os.path.join(bin_path,"chip.gif"))
    elif skin==14:
        background_image = PhotoImage(file = os.path.join(bin_path,"potato.gif"))
    elif skin==15:
        background_image = PhotoImage(file = os.path.join(bin_path,"brick.gif"))
    elif skin==16:
        background_image = PhotoImage(file = os.path.join(bin_path,"cat.gif"))
    elif skin==17:
        background_image = PhotoImage(file = os.path.join(bin_path,"ronaldo2.gif"))
    elif skin==127:
        background_image = PhotoImage(file = os.path.join(bin_path,"skin50.gif"))
    upper_half_image = Label(startwindow, image = background_image)
    upper_half_image.place(x = 0,y = -1)
    bottom_half_image= Label(startwindow, image = background_image)
    bottom_half_image.place(x = 0,y = 240)
    arrange_button()
def load_settings():
    global settings
    with open(os.path.join(localappdata_path, "settings.json"), "r") as settingsfile:
        global settings
        try:
            global settings, music, skin, automated, boosted, trail_state, console_toggled, speed, rgb_trail_state, background_color, trail_color
            settings = json.load(settingsfile)
            music=settings["lastmusic"]
            skin=settings["lastskin"]
            automated=settings["lastauto"]
            boosted=settings["lastboost"]
            trail_state=settings["lasttrail"]
            console_toggled=settings["lastcons"]
            speed=settings["lastspeed"]
            rgb_trail_state=settings["lastrgb"]
            background_color=settings["lastbgcolor"]
            trail_color=settings["lasttrailcolor"]
            show_hide_console()
        except:
            tkinter.messagebox.showinfo("Config file error", "Invalid config file detected! Attempted to reset")
            with open(os.path.join(localappdata_path, "settings.json"), 'w+') as rsettingfile:
                rsettingfile.write('{"lastskin":1, "lastmusic":0, "lastauto":0, "lastboost":0, "lasttrail":0, "lastcons":false, "lastspeed":5, "lastrgb":0, "lastbgcolor":[0, 0, 0], "lasttrailcolor":[255, 0, 0]}')
                rsettingfile.close()
def save_settings():
    global music, skin, automated, boosted, trail_state, console_toggled, speed, rgb_trail_state, background_color, trail_color
    if str(type(automated)) == "<class 'tkinter.IntVar'>":
        settingssave = {
                    "lastskin": skin,
                    "lastmusic": music,
                    "lastauto": automated.get(),
                    "lastboost": boosted.get(),
                    "lasttrail": trail_state.get(),
                    "lastcons": console_toggled,
                    "lastspeed": speed,
                    "lastrgb": rgb_trail_state.get(),
                    "lastbgcolor":background_color,
                    "lasttrailcolor":trail_color,
            }
    else:
        settingssave = {
                    "lastskin": skin,
                    "lastmusic": music,
                    "lastauto": automated,
                    "lastboost": boosted,
                    "lasttrail": trail_state,
                    "lastcons": console_toggled,
                    "lastspeed": speed,
                    "lastrgb": rgb_trail_state,
                    "lastbgcolor":background_color,
                    "lasttrailcolor":trail_color,
            }
    with open(os.path.join(localappdata_path, "settings.json"), 'w') as localsettingfile:
        json.dump(settingssave, localsettingfile)
def reset_settings():
    with open(os.path.join(localappdata_path, "settings.json"), 'w+') as localsettingfile:
        localsettingfile.write('{"lastskin":1, "lastmusic":0, "lastauto":0, "lastboost":0, "lasttrail":0, "lastcons":false, "lastspeed":5, "lastrgb":0, "lastbgcolor":[0, 0, 0], "lasttrailcolor":[255, 0, 0]}')
        localsettingfile.close()
def set_skin_id(id):
    global skin
    global music
    if id not in [7,8,9]:
        skin = id
        set_background_image()
        arrange_button()
    elif id == 7 :
        skin = id
        music= 2
    elif id == 8 :
        skin = id
    elif id == 9 :
        skin = id
def random_skin():
    global skin
    skin=random.randint(1,17)
    set_background_image()
    arrange_button()
def start():
    startwindow.quit()
def check_for_update():
    global lastest_version
    hosts = urllib.request.urlopen('https://enderminecraft.github.io/ver.txt')
    lastest_version = hosts.read()
    if (str(lastest_version.strip().decode('utf-8')) == current_version):
        tkinter.messagebox.showinfo(" ", "App is up to date!")
    elif (str(lastest_version.strip().decode('utf-8')) != current_version):
        msg_box = tk.messagebox.askquestion("Update", "App is not up to date! App is on version " + current_version + " but lastest version is " + str(lastest_version.strip().decode('utf-8')) + "!.Do you want to update?")
        if msg_box == 'yes':
            def upd():
                newVersion = requests.get("https://github.com/enderMinecraft/AmogusCLICK/releases/latest/download/Installer.exe")
                open(os.path.join(localappdata_path, "installer.exe"), "wb").write(newVersion.content)
                qsn = msg_box = tk.messagebox.askquestion(" ", "Download complete! Would you want to install update right now?")
                if qsn == 'yes':
                    os.system("start %Localappdata%\\AmogusClick\\installer.exe")
                    os.kill(os.getpid(), True)
                if qsn == 'no':
                    updthread.Terminate()
            updthread = threading.Thread(target=upd)
            updthread.start()
def hidden():
    tkinter.messagebox.showinfo("hi", "hi")
def myth():
        tkinter.messagebox.showinfo("369 "*37,  "369 "*891 )
def about():
    abt = tkinter.Toplevel(None)
    abt.title("About")
    abt.geometry('310x200')
    abt.resizable(False, False)
    i = Label(abt, text = "AmogusClick",font=("Segoe UI", 15))
    i.pack(expand=True)
    i = Label(abt, text = "Version " + current_version + "\n EnderMinecraft")
    i.pack(expand=True)
    i = Label(abt, text = "Website: \n https://github.com/EnderMinecraft/AmogusCLICK")
    i.pack(expand=True)
    button = ttk.Button(abt, text="Check for update", command=check_for_update)
    button.pack(side=BOTTOM)
def show_help():
    tkinter.messagebox.showinfo("Help","Choose Difficulty & Skin and press start. Your goal is reach as much point as possible by clicking the image")
def rickroll():
    webbrowser.open_new(url)
def read_save_file():
    global data
    with open(os.path.join(localappdata_path, "savefile.json"), "r") as infile:
        global data
        try:
            global data
            data = json.load(infile)
        except:
            tkinter.messagebox.showinfo("Savefile error", "Invalid savefile detected")
            with open(os.path.join(localappdata_path, "savefile.json"), 'w+') as file:
                file.write('{"highscore":0}')
                file.close()
    infile.close()
def reset_save_file():
    resetsvf = {
                "highscore": 0,
            }
    with open(os.path.join(localappdata_path, "savefile.json"), "w") as localsavefile:
                json.dump(resetsvf, localsavefile)
    read_save_file()
def loadsavefile():
    read_save_file()
    global loaded
    global data
    loaded = 1
read_save_file()
def easy_mode():
        global speed
        speed=2
        global difficulty_label
        difficulty_label.destroy()
        difficulty_label = Label(startwindow, text = "Gamemode is EASY", bg="indigo", fg='#FFFFFF')
        difficulty_label.pack()
def normal_mode():
        global speed
        speed=5
        global difficulty_label
        difficulty_label.destroy()
        difficulty_label = Label(startwindow, text = "Gamemode is NORMAL", bg="indigo", fg='#FFFFFF')
        difficulty_label.pack()
def hard_mode():
        global speed
        speed=10
        global difficulty_label
        difficulty_label.destroy()
        difficulty_label = Label(startwindow, text = "Gamemode is HARD", bg="indigo", fg='#FFFFFF')
        difficulty_label.pack()
def set_music_id(id):
    global music
    music = id
def arrange_button():
    button = ttk.Button(startwindow, text="Myth", command=myth)
    button.place(x=310, y=400)
    button = ttk.Button(startwindow, text="Easy", command=easy_mode)
    button.place(x=70, y=60)
    button = ttk.Button(startwindow, text="Normal", command=normal_mode)
    button.place(x=160, y=60)
    button = ttk.Button(startwindow, text="Hard", command=hard_mode)
    button.place(x=250, y=60)
    button = ttk.Button(startwindow, text="START", command=startwindow.destroy)
    button.place(x=160, y=150)
arrange_button()
def activation():
    global password_entry, value
    value = str(password_entry.get())
    if value == activation_key:
        set_skin_id(127)
        tkinter.messagebox.showinfo("Correct","Got it man!")
    elif value == "SHOW":
        tkinter.messagebox.showinfo("ACTCODE",activation_key)
    else:
        tkinter.messagebox.showinfo("Invalid","Try to crack? Not that easy")
def activationwindow():
    global password_entry
    activationwindowbox = tkinter.Toplevel()
    activationwindowbox.title("Enter Activate code")
    activationwindowbox.geometry('400x150')
    activationwindowbox.resizable(False, False)
    signin = ttk.Frame(activationwindowbox)
    signin.pack(padx=5, pady=5, fill='x', expand=False)
    password_label = ttk.Label(signin, text="Enable Code:")
    password_label.pack(fill='x', expand=True)
    password_entry = ttk.Entry(signin, show="*")
    password_entry.pack(fill='x', expand=True)
    login_button = ttk.Button(signin, text="Check", command=activation)
    login_button.pack(fill='x', expand=True, pady=10)
    reqb = ttk.Button(signin, text="Request Code", command=lambda:tk.messagebox.showinfo("RequestCode", request_key))
    reqb.pack(fill='x', expand=True, pady=10)
def hexinputtrailcolor(box, arg):
    global trail_color
    global le
    arg = arg.get()
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', arg)
    if match:
        trail_color = h2rgb(arg)
        trail_color_preview = Label(setting_menu, text = "     ", bd = 0, bg = arg)
        trail_color_preview.place(x=282, y=3)
        trail_color_preview.bind("<Button-1>", lambda e:colorpickerfortrail())
    else:
        le = Label(setting_menu, text = "Invalid Hex value\n(e.g. #42e0f5)", fg="#ff1605", bd=1)
        le.place(x=90, y=50)
        le.after(1000, le.destroy)
        box.delete(0, tk.END)
def hexinputbackgroundcolor(box, arg):
    global background_color
    global le
    arg = arg.get()
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', arg)
    if match:
        background_color = h2rgb(arg)
        background_color_preview = Label(setting_menu, text = "     ", bd = 0, bg = arg)
        background_color_preview.place(x=282, y=33)
        background_color_preview.bind("<Button-1>", lambda e:colorpickerforbackground())
    else:
        le = Label(setting_menu, text = "Invalid Hex value\n(e.g. #42e0f5)", fg="#ff1605", bd=1)
        le.place(x=90, y=50)
        le.after(1000, le.destroy)
        box.delete(0, END)
def h2rgb(value):
    #hex2rgb converter
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
def randomtrailcolor(r, g ,b):
    global trail_color
    trail_color = (r, g ,b)
    trailcolorpreview = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    l1 = Label(setting_menu, text = "     ", bd = 0, bg = trailcolorpreview)
    l1.place(x=282, y=3)
    l1.bind("<Button-1>", lambda e:colorpickerfortrail())   
def randombackgroundcolor(r, g ,b):
    global background_color
    background_color = (r, g, b)
    backgroundcolorpreview = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    l2 = Label(setting_menu, text = "     ", bd = 0, bg = backgroundcolorpreview)
    l2.place(x=282, y=33)
    l2.bind("<Button-1>", lambda e:colorpickerforbackground())
def colorpickerfortrail():
    global trail_color
    color_code = colorchooser.askcolor(title ="Choose color") 
    if color_code[1] == None:
        pass
    else:    
        trailcolorpreview= color_code[1]
        l1 = Label(setting_menu, text = "     ", bd = 0, bg = trailcolorpreview)
        l1.place(x=282, y=3)
        l1.bind("<Button-1>", lambda e:colorpickerfortrail())
    if color_code[0] == None:
        pass
    else:    
        trail_color = color_code[0]
def colorpickerforbackground():
    global background_color
    color_code = colorchooser.askcolor(title ="Choose color")
    if color_code[1] == None:
        pass
    else:    
        backgroundcolorpreview= color_code[1]
        l2 = Label(setting_menu, text = "     ", bd = 0, bg = backgroundcolorpreview)
        l2.place(x=282, y=33)
        l2.bind("<Button-1>", lambda e:colorpickerforbackground())
    if color_code[0] == None:
        pass
    else:    
        background_color = color_code[0]
def settingswindow():
    global setting_menu
    global music
    global speed
    global keypresseasteregg
    setting_menu = tkinter.Toplevel(None)
    setting_menu.title("Settings")
    setting_menu.geometry('310x200')
    setting_menu.resizable(False, False)
    settingmenubar = Menu(setting_menu)
    setting_menu.config(menu=settingmenubar)
    extendedskins = Menu(settingmenubar, tearoff=0)
    extendedskins.add_radiobutton(label="Skin1", command=lambda : set_skin_id(7))
    extendedskins.add_radiobutton(label="Skin2", command=lambda : set_skin_id(8))
    extendedskins.add_radiobutton(label="Skin3", command=lambda : set_skin_id(9))
    settingmenubar.add_cascade(label="Secret Skin", menu=extendedskins, underline=0)
    current_speed_label = Label(setting_menu, text = speed, bd = 0)
    current_speed_label.place(x=140, y=86)
    def speedlabel():
        global speed
        speed = round(wspeed.get())
        current_speed_label = Label(setting_menu, text = speed)
        current_speed_label.place(x=140, y=86)
    text_trail_label = Label(setting_menu, text = "Customize trail color:", bd=0)
    text_trail_label.place(x=70, y=0)
    apply_trail_color = tk.Button(setting_menu, text=u'\u2705', command=lambda: hexinputtrailcolor(color_entry, trail_color_inputed_hex), borderwidth=0, fg="#05ff09", font=("Segoe UI Emoji", 10))
    apply_trail_color.place(x=240, y=-1)
    random_trail_color = tk.Button(setting_menu, text='\U0001F504', command=lambda: randomtrailcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255)), borderwidth=0, font=("Segoe UI Emoji", 10), fg="#0078D7")
    random_trail_color.place(x=260, y=-1)
    color_entry=ttk.Entry(setting_menu, textvariable=trail_color_inputed_hex, width=6)
    color_entry.place(x=190, y=0)

    text_background_label = Label(setting_menu, text = "Customize BG color:", bd=0)
    text_background_label.place(x=70, y=30)
    apply_background_color = tk.Button(setting_menu, text='✅', command=lambda: hexinputbackgroundcolor(bg_entry, background_color_inputed_hex), borderwidth=0, fg="#05ff09", font=("Segoe UI Emoji", 10))
    apply_background_color.place(x=240, y=30)
    random_background_color = tk.Button(setting_menu, text='\U0001F504', command=lambda: randombackgroundcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255)), borderwidth=0, font=("Segoe UI Emoji", 10), fg="#0078D7")
    random_background_color.place(x=260, y=30)
    bg_entry=ttk.Entry(setting_menu, textvariable=background_color_inputed_hex, width=6)
    bg_entry.place(x=190, y=30)
    trail_color_preview = Label(setting_menu, text = "     ", bd = 0, bg = "#ffffff")
    trail_color_preview.place(x=282, y=3)
    background_color_preview = Label(setting_menu, text = "     ", bd = 0, bg = "#000000")
    background_color_preview.place(x=282, y=33)
    
    trail_color_preview.bind("<Button-1>", lambda e:colorpickerfortrail())
    background_color_preview.bind("<Button-1>", lambda e:colorpickerforbackground())
    
    separator = ttk.Separator(setting_menu, orient='vertical')
    separator.place(relx=0.2, rely=0, relheight=0.4)
    button = tk.Button(setting_menu, text="✅", command=speedlabel, borderwidth=0, fg="#05ff09")
    button.place(x=110, y=85)
    button = ttk.Button(setting_menu, text="Show console", command=show_hide_console)
    button.place(x=220, y=170)
    button = ttk.Button(setting_menu, text="Clear command", command=lambda: cmd_entry.delete(0, END))
    button.place(x=113, y=170)
    boostchk = ttk.Checkbutton(setting_menu, text='Boost',variable=boosted, onvalue=1, offvalue=0)
    boostchk.place(x=0, y=40)
    boostchk = ttk.Checkbutton(setting_menu, text='Trail',variable=trail_state, onvalue=1, offvalue=0)
    boostchk.place(x=0, y=20)
    boostchk = ttk.Checkbutton(setting_menu, text='Auto',variable=automated, onvalue=1, offvalue=0)
    boostchk.place(x=0, y=0)
    boostchk = ttk.Checkbutton(setting_menu, text='RGB',variable=rgb_trail_state, onvalue=1, offvalue=0)
    boostchk.place(x=0, y=60)
    wspeed = ttk.Scale(setting_menu, from_=0, to=10, orient=HORIZONTAL)
    wspeed.place(x=0, y=85)
    cmd_entry=ttk.Entry(setting_menu,width=40)
    cmd_entry.place(x=0, y=133)
    #if there are more custom var,put it inside string below
    l = Label(setting_menu, text = "Enter debug command below!", bd=0)
    l.place(x=0, y=111)
    button3 = ttk.Button(setting_menu, text="Run command!", command=lambda: exec("global background_image, upper_half_image, bottom_half_image, speed, boosted, point_multiplier, skin, music, automated, trail_state, url, loaded, activation_key, request_key, console_toggled, startwindow, data, rgb_trail_state\n"+cmd_entry.get()))
    button3.place(x=5, y=170)
    def keypress_handler(event):
        global last_key
        global keypresseasteregg
        key_pressed = event.keysym
        if key_pressed == 'space':
            if last_key == 'Shift_L':
                global keypresseasteregg
                hidden()
                keypresseasteregg=1
        last_key = key_pressed
    exec(keypresseasteregg)
def on_close():
    global running
    running = 0
menubar = Menu(startwindow)
diffoptionsdropdown = Menu(menubar, tearoff=0)
diffoptionsdropdown.add_radiobutton(label="Easy", command=easy_mode)
diffoptionsdropdown.add_radiobutton(label="Normal", command=normal_mode)
diffoptionsdropdown.add_radiobutton(label="Hard", command=hard_mode)
skinoptionsdropdown = Menu(menubar, tearoff=0)
skinoptionsdropdown.add_radiobutton(label="Pmogus(Default)", command= lambda: set_skin_id(1))
skinoptionsdropdown.add_radiobutton(label="Pimogus", command=lambda: set_skin_id(2))
skinoptionsdropdown.add_radiobutton(label="Bmogus", command=lambda: set_skin_id(3))
skinoptionsdropdown.add_radiobutton(label="RMOGUS", command=lambda: set_skin_id(4))
skinoptionsdropdown.add_radiobutton(label="Egg", command=lambda: set_skin_id(5))
skinoptionsdropdown.add_radiobutton(label="Golden Egg", command=lambda: set_skin_id(6))
skinoptionsdropdown.add_radiobutton(label="MONO", command=lambda: set_skin_id(10))
skinoptionsdropdown.add_radiobutton(label="Ronaldo", command=lambda: set_skin_id(11))
skinoptionsdropdown.add_radiobutton(label="GigaChad", command=lambda: set_skin_id(12))
skinoptionsdropdown.add_radiobutton(label="Chip", command=lambda: set_skin_id(13))
skinoptionsdropdown.add_radiobutton(label="Potato", command=lambda: set_skin_id(14))
skinoptionsdropdown.add_radiobutton(label="Brick", command=lambda: set_skin_id(15))
skinoptionsdropdown.add_radiobutton(label="Cat", command=lambda: set_skin_id(16))
skinoptionsdropdown.add_radiobutton(label="Ronaldo2", command=lambda: set_skin_id(17))
skinoptionsdropdown.add_radiobutton(label="Random", command=random_skin)
musicoptionsdropdown = Menu(menubar, tearoff=0)
musicoptionsdropdown.add_radiobutton(label="CTAC(Default)", command=lambda:set_music_id(0))
musicoptionsdropdown.add_radiobutton(label="Rick", command=lambda:set_music_id(2))
musicoptionsdropdown.add_radiobutton(label="MONO", command=lambda:set_music_id(1))
musicoptionsdropdown.add_radiobutton(label="Ronaldo", command=lambda:set_music_id(3))
musicoptionsdropdown.add_radiobutton(label="Potato&Chips", command=lambda:set_music_id(4))
musicoptionsdropdown.add_radiobutton(label="Chad", command=lambda:set_music_id(5))
musicoptionsdropdown.add_radiobutton(label="Brick", command=lambda:set_music_id(6))
saveoptionsdropdown = Menu(menubar, tearoff=0)
saveoptionsdropdown.add_command(label="Load Progress", command=loadsavefile)
saveoptionsdropdown.add_command(label="Reset Progress", command=reset_save_file)
saveoptionsdropdown.add_command(label="Load Settings", command=load_settings)
saveoptionsdropdown.add_command(label="Save Settings", command=save_settings)
saveoptionsdropdown.add_command(label="Reset Settings", command=reset_settings)
saveoptionsdropdown.add_command(label="Open Savefile Folder", command=lambda: subprocess.Popen("explorer " + localappdata_path))
helpoptionsdropdown = Menu(menubar, tearoff=0)
helpoptionsdropdown.add_command(label="Help", command=show_help)
helpoptionsdropdown.add_command(label="DO NOT CLICK", command=rickroll)
helpoptionsdropdown.add_command(label="Myth", command=myth)
helpoptionsdropdown.add_command(label="About", command=about)
extraoptionsdropdown = Menu(menubar, tearoff=0)
extraoptionsdropdown.add_command(label="somesecretskin:)", command=activationwindow)
extraoptionsdropdown.add_command(label="Settings", command=lambda: settingswindow())
menubar.add_cascade(label="Difficulty", menu=diffoptionsdropdown)
menubar.add_cascade(label="Skin", menu=skinoptionsdropdown)
menubar.add_cascade(label="Music", menu=musicoptionsdropdown)
menubar.add_cascade(label="Savefile", menu=saveoptionsdropdown)
menubar.add_cascade(label="Help", menu=helpoptionsdropdown)
menubar.add_cascade(label="Extra", menu=extraoptionsdropdown)
startwindow.config(menu=menubar)
startwindow.mainloop()
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
gc.collect()
gamewindow=turtle.Screen()
gamewindow.colormode(255)
gamewindow.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_close)
gamewindow.title(0)
gamewindow.bgcolor(background_color)
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
gamewindow.setup(1000,700)
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
    current_point=500000
    point_multiplier=127
elif str(type(boosted)) == "<class 'tkinter.IntVar'>":
    if (boosted.get()==1):
        current_point=200
        point_multiplier=999
    else:
        current_point=0
        point_multiplier=1
elif str(type(boosted)) == "<class 'int'>":
    if (boosted==1):
        current_point=200
        point_multiplier=999
    else:
        current_point=0
        point_multiplier=1
else:
    current_point=0
    point_multiplier=1
if (loaded==1):
    current_point=current_point+int(data["highscore"])
else:
    pass
gamewindow.title(current_point)
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
if str(type(trail_state)) == "<class 'tkinter.IntVar'>":
    if(trail_state.get()==1):
        trail=1
        turtle.color(trail_color)
        turtle.pendown()
    elif(trail_state.get()==0):
        turtle.penup()
else:
    if(trail_state==1):
        trail=1
        turtle.color(trail_color)
        turtle.pendown()
    elif(trail_state==0):
        turtle.penup()
if (str(type(rgb_trail_state)) == "<class 'tkinter.IntVar'>" and trail == 1):
    if (rgb_trail_state.get()==1):
        turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    else:
        pass
elif (str(type(rgb_trail_state)) == "<class 'int'>" and trail == 1):
    if (rgb_trail_state==1):
        turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
else:
    pass
turtle.speed(speed)
xoffset=random.randint(5, 12)
yoffset=random.randint(5, 12)
while running == 1:
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
    def on_click_event(a, b):
        if (paused == 0):
            global current_point
            global point_multiplier
            a=random.randint(round(-gamewindow.window_width()/2),round(gamewindow.window_width()/2))
            b=random.randint(round(-gamewindow.window_height()/2),round(gamewindow.window_height()/2))
            turtle.setposition(a, b)
            if(skin==127):
                current_point=current_point*7
            elif str(type(boosted)) == "<class 'tkinter.IntVar'>":
                if (boosted.get()==1):
                    current_point=current_point*point_multiplier
                else:
                    turtle.title(current_point)
            elif str(type(boosted)) == "<class 'int'>":
                if (boosted==1):
                    current_point=current_point*point_multiplier
                else:
                    turtle.title(current_point)
            else:
                current_point=current_point+point_multiplier
            current_point=current_point+point_multiplier
            turtle.title(current_point)
            if (str(type(rgb_trail_state)) == "<class 'tkinter.IntVar'>" and trail == 1):
                if (rgb_trail_state.get()==1):
                    turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
                else:
                    pass
            elif (str(type(rgb_trail_state)) == "<class 'int'>" and trail == 1):
                if (rgb_trail_state==1):
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
        xfinal = x+xoffset
        yfinal = y+yoffset
    else:
        pass
    if (running==0):
        turtle.bye()
        break
    if (paused==0):
        turtle.setposition(xfinal, yfinal)
    else:
        pass
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
    if turtle.xcor() >= gamewindow.window_width()/2 or turtle.xcor() <=-gamewindow.window_width()/2:
        turtle.speed(0)
        xoffset = xoffset * -1
        turtle.right(random.randint(60, 180)) if turtle.xcor() <=-gamewindow.window_width()/2 else turtle.left(random.randint(60, 180))
        turtle.speed(speed)
    if turtle.ycor() >= gamewindow.window_height()/2 or turtle.ycor() <=-gamewindow.window_height()/2:
        yoffset = yoffset * -1
        turtle.speed(0)
        turtle.right(random.randint(180, 270)) if turtle.ycor() >= gamewindow.window_height()/2 else turtle.left(random.randint(180, 270))
        turtle.speed(speed)
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        break
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break
    if str(type(automated)) == "<class 'tkinter.IntVar'>":
        if (automated.get()==1):
            turtle.onclick(on_click_event(xoffset,yoffset))
        else:
            turtle.onclick(on_click_event)
    else:
        if (automated==1):
            turtle.onclick(on_click_event(xoffset,yoffset))
        else:
            turtle.onclick(on_click_event)
    turtle.onclick(on_click_event)
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
                "highscore": current_point,
            }
            with open(os.path.join(localappdata_path, "savefile.json"), "w") as localsavefile:
                json.dump(savefile, localsavefile)
    def pausemenu():
        global current_point
        global paused
        global running
        pausemenu = tkinter.Toplevel()
        paused = 1
        def unpause():
            global paused
            paused = 0
            pausemenu.destroy()
        pausemenu.protocol("WM_DELETE_WINDOW", unpause)
        def center_window(width=400, height=200):
            screen_width = pausemenu.winfo_screenwidth()
            screen_height = pausemenu.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            pausemenu.geometry('%dx%d+%d+%d' % (width, height, x, y))
        center_window(400,200)
        pausemenu.title("                                                Paused")
        pausemenu.resizable(False, False)
        menubar = Menu(pausemenu)
        pausemenu.config(menu=menubar)
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
        saveoptionsdropdown = Menu(menubar, tearoff=0)
        saveoptionsdropdown.add_command(label="Reset Progress", command=reset_save_file)
        saveoptionsdropdown.add_command(label="Save Settings", command=save_settings)
        saveoptionsdropdown.add_command(label="Reset Settings", command=reset_settings)
        saveoptionsdropdown.add_command(label="Open Save Folder", command=lambda: subprocess.Popen("explorer " + localappdata_path))
        menubar.add_cascade(label="Savefile", menu=saveoptionsdropdown)
        def restart():
            global current_point
            turtle.speed(0)
            turtle.setpos(0, 0)
            current_point=0
            gamewindow.title(current_point)
            turtle.speed(speed)
        def end():
            global running
            running = 0
            unpause()
        style = ttk.Style()
        button = ttk.Button(pausemenu, text="Continue", command=unpause, style="cn.TButton")
        button.place(x=110, y=0)
        button = ttk.Button(pausemenu, text="Restart", command=restart, style="rs.TButton")
        button.place(x=110, y=50)
        button = ttk.Button(pausemenu, text="Exit", command=end, style="end.TButton")
        button.place(x=110, y=150)
        button = ttk.Button(pausemenu, text="Save", command=save, style="save.TButton")
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
        gamewindow.onkeypress(reset, "r")
        gamewindow.onkeypress(pausemenu, "Escape")
        gamewindow.listen()
    else:
        pass
    if (running==0):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        turtle.bye()
        break