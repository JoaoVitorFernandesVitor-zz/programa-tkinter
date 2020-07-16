from tkinter import *

#Class da tela principal do sistema
class Main(Frame):
    def __init__(self, parent,list):
        super().__init__()
        #propriedades do frame
        self['heigh'] = 600
        self['width'] = 800
        self['bg']    = "gray"
        texto = StringVar()
        texto.set(list)
        l = Label(self, textvariable = texto )
        l.grid()

        self.grid()