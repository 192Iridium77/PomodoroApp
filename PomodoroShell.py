import time
import pygame
import sys

delay = 1  # 1 second delay

def pomodoro():
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
        elapsed = (currentTime - startTime) // 60
        remaining_minutes = "{:>2d}".format((setTimer * 60 - int(currentTime - startTime)) // 60)
        remaining_seconds = "{:02d}".format(((60 * setTimer) - int((currentTime - startTime))) % 60)

        # check for end condition
        if elapsed >= setTimer:
            end_sound.play()
            print("\nTimer Finished!")
            break

        # animate remaining time on commandline
        sys.stdout.write('\b' * 5)
        sys.stdout.write(remaining_minutes)
        sys.stdout.write(':')
        sys.stdout.write(remaining_seconds)
        sys.stdout.flush()

        time.sleep(delay)

    esc = input("press close to exit")


pomodoro()
