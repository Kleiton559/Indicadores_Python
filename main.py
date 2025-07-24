#Importação de Bibliotecas
import os
import pandas as pd


def display(lista):
    for item in lista:
      print(item)

#Diretório
#diretory = "C:/Users/krena/OneDrive/Documentos/PROJETOS PESSOAIS/DB_vendas/Vendas"
diretory = "C://Users/estagiario.it/Documents/Cursos/Vendas"

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
print("===PRODUTO MAIS VENDIDO===")
tabela_produtos = tabela_total.groupby('Produto').sum()
#Exibir apenas colunas Quantidade Vendida ,Preco Unitario e ordenar por quantidade vendida descendente
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida",ascending=False)
print(tabela_produtos)
print("\n")

#Produto mais faturado - Coluna Quantidade Vendida X Coluna Preco Unitario
#Cria uma nova coluna denominado de Faturamento
print("===PRODUTO MAIS FATURADO ===")
tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"] # Coluna Quantidade Vendida X Coluna Preco Unitario
tabela_faturamento = tabela_total.groupby('Produto').sum().sort_values(by="Faturamento",ascending=False)#Agrupar por produtos e ordenar decresecente de acordo com faturamento
print(tabela_faturamento[["Quantidade Vendida","Preco Unitario","Faturamento"]])
print("\n")


#Loja Que mais Vendeu
print("===LOJA QUE MAIS VENDEU===")
tabela_lojas = tabela_total.groupby('Loja').sum()
print(tabela_lojas[["Quantidade Vendida","Preco Unitario","Faturamento"]])

