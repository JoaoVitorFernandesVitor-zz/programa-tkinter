from tkinter import *
from time import *

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

#Banco de Dados
B_dados = {'Yuki':
            {'senha': '1234',
            'funcao': 'adm'           
}
}



#Criando Frame Login
class Login(Frame):
    def __init__(self, parent):
        super().__init__()
        #propriedades do Frame
        self['bg'] = '#201D1D'
        self['heigh'] = 600
        self['width'] = 800
        self['relief'] = SOLID
        self['padx'] = 300  
        self['pady'] = 300

        #Função para validar a entrada do usuario com o banco de dados
        def validar():
            user = entry_name.get()
            senha = entry_password.get()
            
            try:
                if B_dados[user]['senha'] == senha:
                    print('validado com sucesso')
                    espace['text'] = ''
                    self.destroy()
                else:
                    espace['text'] = 'Senha Incorreta'
                    espace['fg'] = 'red'  
            except(KeyError):
                espace['text'] = 'Usuario ou senha estão incoretos'
                espace['fg'] = 'red'
            
        #widgets
        entry_name = Entry(self, bd = 3)
        user_name  = Label(self, text = 'Username', bd = 3, relief = RAISED)
        entry_password  = Entry(self, bd = 3 )
        user_password = Label(self, text = 'Passwors', bd = 3, relief = RAISED) 
        espace = Label(self, bg = self['bg'], width = 30 )
        bt_login = Button(self,text ="Logar", command = validar)

        #Widgets Grids
        user_name.grid(row = 0)
        entry_name.grid(row = 1)
        espace.grid(row = 2)
        user_password.grid(row = 3, columnspan = 2,)
        entry_password.grid(row = 4)
        bt_login.grid(row = 5)  
        self.grid()
