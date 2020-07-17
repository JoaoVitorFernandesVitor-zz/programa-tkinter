from tkinter import *
from fucoes import *

#Class da tela principal do sistema
class Main(Frame):
    def __init__(self, parent,list):
        super().__init__()
        #propriedades do frame
        self['heigh'] = 600
        self['width'] = 800
        self['bg']    = "gray"
        texto = StringVar()
        #Funcoes
        
        #Fuçao de imprimir cadastrados na tela
        def ver_C(user = '', seach = False):
            t = ''
            #Ver cadastro especifico
            if seach:
                t = f'{user} - {list[user]}'.replace('{', '').replace('}', '').replace(',', '').replace("'", '').replace(':', ' -')


            # Ver todos cadastros
            else:
                t = ''
                for item in list:
                    
                    t += f'\n{item} - {list[item]}'.replace('{', '').replace('}', '').replace(',', '').replace("'", '').replace(':', ' -')

            texto.set(t)

            dados_screen = Label(self, textvariable = texto, width = 32, heigh = 0, font = 'Arial 20', bg = self['bg']).grid(
                    row = 0, rowspan = 5 , column = 2, sticky = N,
                    padx = 0, pady = (0,20)
                )
        #Função para procurar cadastrados
        def seach_C():
            ver_C('yuki',seach = True)


        #Funçao para deletar cadastros
        #def deletar_C():
            
        
        #botoes do menu
        bt_ver = Button(self, text = 'Ver cadastrados', heigh = 5, width = 30 , font = 'System 10  ', bg = "blue1",
        command = ver_C)
        bt_del = Button(self, text = 'Deletar cadastro',heigh = 5, width = 30, font = 'System 10', bg = "blue1")
        bt_seach = Button(self, text = 'Procurar cadrastro', heigh = 5, width = 30, font = 'System 10', bg = "blue1",
        command = seach_C)
        
        #Botoes Grid
        bt_ver.grid(row = 0, column = 0, padx = 30, pady = 50)
        bt_seach.grid(row = 1, column = 0, padx = 30, pady = 50)
        bt_del.grid(row = 2, column = 0, padx = 30, pady = 50)
        
        #Entrada de texto
        text_box = Entry(self, width = 30 ).grid(
            row = 2, column = 3
        )


        #Risco divisor vertical
        traco = Label(self, text = "", bg = "gray2", heigh = 40).grid(
            row = 0, rowspan = 3 , column = 1, sticky = N
        )

        self.grid()