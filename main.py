# created by Jonas Schmidt on 6/8/2022
# "pygame clock demonstration"

import pygame
import math
import datetime
import sys

SCREEN_WIDTH = 270
SCREEN_HEIGHT = 270
centerScreen = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# multipliers to calculate positions based on trigonometry functions, both static
multMinSec = (2 * math.pi) / 60
multHour = (2 * math.pi) / 12

tickClock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)  # determine these arguments
pygame.display.set_caption("Clock")

icon = pygame.image.load("images/win_icon.png")
# load clock face
# should be a 270 x 270 image with current settings
face = pygame.image.load("images/clockFace.jpeg").convert()

pygame.display.set_icon(icon)


# determine if window is closed
def handle_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


# determine terminal position of the hour hand line from center of the screen from center screen
#then, draw the line
def drawHourHand(hour):
    hourHand_x = (SCREEN_WIDTH / 2) + (math.cos((hour * multHour) - (0.5 * math.pi)) * (SCREEN_WIDTH / 3))
    hourHand_y = (SCREEN_WIDTH / 2) + (math.sin((hour * multHour) - (0.5 * math.pi)) * (SCREEN_WIDTH / 3))

    pygame.draw.line(screen, (0, 255, 0), centerScreen, (hourHand_x, hourHand_y), width=4)


# determine terminal position of the minute hand line from center of the screen from center screen
#then, draw the line
def drawMinuteHand(minute):
    minHand_x = (SCREEN_WIDTH / 2) + (math.cos((minute * multMinSec) - (0.5 * math.pi)) * (SCREEN_WIDTH / 2))
    minHand_y = (SCREEN_WIDTH / 2) + (math.sin((minute * multMinSec) - (0.5 * math.pi)) * (SCREEN_WIDTH / 2))

    pygame.draw.line(screen, (0, 0, 255), centerScreen, (minHand_x, minHand_y), width=4)


# determine terminal position of the second hand line from center of the screen from center screen
#then, draw the line
def drawSecondHand(second):
    secHand_x = (SCREEN_WIDTH / 2) + (math.cos((second * multMinSec) - (0.5 * math.pi)) * (SCREEN_WIDTH / 2))
    secHand_y = (SCREEN_WIDTH / 2) + (math.sin((second * multMinSec) - (0.5 * math.pi)) * (SCREEN_WIDTH / 2))

    pygame.draw.line(screen, (255, 0, 0), centerScreen, (secHand_x, secHand_y), width=1)


def main():
    pygame.init()
    clockSpeed = 30

    # run while window is not closed
    while handle_quit():
        tickClock.tick(clockSpeed)

        # display clock face
        screen.blit(face, (0, 0))

        # determine current time ...
        currentTime = datetime.datetime.now()

        second = int(currentTime.strftime("%S"))

        minute = int(currentTime.strftime("%M"))
        minute = minute + (second / 60)

        hour = int(currentTime.strftime("%H"))
        hour = hour + (minute / 60)
        # ...

        # draw hands
        drawMinuteHand(minute)
        drawHourHand(hour)
        drawSecondHand(second)

        pygame.display.update()

    pygame.quit()
    sys.exit()


main()
