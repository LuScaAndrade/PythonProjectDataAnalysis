#Passo 0 - Entender o desafio
#Passo 1 - Percorrer todos os arquivos da base de dados 


#Passo 2 - Importar as bases de dados de vendas
#Passo 3 - Tratar / compilar as bases de dados
#Passo 4 - Calcular o produto mais vendido (em quantidade)
#Passo 5 - Calcular o produto que mais faturou (em faturamento)
#Passo 6 - Calcular a loja / cidade que mais vendeu (em faturamento) - criar um gráfico / dashboard

import os

archives_list = os.listdir(r"C:\Users\Lucas\OneDrive\Área de Trabalho\workspace-python\CursoPython\Vendas")
print(archives_list)
print("\n")
for archive in archives_list:
    print(fr"C:\Users\Lucas\OneDrive\Área de Trabalho\workspace-python\CursoPython\Vendas\{archive}")
    
    
    