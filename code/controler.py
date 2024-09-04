import tkinter as tk
from gtts import gTTS
import os
from tkinter import *
import socket

#variables

#server
ip = "192.168.1.76" # IP of Raspberry Pi
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, 2325))
print("CLIENT: connected")

#audio info

language = "en"

flagGreen_text = "Green Flag"
flagGreen_audio = gTTS(text=flagGreen_text, lang=language, slow=False)
flagGreen_audio.save("flagGreen_play.mp3")

flagYellow_text = "Yellow Flag, slow down"
flagYellow_audio = gTTS(text=flagYellow_text, lang=language, slow=False)
flagYellow_audio.save("flagYellow_play.mp3")

flagRed_text = "Red Flag, slow down and come to a stop"
flagRed_audio = gTTS(text=flagRed_text, lang=language, slow=False)
flagRed_audio.save("flagRed_play.mp3")

flagBlue_text = "Blue flag, move out of the way and let faster cars past"
flagBlue_audio = gTTS(text=flagBlue_text, lang=language, slow=False)
flagBlue_audio.save("flagBlue_play.mp3")

#other functions

#button commands
    
    #top row commands

def flagGreen_command():
    #os.system("start flagGreen_play.mp3")
    
    msg_green = "Green flag"
    # send a message
    client.send(msg_green.encode())

def flagYellow_command():
    #os.system("start flagYellow_play.mp3")
    
    msg_yellow = "Yellow flag"
    # send a message
    client.send(msg_yellow.encode())   
    
def flagRed_command():
    #os.system("start flagRed_play.mp3") 
    
    msg_red = "Red flag"
    # send a message
    client.send(msg_red.encode())    
    
def flagBlue_command():
    #os.system("start flagBlue_play.mp3")  
    
    msg_blue = "Blue flag"
    # send a message
    client.send(msg_blue.encode())    

def shutdown():
    msg_exit = "exit_server"
    # send a message
    client.send(msg_exit.encode())

    # exit
    client.close()
    print("left server")
    
    exit()

def PB_cmd():
    msg_PB = "PB_alert"
    # send a message
    client.send(msg_PB.encode())
    
pass
    #2nd row commands
 
def updatePos_cmd():
    global pos_clicked
    print("value is " + pos_clicked.get())
    
    msg_posUpdate = str("pos" + " " + pos_clicked.get())
    client.send(msg_posUpdate.encode())

pass
    #3rd row commands

def updateTimer_cmd():
    global time_clicked
    print("value is " + time_clicked.get())
    
    msg_timerUpdate = str("time" + " " + time_clicked.get())
    client.send(msg_timerUpdate.encode()) 

# set up visual display 

display = tk.Tk()

#top row buttons

flagGreen_select = tk.Button(
    text="green flag",
    width=8,
    height=4,
    command=flagGreen_command,
    bg="#00FF00")
flagGreen_select.grid(row=4, column=4, pady=50, padx=50)

flagYellow_select = tk.Button(
    text="yellow flag",
    width=8,
    height=4,
    command=flagYellow_command,
    bg="#FFFF00")
flagYellow_select.grid(row=4, column=5, pady=50, padx=50)

flagRed_select = tk.Button(
    text="red flag",
    width=8,
    height=4,
    command=flagRed_command,
    bg="#FF0000")
flagRed_select.grid(row=4, column=6, pady=50, padx=50)

flagBlue_select = tk.Button(
    text="Blue flag",
    width=8,
    height=4,
    command=flagBlue_command,
    bg="#399dbc")
flagBlue_select.grid(row=4, column=7, pady=50, padx=50)

PBAlert_btn = tk.Button(
    text = "PB_alert",
    width=9,
    height=4,
    command=PB_cmd)
PBAlert_btn.grid(row=4, column=10, pady=50, padx=50)

close_btn = tk.Button(
    text = "Exit program",
    width=9,
    height=4,
    command=shutdown)
close_btn.grid(row=4, column=11, pady=50, padx=50)

#2nd row buttons

position_options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
pos_clicked = StringVar(display)
pos_clicked.set(position_options[0])

position_drop = OptionMenu(display, pos_clicked, *position_options)
position_drop.grid(row=6, column=5, pady=50, padx=50)

sendPosition_btn = tk.Button(
    text="Update current position",
    command=updatePos_cmd)
sendPosition_btn.grid(row=6, column=6, pady=50, padx=50)

print(pos_clicked)

#3rd row buttons

time_options = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95]
time_clicked = StringVar(display)
time_clicked.set(time_options[0])

time_drop = OptionMenu(display, time_clicked, *time_options)
time_drop.grid(row=8, column=5, pady=50, padx=50)

sendTimer_btn = tk.Button(
    text="Set time remaining",
    command=updateTimer_cmd)
sendTimer_btn.grid(row=8, column=6, pady=50, padx=50)

display.attributes('-fullscreen', True)
#display.attributes('-topmost', True)
display.mainloop()