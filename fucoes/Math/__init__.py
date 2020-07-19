#Fução q acha o centro x da resolução
def Centerx(parent, lar):  
    largura_screen = parent.winfo_screenwidth()
    posx = largura_screen/2 - lar/2
    return posx

#Fução q acha o centro y da resolução
def Centery(parent,alt):
    altura_screen = parent.winfo_screenheight()
    posy = altura_screen/2 - alt/2
    return posy
