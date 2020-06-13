from tkinter import filedialog
from tkinter import *
import shutil
from time import sleep
import os


def newclip():
    root = Tk()
    root.filename = ""
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))
    file = root.filename
    root.destroy()
    # return root.filename
    if root.filename != "":
        shutil.move(file, "../currentVideos/" + file.split("/")[-1])
        while not os.path.exists("../currentVideos/" + file.split("/")[-1]):
            sleep(1)
        return "../currentVideos/" + file.split("/")[-1]
    else:
        print("No file selected")


if __name__ == "__main__":
    newclip()
