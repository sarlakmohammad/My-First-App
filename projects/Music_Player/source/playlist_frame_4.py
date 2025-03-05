import os
from tkinter.messagebox import showerror
import customtkinter
from CTkListbox import *
from PIL import Image
from tkinter.filedialog import askopenfilename
import shutil

image1 = customtkinter.CTkImage(Image.open("images/list.psd"),size=(75,75))
image2 = customtkinter.CTkImage(Image.open("images/remove_list.psd"),size=(75,75))

class PlaylistFrame(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.file_list = []
        self.musicpath = "null"

        self.grid_columnconfigure((0,1),weight=0)
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(1,weight=0)
        self.grid_rowconfigure(2,weight=3)
        self.grid_rowconfigure(3,weight=2)

        self.name = customtkinter.CTkLabel(self,
                                           text="Shadow Music",
                                           text_color="white",
                                           font=customtkinter.CTkFont(family="Arial", weight="bold", size=30),

                                           )
        self.name.grid(column=0, row=0,columnspan=2,padx=(50,0),pady=(20,0))

        self.name2 = customtkinter.CTkLabel(self,
                                           text="Playlist",
                                           width=100,
                                           fg_color="#061529",
                                           text_color="white",
                                           font=customtkinter.CTkFont(family="Arial", weight="bold", size=20),
                                           corner_radius=1
                                           )
        self.name2.grid(column=0, row=1,columnspan=2,padx=(50,0),pady=(60,0))

        self.playlist = CTkListbox(self,
                               fg_color="white",
                               width=300,
                               height=400,
                               text_color="black",
                               # multiple_selection=True,
                               highlight_color="#0799BD",
                               hover_color='#066B84'
                               )
        self.playlist.grid(column=0, row=2,columnspan=2,padx=(36,0),pady=(0,10))

        self.but1 = customtkinter.CTkButton(self,
                                            text="",
                                            command=self.add_music,
                                            image=image1,
                                            width=75,
                                            height=75,
                                            fg_color="transparent",
                                            hover_color="#06A4FF"
                                            )
        self.but1.grid(column=0, row=3, sticky="nsew", padx=(40, 0))

        self.but2 = customtkinter.CTkButton(self,
                                            text="",
                                            command=self.remove_music,
                                            image=image2,
                                            width=75,
                                            height=75,
                                            fg_color="transparent",
                                            hover_color="#06A4FF"
                                            )
        self.but2.grid(column=1, row=3, sticky="nsew", padx=(139, 0))

        self.show()

    def show(self):
        self.playlist.delete(0,'end')
        self.file_list = os.listdir("music")
        for music in self.file_list:
            self.playlist.insert("end",music)

    def add_music(self):
        try:
            self.musicpath = askopenfilename(title="choose a song",
                                        filetypes=(("Mp3 Songs", "*.mp3"),)
                                        )
            if not self.musicpath in self.file_list:
                shutil.copy(self.musicpath, "music")
            self.show()
        except FileNotFoundError:
            pass

    def remove_music(self):
        try:
            index = self.playlist.curselection()
            musicname = self.playlist.get(index)
            os.remove(f'music/{musicname}')
            self.show()
        except FileNotFoundError:
            showerror("no file selected !","please select a file first")