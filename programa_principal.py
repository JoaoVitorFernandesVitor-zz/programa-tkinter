from tkinter import *
from fucoes import *



#Iniciando a tela principal
screen = Tk()

#Propriedades da tela
altura = 600
largura = 800
titulo = 'Login'
icone = ''

#centralizando a tela
largura_screen = screen.winfo_screenwidth()
altura_screen = screen.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#Programação da Tela
screen.geometry('%dx%d+%d+%d'%(largura, altura, posx, posy))
screen.title(titulo)
#screen.icon= icone

#Adicionando Widgets
b1 = Botao(screen,'Entrar')
e1 = MinhaEntry(screen, )
l2 = label(screen, 'Senha')

l2['text'] = 'fon'


screen.mainloop()