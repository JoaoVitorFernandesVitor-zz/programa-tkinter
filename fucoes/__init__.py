from tkinter import *



#criando botao
class Botao(Button):
    def __init__(self,parent , texto, row_ = 0 , column_ = 1):
        super().__init__()
        self['text'] = texto
        self.grid(row = row_, column= column_ )

#Criando Entrada de Texto
class MinhaEntry(Entry):
    def __init__(self, parent, row_ = 0, column_ = 0):
        super().__init__()
        self['width'] = 50
        self['bd'] = 5
        self.grid(row = row_, column = column_)

#Criando Label      
class label(Label):
    def __init__(self, parent, texto = '', row_ = 0, column_ = 0 , borda = 0):
        super().__init__()
        self['text'] = texto
        self.grid(row = row_, column = column_)
    