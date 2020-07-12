from tkinter import *
from fucoes import *


#criando a tela principal
screen = Tk()
altura = 600
largura = 800
#centralizando a tela
largura_screen = screen.winfo_screenwidth()
altura_screen = screen.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

screen.geometry('%dx%d+%d+%d'%(largura, altura, posx, posy))




screen.mainloop()