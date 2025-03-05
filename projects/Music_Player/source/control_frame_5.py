import customtkinter
from PIL import Image

image1 = customtkinter.CTkImage(Image.open("images/stop.psd"),
                                size=(66,66))
image2 = customtkinter.CTkImage(Image.open("images/befor.psd"),
                                size=(125,125))
image3 = customtkinter.CTkImage(Image.open("images/play.psd"),
                                size=(137,137))
image4 = customtkinter.CTkImage(Image.open("images/next.psd"),
                                size=(125,125))
image5 = customtkinter.CTkImage(Image.open("images/loop.psd"),
                                size=(66,66))

class ControlFrame(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.grid_rowconfigure(0,weight=0)

        self.grid_columnconfigure((0,4),weight=1)
        self.grid_columnconfigure((1,3),weight=2)
        self.grid_columnconfigure(2,weight=3)

        self.but1 = customtkinter.CTkButton(self,
                                            text="",
                                            # command=,
                                            image=image1,
                                            width=66,
                                            height=66,
                                            fg_color="transparent",
                                            hover_color="#06A4FF"
        )
        self.but1.grid(column=0,row=0, pady=(6,0))

        self.but2 = customtkinter.CTkButton(self,
                                            text="",
                                            # command=
                                            image=image2,
                                            width=125,
                                            height=125,
                                            fg_color="transparent",
                                            hover_color="#06A4FF"
                                            )
        self.but2.grid(column=1, row=0, pady=(6,0))

        self.but3 = customtkinter.CTkButton(self,
                                            text="",
                                            # command=
                                            image=image3,
                                            width=137,
                                            height=137,
                                            fg_color="transparent",
                                            hover_color="#06A4FF"
                                            )
        self.but3.grid(column=2, row=0, pady=(6,0))

        self.but4 = customtkinter.CTkButton(self,
                                            text="",
                                            # command=,
                                            image=image4,
                                            width=125,
                                            height=125,
                                            fg_color="transparent",
                                            hover_color="#06A4FF"
                                            )
        self.but4.grid(column=3, row=0, pady=(6,0))

        self.but5 = customtkinter.CTkButton(self,
                                            text="",
                                            # command=
                                            image=image5,
                                            width=66,
                                            height=66,
                                            fg_color="transparent",
                                            hover_color="#06A4FF",
                                            state='disabled'
                                            )
        self.but5.grid(column=4, row=0, pady=(6,0))

    def change_func1(self,func):
        self.but4.configure(command=func)

    def change_func2(self,func):
        self.but3.configure(command=func)

    def change_func3(self,func):
        self.but2.configure(command=func)

    def change_func4(self,func):
        self.but1.configure(command=func)