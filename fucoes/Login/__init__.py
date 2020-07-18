from tkinter import *
from fucoes import main_menu
from fucoes import Registro
from fucoes import Math

#Banco de Dados
B_dados = {'Yuki':
            {'senha': '1234'} ,         
        'yuki': {'senha': '5443'}
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
                    main_menu.Main(parent,B_dados)

                else:
                    espace['text'] = 'Senha Incorreta'
                    espace['fg'] = 'red'  
            except(KeyError):
                espace['text'] = 'Usuario ou senha estão incoretos'
                espace['fg'] = 'red'
        
        def register():
            Registro.Register(self)

        #widgets login
        entry_name = Entry(self, bd = 3)
        user_name  = Label(self, text = 'Username', bd = 3, relief = RAISED)
        entry_password  = Entry(self, bd = 3 )
        user_password = Label(self, text = 'Passwors', bd = 3, relief = RAISED) 
        espace = Label(self, bg = self['bg'], width = 30 )
        bt_login = Button(self,text ="Logar", command = validar)
        bt_create = Button(self, text = 'Criar Conta', command = register)

        #Widgets Grids
        user_name.grid(row = 0)
        entry_name.grid(row = 1, pady = (0,1))
        espace.grid(row = 2)
        user_password.grid(row = 3, columnspan = 2,)
        entry_password.grid(row = 4, pady = (0,1))
        bt_login.grid(row = 5)  
        bt_create.grid(row = 6, pady = (0,30))
        self.grid()
