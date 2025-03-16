#Copyright (c) 2025 @sarlakmohammad
    #All rights reserved
from time import *
import mutagen
from customtkinter import *
from control_frame_5 import ControlFrame
from time_frame_8 import TimeSlider
from volume_frame_6 import VolumeFrame
from playlist_frame_4 import PlaylistFrame
from default_pic_2 import DefaultPic
import music_tag
from PIL import Image
import pygame
from tkinter.messagebox import showerror

# window_panel
window = CTk()
window.title("Shadow Music")
window.iconbitmap('icon/1.ico')

window.minsize(1200, 760)
window.geometry("1200x770+0+0")
window.maxsize(1200, 793)
pygame.mixer.init()

# variables
default_pic = CTkImage(Image.open('images/2.jpg'), size=(600, 500))
play_pic = CTkImage(Image.open("images/play.psd"), size=(137, 137))
pause_pic = CTkImage(Image.open("images/pause.psd"), size=(137, 137))
playing_key = BooleanVar(value=False)
pause_key = BooleanVar(value=False)
position_slider_var = IntVar(value=0)
real_time = IntVar(value=0)
end_time_music = IntVar(value=0)
index = 0

# functions
def next_music():
    playing_key.set(False)
    pause_key.set(False)
    try:
        frame4.playlist.activate(index + 1)
    except IndexError:
        frame4.playlist.activate(0)
    finally:
        play_pause_music()


def previous_music():
    playing_key.set(False)
    pause_key.set(False)
    frame4.playlist.activate(index - 1)
    play_pause_music()


def play_pause_music():
    global index
    index = frame4.playlist.curselection()
    if not playing_key.get():
        try:
            frame8.slider.configure(state="normal")
            real_time.set(0)
            playing_key.set(True)
            music_name = frame4.playlist.get(index)
            mp3 = music_tag.load_file(f'music/{music_name}')
            frame5.but3.configure(image=pause_pic)
            try:
                music_artwork = mp3['artwork'].first.data
                with open('artwork/image.jpg', 'wb') as file:
                    file.write(music_artwork)
                frame2.pic.configure(image=CTkImage(Image.open('artwork/image.jpg'), size=(600, 500)))
            except AttributeError:
                frame2.pic.configure(image=default_pic)
            pygame.mixer_music.load(f'music/{music_name}')
            get_end_time()
            get_current_time()
            pygame.mixer_music.play()
        except mutagen.MutagenError:
            showerror('music', 'please select a music first')

    elif playing_key.get() and (not pause_key.get()):
        pause_key.set(True)
        frame5.but3.configure(image=play_pic)
        pygame.mixer_music.pause()

    elif playing_key.get() and pause_key.get():
        pause_key.set(False)
        frame5.but3.configure(image=pause_pic)
        pygame.mixer_music.unpause()


def stop_music():
    frame4.playlist.deselect(index)
    pygame.mixer_music.stop()
    frame8.slider.configure(state="disabled")
    frame8.time2.configure(text="00:00")
    frame2.pic.configure(image=default_pic)
    frame5.but3.configure(image=play_pic)
    playing_key.set(False)


def get_current_time():
    _current_time = real_time.get() + int((pygame.mixer_music.get_pos() + 1)/1000)
    _convert_time = strftime('%M:%S',gmtime(_current_time))

    frame8.time1.configure(text=_convert_time)
    position_slider_var.set(_current_time)
    if end_time_music.get() == _current_time+1 or end_time_music.get() == _current_time:
        stop_music()
        if index + 1 < frame4.playlist.size():
            frame4.playlist.activate(index + 1)
            play_pause_music()
        else:
            frame4.playlist.activate(0)
            play_pause_music()
        real_time.set(0)
    frame8.time1.after(1000,get_current_time)


def get_end_time():
    _music = frame4.playlist.get(index)
    _mp3 = music_tag.load_file(f'music/{_music}')
    _end_time = int(_mp3["#length"])
    _convert_time = strftime("%M:%S",gmtime(_end_time))

    end_time_music.set(_end_time)
    frame8.slider.configure(to=_end_time)
    frame8.time2.configure(text=_convert_time)


def change_slider(value):
    _music = frame4.playlist.get(index)
    pygame.mixer_music.load(f'music/{_music}')
    pygame.mixer_music.play(start=value)
    real_time.set(value=value)
    pause_key.set(False)
    frame5.but3.configure(image=pause_pic)
    get_current_time()


def change_volume(value):
    pygame.mixer_music.set_volume(value)


def event2(event):
    playing_key.set(False)
    pause_key.set(False)
    play_pause_music()


def volume_change(event):
    _volume = frame6.slider.get()
    if event.delta == 120:
        frame6.slider.configure(variable=DoubleVar(value=_volume + 0.1))
        pygame.mixer_music.set_volume(_volume + 0.1)
    elif event.delta == -120:
        frame6.slider.configure(variable=DoubleVar(value=_volume - 0.1))
        pygame.mixer_music.set_volume(_volume - 0.1)


# def upp_select(event):
#     _index = frame4.playlist.curselection()
#     if _index:
#         if _index > 0:
#             frame4.playlist.activate(index - 1)
#         else:
#             frame4.playlist.activate(frame4.playlist.size())
#
#
# def down_select(event):
#     _index = frame4.playlist.curselection()
#     if _index:
#         if _index < frame4.playlist.size():
#             frame4.playlist.activate(index + 1)
#         else:
#             frame4.playlist.activate(0)

# frame
########################################################  row 0

frame1 = CTkFrame(window, fg_color="#b2ced0", width=100, height=500)
frame1.grid(column=0, row=0, sticky='nsew', rowspan=3)

############################################DefaultPic
frame2 = DefaultPic(window, fg_color="transparent", width=600, height=500)
frame2.grid(column=1, row=0, sticky='nsew')

frame3 = CTkFrame(window, fg_color="#b2ced0", width=100, height=500)
frame3.grid(column=2, row=0, sticky='nsew')

############################################PlaylistFrame
frame4 = PlaylistFrame(window, fg_color="#0f2b4e", width=400, height=500)
frame4.grid(column=3, row=0, sticky='nsew', rowspan=2)

########################################################  row 1

############################################ControlFrame
frame5 = ControlFrame(window,
                      bg_color="#72C4D4",
                      fg_color='#0e3c59',
                      corner_radius=50,
                      border_width=5,
                      border_color='#0e3c59',
                      width=600,
                      height=172
                      )
frame5.grid(column=1, row=1, sticky='nsew')

############################################VolumeFrame
frame6 = VolumeFrame(window, fg_color="#b2ced0", width=100, height=190)
frame6.grid(column=2, row=1, sticky='nsew', rowspan=2)

########################################################  row 2

############################################TimeSlider
frame8 = TimeSlider(window, fg_color="#72C4D4", width=600, height=121)
frame8.grid(column=1, row=2, sticky='nsew')

frame9 = CTkFrame(window, fg_color="#0f2b4e", width=400, height=121)
frame9.grid(column=3, row=2, sticky='nsew')

# vigets

# operate
window.grid_columnconfigure((0, 2), weight=3)
window.grid_columnconfigure(1, weight=15)
window.grid_columnconfigure(3, weight=10)

window.grid_rowconfigure(0, weight=10)
window.grid_rowconfigure(1, weight=3)
window.grid_rowconfigure(2, weight=1)

frame5.change_func1(next_music)
frame5.change_func2(play_pause_music)
frame5.change_func3(previous_music)
frame5.change_func4(stop_music)

window.bind('<Return>', event2)
window.bind('<Return>', real_time.set(0))
# window.bind('<Up>',upp_select)
# window.bind('<Down>',down_select)
# window.bind('<MouseWheel1>',func=volume_change)

frame8.slider.configure(variable=position_slider_var,command=change_slider)
frame6.slider.configure(command=change_volume)

window.mainloop()
