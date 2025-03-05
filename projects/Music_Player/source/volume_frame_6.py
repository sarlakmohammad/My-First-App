import customtkinter
from PIL import Image
import tkinter

image_up = customtkinter.CTkImage(Image.open("images/volume-up.png"))
image_down = customtkinter.CTkImage(Image.open("images/volume-down.png"))

class VolumeFrame(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,3), weight=1)
        self.grid_rowconfigure(2, weight=3)

        self.text = customtkinter.CTkLabel(self,
                                           text="volume:",
                                           text_color="black",
                                           font=customtkinter.CTkFont(family="Arial",weight="bold",size=20),
                                           anchor="s",
                                           compound="bottom"
        )
        self.text.grid(column=0, row=0,pady=15)

        self.volume_upp = customtkinter.CTkLabel(self,
                                                 text="",
                                                 image=image_up
                                                 )
        self.volume_upp.grid(column=0, row=1)

        self.slider = customtkinter.CTkSlider(self,
                                button_color='#04313c',
                                orientation="vertical",
                                button_hover_color='#031b21',
                                progress_color='#007694',
                                fg_color="white",
                                height=170,
                                from_=0,
                                to=1,
                                variable=tkinter.DoubleVar(value=1.0)
                                )
        self.slider.grid(column=0, row=2)

        self.volume_down = customtkinter.CTkLabel(self,
                                                 text="",
                                                 image=image_down
                                                 )
        self.volume_down.grid(column=0, row=3)