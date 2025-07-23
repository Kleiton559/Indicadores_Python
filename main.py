#Importação de Bibliotecas
import os

def display(lista):
    for item in lista:
      print(item)

#Diretório
#diretory = "C:/Users/krena/OneDrive/Documentos/PROJETOS PESSOAIS/DB_vendas/Vendas"
diretory = "****Coloque o Seu Diretório Aqui****"
#listar Arquivos dentro de uma pasta
lista_arquivos = os.listdir(diretory)
#display(lista_arquivos)


#Importar bases de dados de vendas
for arquivo in lista_arquivos:
    # Exibir o nome de cada arquivo
     #print(arquivo)

    #Verificar se é  um arquivo de vendas
    if "vendas" in arquivo.lower():#arquivo.lower() - tratamento de dados
     #Importar o Arquivo de Vendas
     print(f'{diretory}/{arquivo}')
