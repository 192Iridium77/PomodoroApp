from tkinter import *
import time
import pygame

class PomodoroCanvas:
    def __init__(self):
        window = Tk()
        window.title("Pomodoro0.3")
        self.canvas_width = 300
        self.canvas_height = 400
        self.canvas = Canvas(window, width=self.canvas_width, height=self.canvas_height,
                             bg="white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        self.displayTimer()

        window.mainloop()

    def displayTimer(self):
        center_x = int(self.canvas_width / 2)
        center_y = int(self.canvas_height / 2)
        RADIUS = 80

        pygame.mixer.init()
        try:
            start_sound = pygame.mixer.Sound("sounds/START.wav")
            end_sound = pygame.mixer.Sound("sounds/DING.wav")
        except:
            raise UserWarning("Sound file could not be played")

        setTimer = int(input("Enter number of minutes: "))
        startTime = time.time()

        start_sound.play()

        while True:
            currentTime = time.time()
            elapsed_seconds = int(currentTime - startTime)
            set_seconds = setTimer * 60
            remaining_minutes = "{:>2d}".format((set_seconds - elapsed_seconds) // 60)
            remaining_seconds = "{:02d}".format((set_seconds - elapsed_seconds) % 60)
            time_text = remaining_minutes + ":" + remaining_seconds

            completion_ratio = elapsed_seconds / (setTimer * 60)

            # check for end condition
            if set_seconds - elapsed_seconds == -1:
                end_sound.play()
                # self.wriggle()
                break

            arc_extent = int(completion_ratio * 360)
            # animate remaining time
            self.canvas.delete("time")
            self.canvas.delete("arc")
            self.canvas.create_text(center_x - 5, center_y, text=time_text,
                                    font="Helvetica 20", tags="time")
            self.canvas.create_oval(center_x - RADIUS, center_y - RADIUS,
                                   center_x + RADIUS, center_y + RADIUS,
                                    width=5,
                                    outline="#f2f3f4", tags="clock")
            self.canvas.create_arc(center_x - RADIUS, center_y - RADIUS,
                                   center_x + RADIUS, center_y + RADIUS,
                                   start=90, extent=arc_extent, width=5,
                                   style=ARC, outline="#17a589", tags="arc")
            self.canvas.after(1000)
            self.canvas.update()
    #
    # def wriggle(self):
    #

PomodoroCanvas()