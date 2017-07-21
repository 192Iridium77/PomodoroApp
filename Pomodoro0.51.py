from tkinter import *
import datetime
import pygame

class PomodoroCanvas:
    def __init__(self):
        self.radius = 80
        self.canvas_width = 300
        self.canvas_height = 350
        self.center_x = int(self.canvas_width / 2)
        self.center_y = int(self.canvas_height / 2)

        # initialize datetime objects for animate function
        self.elapsed = datetime.datetime.now()
        self.delta = datetime.datetime.now()

        self.window = Tk()
        self.window.title("Pomodoro0.51")
        frame1 = Frame(self.window)
        frame1.pack()
        self.canvas = Canvas(frame1, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # buttons
        frame2 = Frame(self.window)
        frame2.pack()
        self.slider = Scale(frame2, label="Set Timer: ",from_=1, to=60, orient='horizontal', length=200,
                            tickinterval=10)
        self.bt_start = Button(frame2, text="Start", command=self.start)
        self.bt_pause = Button(frame2, text="Pause", command=self.pause)
        self.bt_resume = Button(frame2, text="Resume", command=self.resume)
        # bt_stop = Button(frame2, text="Stop", command=)

        self.slider.grid(row=1, column=1, columnspan=3)
        self.bt_start.grid(row=2, column=1)
        self.bt_pause.grid(row=2, column=2)
        self.bt_resume.grid(row=2, column=3)

        self.running = False
        self.begin = False

        # default display
        self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                                self.center_x + self.radius, self.center_y + self.radius,
                                width=5,
                                outline="#f2f3f4", tags="clock")

        self.window.mainloop()

    def start(self):
        self.running = True
        self.begin = True
        self.animate()

    def pause(self):
        self.running = False

    def resume(self):
        self.running = True
        print(self.running)
        self.animate()


    def animate(self):
        pygame.mixer.init()
        try:
            start_sound = pygame.mixer.Sound("sounds/START.wav")
            end_sound = pygame.mixer.Sound("sounds/DING.wav")
        except:
            raise UserWarning("Sound file not found.")
        start_sound.play()

        # when the start button is pressed, the slider must be read
        if self.begin:
            self.setTimer = self.slider.get() * 60
            self.begin = False
            startTime = datetime.datetime.now()
        # after pausing, the pomodoro must reanimate from the previous time
        else:
            startTime = self.delta - self.elapsed

        while self.running:
            currentTime = datetime.datetime.now()
            self.elapsed = currentTime - startTime  # note that self.elapsed now becomes a delta
            self.delta = datetime.timedelta(seconds=self.setTimer)
            remaining_minutes = "{:>2d}".format((self.delta.seconds - self.elapsed.seconds) // 60)
            remaining_seconds = "{:02d}".format((self.delta.seconds - self.elapsed.seconds) % 60)
            time_text = remaining_minutes + ":" + remaining_seconds

            completion_ratio = self.elapsed.seconds / (self.setTimer)

            # check for end condition
            if self.delta.seconds - self.elapsed.seconds == -1:
                end_sound.play()
                break

            arc_extent = int(completion_ratio * 360)

            # animate remaining time
            self.canvas.delete("time")
            self.canvas.delete("arc")
            self.canvas.create_text(self.center_x - 5, self.center_y + 5, text=time_text,
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

PomodoroCanvas()