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
        
        #Tela para Registro 
        def register():

            #Funcoes
            def cadastrar():
                r_user = entry_Ruser.get()
                r_pass = entry_Rpassword.get()
                r_confirm = entry_Rconfimpass.get()
            
             #Tratamento de Erros
                
               #Verifica se nome do usuario ja existe
                try:
                    if B_dados[r_user]:
                        print('Usuario Ja Cadastrado')

               #Se nao existir,começa o cadastro
                except(KeyError):
                    v  = True
                    #User em branco
                    if r_user == '':
                        print('Users em branco nao são permitidos')
                        v = False
                    #Senhas em branco
                    if r_pass == '':
                        print('Senhas em branco não são permitidas')
                        v = False
                    #Senha e User iguais
                    if r_user == r_pass :
                        print('User e Password não podem ser iguais')
                        v = False

                    #Verifica se as senha e a confirmação da senha sao iguais
                    if r_pass != r_confirm:
                        print('Password e Confirm não são iguais')
                        v = False
                    
                    #Cadastrar usuario se não tiver nenhum erro
                    if v:
                        B_dados[r_user]= {'senha' : r_pass }
                        print('Usuario Cadastrado com sucesso!')

            #Propriedades da tela de registro
            r_lar = 250
            r_alt = 150
            r_titulo = 'Registrar-se'
            r_x = Centerx(self, r_alt)
            r_y = Centery(self, r_lar)

            #Configurando tela registro
            r_janela = Toplevel(parent)
            r_janela.geometry('%dx%d+%d+%d' %(r_lar, r_alt, r_x, r_y))
            r_janela.title(r_titulo)
            r_janela.resizable(False, False)

            #Widgets registro
            t_frame =Frame(r_janela,width = 300,heigh = 10)
            tituloI_text = Label(r_janela, text = 'Novo Registro', font = 'Arial 20', width = 15)
            
            entry_Ruser = Entry(r_janela, bd = 3)
            user_text = Label(r_janela, text = 'User')
            
            entry_Rpassword = Entry(r_janela, bd = 3)
            password_text = Label(r_janela, text = 'Password')
            
            entry_Rconfimpass = Entry(r_janela, bd = 3)
            confirmpass_text = Label(r_janela, text = 'Confirm')
            
            bt_registrar = Button(r_janela, text = 'Registrar' , command = cadastrar)
            #Grids registro
            tituloI_text.grid(columnspan = 3)

            entry_Ruser.grid(row = 1 , column = 1)
            user_text.grid(row = 1)

            
            entry_Rpassword.grid(row = 2, column = 1)
            password_text.grid(row = 2)
            
            entry_Rconfimpass.grid(row = 3, column = 1)
            confirmpass_text.grid(row = 3)
            bt_registrar .grid(column = 1)

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
        entry_name.grid(row = 1)
        espace.grid(row = 2)
        user_password.grid(row = 3, columnspan = 2,)
        entry_password.grid(row = 4)
        bt_login.grid(row = 5)  
        bt_create.grid(row = 6)
        self.grid()
