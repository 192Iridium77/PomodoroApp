from tkinter import *
import time
import pygame
from PomodoroClass import Pomodoro


class PomodoroCanvas:
    def __init__(self):
        self.radius = 80
        self.canvas_width = 300
        self.canvas_height = 350
        self.center_x = int(self.canvas_width / 2)
        self.center_y = int(self.canvas_height / 2)

        window = Tk()
        window.title("Pomodoro0.4")
        frame1 = Frame(window)
        frame1.pack()
        self.canvas = Canvas(frame1, width=self.canvas_width, height=self.canvas_height,
                             bg="white")
        self.canvas.pack()

        p1 = Pomodoro(False, False, False, False, 0)

        # buttons
        frame2 = Frame(window)
        frame2.pack()
        slide_input = Scale(frame2, label="Set Timer: ", to=60, orient='horizontal')
        bt_start = Button(frame2, text="Start", command=p1.toggleStart)
        bt_pause = Button(frame2, text="Pause", command=p1.togglePause)
        bt_resume = Button(frame2, text="Resume", command=p1.toggleResume)
        bt_stop = Button(frame2, text="Stop", command=p1.toggleStop)

        slide_input.grid(row=1, column=1, columnspan=4)
        bt_start.grid(row=2, column=1)
        bt_pause.grid(row=2, column=2)
        bt_resume.grid(row=2, column=3)
        bt_stop.grid(row=2, column=4)

        window.update_idletasks()
        window.update()

        if p1.isRunning() is True:
            press = StringVar()
            bt_start['state'] = press
            press.set("state")

            self.displayTimer(window, p1, self.center_x, self.center_y, self.radius, slide_input.get())

        window.update_idletasks()
        window.update()

        end = input("End process? ")  # for debugging

    def displayTimer(self, window, pomodoro, center_x, center_y, RADIUS, setTimer):
        pygame.mixer.init()
        try:
            start_sound = pygame.mixer.Sound("sounds/START.wav")
            end_sound = pygame.mixer.Sound("sounds/DING.wav")
        except:
            raise UserWarning("Sound file not found.")

        startTime = time.time()

        start_sound.play()

        window.update_idletasks()

        while pomodoro.isRunning:
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
                self.wriggle(center_x, center_y, pomodoro)
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

            window.update_idletasks()

    def wriggle(self, x, y, pomodoro):
        while not pomodoro.isStopped:
            self.canvas.delete("time", "arc")
            dx = 1
            for i in range(6):
                self.canvas.create_text(x - dx, y, text="0:00", tags="time")
                self.canvas.delete("time")
                self.canvas.after(100)
                self.canvas.update()
            for i in range(12):
                self.canvas.create_text(x + dx, y, text="0:00", tags="time")
                self.canvas.delete("time")
                self.canvas.after(100)
                self.canvas.update()
            for i in range(6):
                self.canvas.create_text(x - dx, y, text="0:00", tags="time")
                self.canvas.delete("time")
                self.canvas.after(100)
                self.canvas.update()


PomodoroCanvas()