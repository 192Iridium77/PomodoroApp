import time
import pygame
from tkinter import *

delay = 1  # 1 second delay

# while True:
#     localTime = time.localtime()
#     # print("{:02d}:{:02d}:{:02d}".format(localTime[3], localTime[4], localTime[5]))
#     print("%02d:%02d:%02d" % (localTime[3], localTime[4], localTime[5]))
#     time.sleep(delay)

class Pomodoro:
    # constructor
    def __init__(self, running=False, paused=False, stopped=True, set=0, start_time=0, sounds=[]):
        self.__running = running
        self.__paused = paused
        self.__stopped = stopped
        self.__set = set
        self.__start_time = start_time
        self.__sounds = sounds

    def setStartTime(self):
        self.__start_time = time.time()
        self.toggleRunning()

    def toggleRunning(self):
        if not self.__running:
            self.__running = True
        else:
            self.__running = False

    def togglePaused(self):
        if not self.__paused:
            self.__paused = True
        else:
            self.__paused = False

    def toggleStopped(self):
        if not self.__stopped:
            self.__stopped = True
        else:
            self.__stopped = False

    def loadSounds(self):
        try:
            self.__sounds.add(pygame.mixer.Sound("sounds/START.wav"))
            self.__sounds.add(pygame.mixer.Sound("sounds/DING.wav"))
            # TODO make it so you can add custom sounds to a list
        except:
            raise UserWarning("Sound file could not be played")
            # TODO make this a popup error

    def operateTimer(self):
        while self.__running:
            currentTime = time.time()
            if (currentTime - self.__startTime) > (self.__set * 60):
                break
            time.sleep(delay)

        print("Timer Finished!")
        finishSound(self.__sounds)

    def startSound(sound_list):
        sound_list[0].play()

    def finishSound(sound_list):
        sound_list[1].play()

def displayPomodoro(pomodoro):
    window = Tk()
    label = Label(window, text="Pomodoro")
    canvas = Canvas(window, bg = "white", width = 200, height = 200)
    slide_input = Scale(window, from_=0, to=60, orient='horizontal')
    bt_start = Button(window, text="Start", command=pomodoro.setStartTime())
    bt_pause = Button(window, text="Pause", command=pomodoro.togglePaused())
    bt_stop = Button(window, text="Stop", command=pomodoro.toggleStopped())

    label.pack()
    canvas.pack()
    slide_input.pack()
    bt_start.pack()
    bt_stop.pack()

def main():


    startTime = time.time()
    p = Pomodoro()
    displayPomodoro(p)

    pygame.mixer.init()

    sounds = loadSoundObjects()
    startSound(sounds)

    operateTimer(startTime, setTime, sounds)

    window.mainloop()

main()