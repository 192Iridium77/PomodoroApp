import time
import pygame

delay = 1

class Pomodoro:
    # constructor
    def __init__(self, running, paused, resumed, stopped, set):
        self.__running = running
        self.__paused = paused
        self.__resumed = resumed
        self.__stopped = stopped
        self.__set = set

    def isRunning(self):
        print(self.__running)
        return self.__running

    def isStopped(self):
        print(self.__stopped)
        return self.__stopped

    def toggleStart(self):
        if not self.__running:
            self.__running = True
            print("running:", self.__running)
        else:
            self.__running = False
            print("running:", self.__running)

    def togglePause(self):
        if not self.__paused:
            self.__paused = True
            print("paused:", self.__paused)
        else:
            self.__paused = False
            print("paused:", self.__paused)

    def toggleResume(self):
        if not self.__resumed:
            self.__resumed = True
            print("resumed:", self.__resumed)
        else:
            self.__resumed = False
            print("resumed:", self.__resumed)

    def toggleStop(self):
        if not self.__stopped:
            self.__stopped = True
            print("stopped:", self.__stopped)
        else:
            self.__stopped = False
            print("stopped:", self.__stopped)

    # def loadSounds(self):
    #     try:
    #         self.__sounds.add(pygame.mixer.Sound("sounds/START.wav"))
    #         self.__sounds.add(pygame.mixer.Sound("sounds/DING.wav"))
    #         # TODO make it so you can add custom sounds to a list
    #     except:
    #         raise UserWarning("Sound file could not be played")
    #         # TODO make this a popup error
    #
    # def startSound(sound_list):
    #     sound_list[0].play()
    #
    # def finishSound(sound_list):
    #     sound_list[1].play()