from moviepy.editor import *


class Clip:
    def __init__(self, filepath):
        self.video = VideoFileClip(filepath)
        self.video.size = (1920, 1080)
        self.composite_list = [self.video]

    def fadein(self):
        self.video = self.video.fadein(0.5)
        self.composite_list[0] = self.composite_list[0].fadein(0.5)

    def fadeout(self):
        self.video = self.video.fadeout(0.5)
        self.composite_list[0] = self.composite_list[0].fadeout(0.5)

    def text_overlay(self, input_text, posx, posy):
        text = TextClip(input_text, color='white', bg_color='red', method='label',
                        fontsize=50).set_duration(3).set_position((posx, posy))
        self.composite_list.append(text)

    def render(self):
        print(len(self.composite_list))
        if len(self.composite_list) > 1:
            return CompositeVideoClip(self.composite_list)
        else:
            return self.video


# https://stackoverflow.com/questions/35067777/moviepy-create-multiple-subclips-using-times-from-csv-file
# learn how make subclips and a second layer for edits that aren't attached to one video


if __name__ == "__main__":
    from export import render

    a = Clip('../currentVideos/out.mp4')
    b = Clip('../currentVideos/out.mp4')
    a.text_overlay("hello", 10, 10)
    render([a, b], "hello")
