from tkinter import *
def Centerx(parent, lar):
    #Fução q acha o centro x da resolução
    largura_screen = parent.winfo_screenwidth()
    posx = largura_screen/2 - lar/2
    return posx

def Centery(parent,alt):
    #Fução q acha o centro y da resolução
    altura_screen = parent.winfo_screenheight()
    posy = altura_screen/2 - alt/2
    return posy

#Criando Frame Login
class Login(Frame):
    def __init__(self, parent):
        super().__init__()
        #propriedades do Frame
        self['bg'] = 'black'
        self['heigh'] = 600
        self['width'] = 800
        self['relief'] = SOLID

        #widgets
    
        #Widgets Grid
        self.grid()
    #validação
    #autodestruir