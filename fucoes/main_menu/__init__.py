from tkinter import *
from fucoes import Login
from fucoes import Registro
from fucoes import B_dados

#Class da tela principal do sistema
class Main(Frame):
    def __init__(self, parent):
        super().__init__()
        #propriedades do frame
        self['heigh'] = 600
        self['width'] = 800
        self['bg']    = "#DCDCDC"
        texto = StringVar()
        linha = '-' * 50
        #Funcoes
        
        #Fuçao de imprimir cadastrados na tela
        def ver_C(user = "", seach = False):
            t = ''
            #Ver cadastro especifico
            if seach is True:
                
                try:
                    t = f'User - {user} - {B_dados.B_dados[user]}'.replace('{', '').replace('}', '').replace(',', '').replace("'", '').replace(':', ' -')
                
                except(KeyError):
                    t = 'Usuario não encontrado\nno banco de dados.'
                
            # Ver todos cadastros
            else:
                t = ''
                for item in B_dados.B_dados:
                    
                    t += f'\nUser - {item} - {B_dados.B_dados[item]}\n{linha}'.replace('{', '').replace('}', '').replace(',', '').replace("'", '').replace(':', ' -')

            texto.set(t)
            
            #Label responsavel para imprimir o texto com os cadastrados
            dados_screen = Label(self, textvariable = texto, width = 32, heigh = 0, font = 'Arial 20', bg = self['bg']).grid(
                    row = 0, rowspan = 5 , column = 2, sticky = N,
                    padx = 0, pady = (0,20)
                )
    
        #Função para procurar cadastrados
        def seach_C():
            user_ = entry_seach.get()
            ver_C(user_, seach = True)

        #Funçao para deletar cadastros
        def Add():
            Registro.Register(self)
        
        #botoes do menu
        bt_ver = Button(self, text = 'Ver cadastrados', heigh = 5, width = 30 , font = 'System 10  ', bg = "#5F9EA0",
        command = ver_C)
        bt_del = Button(self, text = 'Adicionar cadrastro',heigh = 5, width = 30, font = 'System 10', bg = "#5F9EA0",
        command = Add)
        bt_seach = Button(self, text = 'Procurar cadrastro', heigh = 5, width = 30, font = 'System 10', bg = "#5F9EA0",
        command = seach_C)
        
        #Botoes Grid
        bt_ver.grid(row = 0, column = 0, padx = 30, pady = 50)
        bt_seach.grid(row = 1, column = 0, padx = 30, pady = 0)
        bt_del.grid(row = 3, column = 0, padx = 30, pady = 50)
        
        #Entrada de texto
        entry_seach = Entry(self,bd = 5)
        entry_seach.grid(row = 2, column = 0)
        
        #Risco divisor vertical
        traco = Label(self, text = "", bg = "#054F77", heigh = 40, bd = 5 , relief = RAISED).grid(
          row = 0, rowspan = 4 , column = 1, sticky = N)
        self.grid()