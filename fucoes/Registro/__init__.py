from tkinter import *
from fucoes import Login
from fucoes import Math
from fucoes import B_dados

#Tela para Registro 
class Register(Frame):
            
    def __init__(self, parent):
        super().__init__()
        texto = StringVar()
                
        #Funcoes
        def cadastrar():
            r_user = entry_Ruser.get()
            r_pass = entry_Rpassword.get()
            r_confirm = entry_Rconfimpass.get()
            erro_text['fg'] = "red"

            #Tratamento de Erros
                    
            #Verifica se nome do usuario ja existe
            try:

                if B_dados.B_dados[r_user]:
                    texto.set('Usuario Ja Cadastrado')
            #Se nao existir,começa o cadastro
            except(KeyError):

                v  = True
                #User em branco
                if r_user == '':
                    texto.set('Users em branco nao são permitidos')
                    v = False
                #Senhas em branco
                if r_pass == '':
                    texto.set('Senhas em branco não são permitidas')
                    v = False
                #Senha e User iguais
                if r_user == r_pass :
                    texto.set('User e Password não podem ser iguais')
                    v = False

                #Verifica se as senha e a confirmação da senha sao iguais
                if r_pass != r_confirm:
                    texto.set('Password e Confirm não são iguais')
                    v = False
                        
                #Cadastrar usuario se não tiver nenhum erro
                if v:
                    erro_text['fg'] = "green"
                    B_dados.B_dados[r_user]= {'senha' : r_pass }
                    texto.set('Usuario Cadastrado com sucesso!')

        #Propriedades da tela de registro
        r_lar = 250
        r_alt = 160
        r_titulo = 'Registrar-se'
        r_x = Math.Centerx(self,r_lar)
        r_y = Math.Centery(self,r_alt)

        #Configurando tela registro
        r_janela = Toplevel(parent)
        r_janela.geometry('%dx%d+%d+%d' %(r_lar, r_alt, r_x, r_y))
        r_janela.title(r_titulo)
        r_janela.resizable(False, False)

        #Widgets registro
        t_frame =Frame(r_janela,width = 300,heigh = 10)
        tituloI_text = Label(r_janela, text = 'Novo Registro', font = 'System 20', width = 15)
        erro_text = Label(r_janela, textvariable = texto, font = 'System 12', fg = "red")

        entry_Ruser = Entry(r_janela, bd = 3)
        user_text = Label(r_janela, text = 'USER')
                
        entry_Rpassword = Entry(r_janela, bd = 3)
        password_text = Label(r_janela, text = 'PASSWORD')
                
        entry_Rconfimpass = Entry(r_janela, bd = 3)
        confirmpass_text = Label(r_janela, text = 'CONFIRM')
                
        bt_registrar = Button(r_janela, text = 'Registrar' , command = cadastrar)

                
        #Grids registro
        tituloI_text.grid(columnspan = 3)
        erro_text.grid(row = 1, columnspan = 3)

        entry_Ruser.grid(row = 2, column = 1)
        user_text.grid(row = 2)

                
        entry_Rpassword.grid(row = 3, column = 1)
        password_text.grid(row = 3)
                
        entry_Rconfimpass.grid(row = 4, column = 1)
        confirmpass_text.grid(row = 4)
        bt_registrar .grid(row = 5,column = 1)
        self.grid()