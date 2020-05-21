import pygame
import pygame_gui
from newClip import clip
from export import render
import threading
from threading import Thread
from ClipClass import Clip as c
from os import walk

clips = []


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


# gets the videos already in the current video file and makes clip classes for them
for (dirpath, dirnames, filenames) in walk('../currentVideos/'):
    print("hello")
    for file in filenames:
        print(file)
        clips.append(c("../currentVideos/" + file))

pygame.init()

pygame.display.set_caption('Video Editor')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

import_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 100), (100, 50)),
                                             text='Import',
                                             manager=manager)

export_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 100), (100, 50)),
                                             text='Export',
                                             manager=manager)

export_button.unfocus()
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0

    # events
    for event in pygame.event.get():
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

    manager.update(time_delta)

    # drawing, order from bottom to top
    window_surface.blit(background, (0, 0))
    pygame.draw.line(window_surface, (255, 255, 255), (1, 1), (799, 599), 10)
    manager.draw_ui(window_surface)

    pygame.display.update()