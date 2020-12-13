from moviepy.editor import *


def render(videos, name):
    L = [video.render() for video in videos]
    composite = [CompositeVideoClip(L)]
    try:
        concatenate_videoclips(composite, padding=-1).write_videofile(
            "..\\finalVideos\\%s.mp4" % name, codec='h264',
            remove_temp=True, threads=4)
    # known issue: increasing threads above 4 slows rendering
    except Exception as e:
        print("You don't have a nvidia graphics card")
        concatenate_videoclips(composite, padding=-1).write_videofile(
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
    render([Clip('../currentVideos/40hiko0.mp4')], "hello")
