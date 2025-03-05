import customtkinter
from PIL import Image

dif_image = customtkinter.CTkImage(Image.open("images/2.jpg"),
                                   size=(600,500))

class DefaultPic(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.grid_columnconfigure(0,weight=0)
        self.grid_rowconfigure(0,weight=0)

        self.pic = customtkinter.CTkLabel(self,
                                          text="",
                                          image=dif_image
                                          )
        self.pic.grid(column=0,row=0,sticky="nsew")