import type as t
from plyer import notification
from tqdm import tqdm
import time
import random
import sys

#Variables
waitfor=random.choice([.01,.02,.03,.04,.05,.010])
#---------
#Functions
#---TTS----

# importing the pyttsx library
import pyttsx3

# initialisation

#----------

def start():
    t.type("Time to begin @"+name+"!",.06)
    t.type("Its About time We Begin our jorney to trade Around the PyWorld!",.005)
    for i in tqdm(range(100), desc="Loading Market..."):
        time.sleep(waitfor)
        pass
    print("|ID|-|name|--Market VK1-----|")
    print("|01-Car Market              |")
    print("|02-Textiles Market         |")
    print("|03-Furry Market            |")
    print("|---------------------------|")
    select=input("Choose Product Market>")
    if select=="03":
        F.market()
#---------
t.type("Hello there\n", .05)
t.type("Brought To You by FurroProgrammer01\n", .05)
t.type("Welcome to the Ultimate trading sim\nfirst we need a name to call you!\n", .05)

name = input("Input a name> ")
print("Your name is:",len(name),"Characters Long!")
if len(name)>=27:
    t.type("Sorry! Please Select a name under 27 chars!",.01)
    sys.exit()
t.type("Nice To meet you @" + name + "\n", .03)
engine = pyttsx3.init()
engine.say("Nice to meet you @"+ name)
engine.runAndWait()
t.type("For your reward you will get an Acheivement!", .06)

notification.notify(
    app_name="Tradrr",
    title="Acheivement Unlocked",
    message="Wow I exist? Im now @"+name,
    toast=True,
    ticker="Loading Acheivement",
        # displaying time
    timeout=10
    )
for i in tqdm(range(100), desc="Loading Assets..."):
    time.sleep(waitfor)
    pass
for i in tqdm(range(100), desc="Loading Tkinter..."):
    time.sleep(waitfor)
    pass
for i in tqdm(range(100), desc="Checking For Name..."):
    time.sleep(waitfor)
    pass
for i in tqdm(range(100), desc="Finalizing..."):
    time.sleep(waitfor*2)
    pass
start()

#Initialisation
#--------------

