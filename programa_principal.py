from tkinter import *
from fucoes import Login
from fucoes import Math



#Iniciando a tela principal
screen = Tk()

#Propriedades da tela
altura = 600
largura = 800
titulo = 'Login'
icone = 'imagens/aranha.ico'
screen.resizable (False, False)


#Centralizando a Tela
tela_x = Math.Centerx(screen, largura)
tela_y = Math.Centery(screen, altura)

#Programação da Tela
screen.geometry('%dx%d+%d+%d'%(largura, altura, tela_x, tela_y))
screen.title(titulo)
screen.iconbitmap(icone)
screen['bg'] = 'gray'

#Adicionando Widgets
login = Login.Login(screen)
screen.mainloop()