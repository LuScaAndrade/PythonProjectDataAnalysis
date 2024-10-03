import os
import pandas as pd
import plotly.express as px
from IPython.display import display

archives_list = os.listdir(r"C:\Users\Lucas\OneDrive\Área de Trabalho\workspace-python\CursoPython\Vendas")

total_table = pd.DataFrame()

for archive in archives_list:
    if "Vendas" in archive:
        table = pd.read_csv(rf"C:\Users\Lucas\OneDrive\Área de Trabalho\workspace-python\CursoPython\Vendas\{archive}")
        total_table = pd.concat([total_table, table], ignore_index = True)
        
product_table = total_table.groupby('Produto').sum()
product_table = product_table[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=True)
display(product_table)

total_table['Faturamento'] = total_table['Quantidade Vendida'] * total_table['Preco Unitario']
billing_table = total_table.groupby('Produto').sum()
billing_table = billing_table[["Faturamento"]].sort_values(by="Faturamento", ascending=True)
display(billing_table)

stores_table = total_table.groupby('Loja').sum()
stores_table = stores_table[['Faturamento']]
display(stores_table)

graphic = px.bar(stores_table, x = stores_table.index, y = 'Faturamento') 
graphic.show()