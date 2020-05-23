import pygame
import pygame_gui
from newClip import clip
from export import render
import threading
from threading import Thread
from ClipClass import Clip as c
from os import walk
import os

clips = []
totalD = 0


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


# checks if  currentVideos and finalVideos are there and if not creates them
folders = ['../currentVideos', '../finalVideos']
for folder in folders:
    if not os.path.isdir(folder):
        os.mkdir(folder)

# gets the videos already in the current video file and makes clip classes for them
for (dirpath, dirnames, filenames) in walk('../currentVideos/'):
    print("hello")
    for file in filenames:
        print(file)
        clips.append(c("../currentVideos/" + file))

for clip in clips:
    totalD += clip.video.duration

# init of all the window and the background
pygame.init()
pygame.display.set_caption('Video Editor')
window_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((800, 600))

# init for text
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# setting of the buttons in memory
import_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 100), (100, 50)),
                                             text='Import',
                                             manager=manager)

export_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 100), (100, 50)),
                                             text='Export',
                                             manager=manager)

buttons = []
durationPointerOld = 100
durationPointerNew = 100
for clip in clips:
    x = clip.video.duration
    durationPointerNew += (x / totalD) * 600
    print(durationPointerOld, durationPointerNew, x, x / totalD, clip.video.filename.split("/")[-1])
    buttons.append(
        pygame_gui.elements.UIButton(relative_rect=pygame.Rect((durationPointerOld, 400), (durationPointerNew, 430)),
                                     text=clip.video.filename.split("/")[-1],
                                     manager=manager))
    durationPointerOld = durationPointerNew

    is_running = True

    # event handler


def event_handler(events):
    global is_running
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == import_button:
                    clipT = ThreadWithReturnValue(target=clip)
                    clipT.start()
                    try:
                        clips.append(c(clipT.join()))
                    except AttributeError:
                        pass
                elif event.ui_element == export_button:
                    clipT = threading.Thread(target=render, args=(clips, "hello"))
                    clipT.start()
                    clipT.join()
        manager.process_events(event)


def process():
    global textsurface
    totalDuration = 0
    for video in clips:
        totalDuration += video.video.duration
    seconds = round(totalDuration % 60)
    minutes = round(totalDuration / 60)
    textsurface = myfont.render(str(minutes) + ":" + (str(seconds) if len(str(seconds)) == 2 else "0" + str(seconds)),
                                False, (255, 255, 255))


def drawer():
    # drawing, order from bottom to top
    window_surface.blit(background, (0, 0))
    window_surface.blit(textsurface, (700, 300))
    pygame.draw.line(window_surface, (255, 255, 255), (100, 500), (700, 500), 10)

    manager.draw_ui(window_surface)
    pygame.display.update()


clock = pygame.time.Clock()

while is_running:
    time_delta = clock.tick(60) / 1000.0
    event_handler(pygame.event.get())
    process()
    manager.update(time_delta)
    drawer()
