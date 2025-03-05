import customtkinter
from customtkinter import CTkSlider
import music_tag


class TimeSlider(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure((0,1,4,5),weight=1)
        self.grid_columnconfigure((3,4), weight=3)

        self.slider = CTkSlider(self,
                                button_color='#05484A',
                                button_hover_color='#032D2F',
                                progress_color='#008084',
                                fg_color="white",
                                height=22,
                                width=300,
                                from_=0,
                                to=100,
                                state="disabled"
                                )
        self.slider.grid(column=1,row=0,sticky="ew",columnspan=4)

        self.time1 = customtkinter.CTkLabel(self,
                                            text="00:00",
                                            font=customtkinter.CTkFont(
                                                family="Verdana",
                                                size=20
                                            ),
                                            text_color='black'
                                            )
        self.time1.grid(column=0,row=0,padx=(10,0))

        self.time2 = customtkinter.CTkLabel(self,
                                            text="00:00",
                                            font=customtkinter.CTkFont(
                                                family="Verdana",
                                                size=20
                                            ),
                                            text_color='black'
                                            )
        self.time2.grid(column=5, row=0,padx=(0,10))