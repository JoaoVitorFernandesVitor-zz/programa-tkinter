import json
#Banco de Dados
B_dados = {'Yuki':
            {'senha': '1234'} ,         
        'yuki': {'senha': '5443'}
}


#Cria o Banco de dados em .json
def Create():
    try :
        open('B_dados.json', 'x')
        print("Baco de dados criado com sucesso")

    except:
        print('Houve um erro na criação do banco de dados')

#Função para se escrever no Aquivo
def Write(text):
    try:
        with open('B_dados.json', 'a') as file :
            file.write(text)
    except:
        print('Falha na escrita no Banco de dados')

