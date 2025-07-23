#Importação de Bibliotecas
import os
import pandas as pd
import  matplotlib.pyplot as plt


def display(lista):
    for item in lista:
      print(item)

#Diretório
diretory = "C:/Users/krena/OneDrive/Documentos/PROJETOS PESSOAIS/DB_vendas/Vendas"
#listar Arquivos dentro de uma pasta
lista_arquivos = os.listdir(diretory)
#display(lista_arquivos)
tabela_total = pd.DataFrame()


#Importar bases de dados de vendas
for arquivo in lista_arquivos:
    # Exibir o nome de cada arquivo
     #print(arquivo)

    #Verificar se é  um arquivo de vendas
    if "vendas" in arquivo.lower():#arquivo.lower() - tratamento de dados
        #Importar o Arquivo de Vendas
        #print(f'{diretory}/{arquivo}')
        diretory_arquivo = diretory+'/'+arquivo
        #print(diretory_arquivo)
        #print(arquivo)
        tabela=pd.read_csv(diretory_arquivo)

        # Adicionar numa unica tabela
        tabela_total = tabela_total._append(tabela)

#Exibir a tabela total com as outras tabelas adicionadas
#print(tabela_total)


#Produto mais vendido
tabela_produtos = tabela_total.groupby('Produto').sum()

#Exibir apenas colunas [["Quantidade Vendida", "Preco Unitario"]]
tabela_produtos = tabela_produtos[["Quantidade Vendida", "Preco Unitario"]]
print(tabela_produtos)


