# Imports
from pygame import mixer
import time
import os, sys

# Loops the code
infinite_loop = 1

# Function to run audio
def play_song(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

#Realitive Paths
APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(APP_FOLDER)
full_path0 = os.path.join(APP_FOLDER, "12 AM.mp3")
full_path1 = os.path.join(APP_FOLDER, "1 AM.mp3")
full_path2 = os.path.join(APP_FOLDER, "2 AM.mp3")
full_path3 = os.path.join(APP_FOLDER, "3 AM.mp3")
full_path4 = os.path.join(APP_FOLDER, "4 AM.mp3")
full_path5 = os.path.join(APP_FOLDER, "5 AM.mp3")
full_path6 = os.path.join(APP_FOLDER, "6 AM.mp3")
full_path7 = os.path.join(APP_FOLDER, "7 AM.mp3")
full_path8 = os.path.join(APP_FOLDER, "8 AM.mp3")
full_path9 = os.path.join(APP_FOLDER, "9 AM.mp3")
full_path10 = os.path.join(APP_FOLDER, "10 AM.mp3")
full_path11 = os.path.join(APP_FOLDER, "11 AM.mp3")
full_path12 = os.path.join(APP_FOLDER, "12 PM.mp3")
full_path13 = os.path.join(APP_FOLDER, "1 PM.mp3")
full_path14 = os.path.join(APP_FOLDER, "2 PM.mp3")
full_path15 = os.path.join(APP_FOLDER, "3 PM.mp3")
full_path16 = os.path.join(APP_FOLDER, "4 PM.mp3")
full_path17 = os.path.join(APP_FOLDER, "5 PM.mp3")
full_path18 = os.path.join(APP_FOLDER, "6 PM.mp3")
full_path19 = os.path.join(APP_FOLDER, "7 PM.mp3")
full_path20 = os.path.join(APP_FOLDER, "8 PM.mp3")
full_path21 = os.path.join(APP_FOLDER, "9 PM.mp3")
full_path22 = os.path.join(APP_FOLDER, "10 PM.mp3")
full_path23 = os.path.join(APP_FOLDER, "11 PM.mp3")

print("")
print("Thanks for using my program, to stop the music simply close the terminal window")
print("This version will play the music from Animal Crossing: New Leaf")
print("All music is not owned by me, i just coded this program.")
print("Enjoy :)")

while infinite_loop == infinite_loop:
    # Gets local time
    t = time.localtime()
    current_time = time.strftime("%H", t)

    # Plays the appropriate song based of the local time (24 hour)
    if current_time == ("00"):
        play_song(full_path0)
        time.sleep(33.813)

    elif current_time == ("01"):
        play_song(full_path1)
        time.sleep(57.313)

    elif current_time == ("02"):
        play_song(full_path2)
        time.sleep(83.419)

    elif current_time == ("03"):
        play_song(full_path3)
        time.sleep(41.055)

    elif current_time == ("04"):
        play_song(full_path4)
        time.sleep(52.320)

    elif current_time == ("05"):
        play_song(full_path5)
        time.sleep(54.014)

    elif current_time == ("06"):
        play_song(full_path6)
        time.sleep(36.955)

    elif current_time == ("07"):
        play_song(full_path7)
        time.sleep(44.634)

    elif current_time == ("08"):
        play_song(full_path8)
        time.sleep(43.202)

    elif current_time == ("09"):
        play_song(full_path9)
        time.sleep(28.806)

    elif current_time == ("10"):
        play_song(full_path10)
        time.sleep(39.628)

    elif current_time == ("11"):
        play_song(full_path11)
        time.sleep(42.170)

    elif current_time == ("12"):
        play_song(full_path12)
        time.sleep(42.870)

    elif current_time == ("13"):
        play_song(full_path13)
        time.sleep(40.005)

    elif current_time == ("14"):
        play_song(full_path14)
        time.sleep(42.406)

    elif current_time == ("15"):
        play_song(full_path15)
        time.sleep(30.009)

    elif current_time == ("16"):
        play_song(full_path16)
        time.sleep(45.014)

    elif current_time == ("17"):
        play_song(full_path17)
        time.sleep(66.787)

    elif current_time == ("18"):
        play_song(full_path18)
        time.sleep(44.864)

    elif current_time == ("19"):
        play_song(full_path19)
        time.sleep(42.399)

    elif current_time == ("20"):
        play_song(full_path20)
        time.sleep(41.780)

    elif current_time == ("21"):
        play_song(full_path21)
        time.sleep(42.679)

    elif current_time == ("22"):
        play_song(full_path22)
        time.sleep(36.716)

    elif current_time == ("23"):
        play_song(full_path23)
        time.sleep(62.061)

    else:
        print("Time error, retrying in 5 seconds.")
        time.sleep(5)