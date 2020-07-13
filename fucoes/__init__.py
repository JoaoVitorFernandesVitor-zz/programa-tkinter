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
        self['heigh'] = 100
        self['width'] = 100
        self['relief'] = SOLID
        self['padx'] = 340  
        self['pady'] = 270
        

        #Função para validar a entrada do usuario com o banco de dados
        def validar():
            user = entry_name.get()
            senha = entry_password.get()
            
            if B_dados[user]['senha'] == senha:
                print('validado com sucesso')
            else:
                print('falha')

        #widgets
        entry_name = Entry(self, bd = 3)
        user_name  = Label(self, text = 'Username', bd = 3, relief = RAISED)
        entry_password  = Entry(self, bd = 3 )
        user_password = Label(self, text = 'Passwors', bd = 3, relief = RAISED) 
        espace = Label(self, bg = self['bg'])
        bt_login = Button(self,text ="Logar", command = validar)

        #Widgets Grids
        self.grid()
        user_name.grid()
        entry_name.grid()
        espace.grid()
        user_password.grid()
        entry_password.grid()
        bt_login.grid()  

        
    #autodestruir