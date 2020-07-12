from tkinter import *


#criando botao
def botao(parent, texto, row_ = 0, column_ = 0):
    bt = Button(parent,text= texto,)
    bt.grid(row = row_, column= column_ )
