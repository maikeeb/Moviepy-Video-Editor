from tkinter import filedialog
from tkinter import *
import shutil


def clip():
    root = Tk()
    root.filename = ""
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))
    file = root.filename
    root.destroy()
    # return root.filename
    if root.filename != "":
        shutil.move(file, "../currentVideos/" + file.split("/")[-1])
        return "../currentVideos/" + file.split("/")[-1]
    else:
        print("No file selected")


if __name__ == "__main__":
    clip()
