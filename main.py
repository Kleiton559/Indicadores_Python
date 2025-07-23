import pandas as pd



import plotly.express as px
import plotly.graph_objects as go

#lendo o ficheiro CSV
df = pd.read_csv('dataset_asimov.csv')

#Transformando meses em numeros para libertacao de Memoria
df.loc[ df['Mês'] == 'Jan', 'Mês'] = 1
df.loc[ df['Mês'] == 'Fev', 'Mês'] = 2
df.loc[ df['Mês'] == 'Mar', 'Mês'] = 3
df.loc[ df['Mês'] == 'Abr', 'Mês'] = 4
df.loc[ df['Mês'] == 'Mai', 'Mês'] = 5
df.loc[ df['Mês'] == 'Jun', 'Mês'] = 6
df.loc[ df['Mês'] == 'Jul', 'Mês'] = 7
df.loc[ df['Mês'] == 'Ago', 'Mês'] = 8
df.loc[ df['Mês'] == 'Set', 'Mês'] = 9
df.loc[ df['Mês'] == 'Out', 'Mês'] = 10
df.loc[ df['Mês'] == 'Nov', 'Mês'] = 11
df.loc[ df['Mês'] == 'Dez', 'Mês'] = 12

#print(df.info())


# Status de pagamento para 0 e 1
df['Valor Pago'] = df['Valor Pago'].str.lstrip('R$ ')
df.loc[df['Status de Pagamento'] == 'Pago', 'Status de Pagamento'] = 1
df.loc[df['Status de Pagamento'] == 'Não pago', 'Status de Pagamento'] = 0

# Transformando alguns campos em inteiros
df['Chamadas Realizadas'] = df['Chamadas Realizadas'].astype(int)
df['Dia'] = df['Dia'].astype(int)
df['Mês'] = df['Mês'].astype(int)
df['Valor Pago'] = df['Valor Pago'].astype(int)
df['Status de Pagamento'] = df['Status de Pagamento'].astype(int)

#Vendas Por Equipa
df_vendas_por_equipas = df.groupby('Equipe')['Valor Pago'].sum().reset_index()
print(df_vendas_por_equipas)

fig_df_vendas_por_equipas = go.Figure(go.Bar(
    x = df_vendas_por_equipas['Valor Pago'],
    y = df_vendas_por_equipas['Equipe'],
    orientation = 'h',
    textposition = 'auto',
    text = df_vendas_por_equipas['Valor Pago'],
    insidetextfont=dict(family='Times', size=12)
))
#print(fig_df_vendas_por_equipas.show())