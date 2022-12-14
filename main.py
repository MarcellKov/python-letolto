from tkinter import *
from pytube import YouTube


root=Tk()
root.geometry("500x500")

felirat=Label(root,text="YouTube videó letöltő")
felirat.pack()

e=Entry(root)
e.pack()

def mp3():
    url=e.get()
    video=YouTube(url)
    x=video.streams.get_audio_only()
    x.download()

def mp4():
    url=e.get()
    video=YouTube(url)
    x=video.streams.get_highest_resolution()
    x.download()

gomb1=Button(root,text="MP3 letöltése", command=mp3)
gomb1.pack()
gomb2=Button(root,text="MP4 letöltése",command=mp4)
gomb2.pack()



root.mainloop()