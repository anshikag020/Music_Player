from tkinter import *
import pygame
import os
import random

root = Tk()
root.title("Music Player")
root.geometry("500x300")

pygame.mixer.init()
count=0
songs =[]
history=[]
current_song = ""
paused = False
song_count=0


def load_music():
    root.directory = "audioFiles"

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)

load_music()
random.shuffle(songs)
def play_music():
    global current_song, paused,song_count,count
    current_song=songs[count]
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory,current_song))
        history.append(current_song)
        song_count+=1
        pygame.mixer.music.play()
        
    else:
        pygame.mixer.music.unpause()
        paused=False


def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused=True

def next_music():
    global current_song,paused,count,song_count
    pygame.mixer.music.pause()
    count+=1
    if count == 20:
        count=0
        random.shuffle(songs)
    paused=True
    current_song=songs[count]
    pygame.mixer.music.load(os.path.join(root.directory,current_song))
    history.append(current_song)
    song_count+=1
    pygame.mixer.music.play()

def prev_music():
    global current_song,song_count
    pygame.mixer.music.pause()
    paused=True
    if song_count ==1:
        pygame.mixer.music.load(os.path.join(root.directory,current_song))
        pygame.mixer.music.play()

    else:
        song_count-=1
        pygame.mixer.music.load(os.path.join(root.directory,history[song_count-1]))
        pygame.mixer.music.play()

songlist = Listbox(root, bg="grey", fg="white", width=100, height=12)
songlist.pack()

play_btn_img = PhotoImage(file="images/play.png")
pause_btn_img = PhotoImage(file="images/pause.png")
next_btn_img = PhotoImage(file="images/next.png")
prev_btn_img = PhotoImage(file="images/previous.png")

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image = play_btn_img, borderwidth=0,command=play_music)
pause_btn = Button(control_frame, image = pause_btn_img, borderwidth=0,command=pause_music)
next_btn = Button(control_frame, image = next_btn_img, borderwidth=0,command=next_music)
prev_btn = Button(control_frame, image = prev_btn_img, borderwidth=0,command=prev_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)


root.mainloop()
