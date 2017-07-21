from tkinter import *
import time
import pygame

class PomodoroCanvas:
    def __init__(self):
        self.radius = 80
        self.canvas_width = 300
        self.canvas_height = 350
        self.center_x = int(self.canvas_width / 2)
        self.center_y = int(self.canvas_height / 2)

        self.window = Tk()
        self.window.title("Pomodoro0.4")
        frame1 = Frame(self.window)
        frame1.pack()
        self.canvas = Canvas(frame1, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # buttons
        frame2 = Frame(self.window)
        frame2.pack()
        self.slider = Scale(frame2, label="Set Timer: ", to=60, orient='horizontal', length=200,
                            tickinterval=10)
        self.bt_start = Button(frame2, text="Start", command=self.start)
        # bt_pause = Button(frame2, text="Pause", command=)
        # bt_resume = Button(frame2, text="Resume", command=)
        # bt_stop = Button(frame2, text="Stop", command=)

        self.slider.pack()
        self.bt_start.pack()

        self.window.mainloop()

    def start(self):
        setTimer = self.slider.get()
        pygame.mixer.init()
        try:
            start_sound = pygame.mixer.Sound("sounds/START.wav")
            end_sound = pygame.mixer.Sound("sounds/DING.wav")
        except:
            raise UserWarning("Sound file not found.")

        start_sound.play()
        startTime = time.time()

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
                break

            arc_extent = int(completion_ratio * 360)
            # animate remaining time
            self.canvas.delete("time")
            self.canvas.delete("arc")
            self.canvas.create_text(self.center_x - 5, self.center_y, text=time_text,
                                    font="Helvetica 20", tags="time")
            self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                                    self.center_x + self.radius, self.center_y + self.radius,
                                    width=5,
                                    outline="#f2f3f4", tags="clock")
            self.canvas.create_arc(self.center_x - self.radius, self.center_y - self.radius,
                                   self.center_x + self.radius, self.center_y + self.radius,
                                   start=90, extent=arc_extent, width=5,
                                   style=ARC, outline="#17a589", tags="arc")
            self.canvas.after(1000)
            self.canvas.update()

            self.window.update()
            self.window.update_idletasks()

PomodoroCanvas()