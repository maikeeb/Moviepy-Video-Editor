from tkinter import filedialog
from tkinter import *
import shutil


def clip():
    root = Tk()
    root.filename = ""
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))
    # return root.filename
    if root.filename != "":
        shutil.move(root.filename, "../currentVideos/" + root.filename.split("/")[-1])
        return "../currentVideos/" + root.filename.split("/")[-1]
    else:
        print("No file selected")


if __name__ == "__main__":
    clip()
