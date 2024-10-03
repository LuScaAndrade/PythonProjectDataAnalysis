# PythonProjectDataAnalysis

## Análise de Vendas com Pandas e Plotly

Este projeto realiza a análise de dados de vendas, mostrando informações detalhadas sobre produtos vendidos e faturamento por loja. Utiliza as bibliotecas **Pandas** para manipulação de dados e **Plotly** para visualização de gráficos.

## Funcionalidades

- **Agrupamento e soma de vendas por produto:** O código processa diversos arquivos de vendas e calcula a quantidade total vendida de cada produto.
- **Cálculo de faturamento:** Calcula o faturamento total de cada produto com base na quantidade vendida e no preço unitário.
- **Visualização de faturamento por loja:** Exibe os dados de faturamento total por loja e gera um gráfico de barras interativo.

## Requisitos

Antes de executar o código, certifique-se de que as seguintes bibliotecas estão instaladas:

```bash
py -m pip install pandas
py -m pip install plotly
py -m pip install ipython
```

## Como Funciona
1. **Leitura de arquivos CSV:** O código percorre todos os arquivos da pasta de vendas que contêm a palavra "Vendas" no nome e concatena os dados em um DataFrame total.
2. **Agrupamento de dados:**
  - Agrupa as vendas por Produto e exibe a quantidade total vendida.
  - Calcula o faturamento (quantidade vendida x preço unitário) para cada produto e loja.
3. **Visualização dos dados:**
  - Exibe as tabelas de vendas e faturamento por produto e loja.
  - Cria um gráfico de barras interativo com o faturamento por loja usando Plotly.

## Exemplo de Uso
Para executar o script, basta rodar o arquivo principal:
```bash
python main.py
```
Isso vai gerar a análise das vendas e um gráfico interativo de faturamento por loja que será exibido na tela.

## Personalização
**Caminho dos arquivos:** Se os arquivos de vendas estiverem em outra pasta, ajuste o caminho na linha que faz a leitura dos arquivos:

```python
archives_list = os.listdir(r"Caminho\Para\Sua\Pasta\Vendas")
```

**Colunas dos dados:** O código depende de colunas específicas como 'Produto', 'Quantidade Vendida', 'Preço Unitário' e 'Loja'. Certifique-se de que os arquivos CSV contenham essas colunas.

## Gráfico de Barras Interativo
O gráfico gerado por este código usa Plotly para mostrar o faturamento por loja de forma visual. É possível interagir com o gráfico, clicando nos elementos e explorando os dados.
