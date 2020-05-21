from moviepy.editor import *


def render(videos, name):
    L = []
    print(videos)
    for video in videos:
        L.append(video.render())
    print(L)
    final_clip = [CompositeVideoClip(L)]
    concatenate_videoclips(final_clip, padding=-1).write_videofile(
        "..\\finalVideos\\%s.mp4" % name,
        remove_temp=True, threads=4)


if __name__ == "__main__":
    from ClipClass import Clip

    # both of these work
    """final_clip = [CompositeVideoClip([VideoFileClip('../finalVideos/clip1.mp4')])]
    concatenate_videoclips(final_clip, padding=-1).write_videofile(
        "..\\finalVideos\\%s.mp4" % "name",
        remove_temp=True, threads=4)"""
    # this one to
    render([Clip('../finalVideos/clip1.mp4')], "hello")