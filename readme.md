# Projeto de Filtragem de Nomes Duplicados

Este projeto utiliza a biblioteca `pandas` para carregar, filtrar e salvar dados de um arquivo Excel. O objetivo é remover nomes duplicados na coluna "Instagram Adv" e salvar os nomes únicos em um novo arquivo Excel.

## Arquivos

- **BPC Leads (1).xlsx**: Arquivo original contendo os dados a serem processados.
- **nomes_nao_duplicados.xlsx**: Arquivo gerado contendo apenas os nomes não duplicados.

## Código

```python
import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('../BPC Leads (1).xlsx')

# Filtrar os nomes não duplicados na coluna "Instagram Adv"
unique_df = df.drop_duplicates(subset=['Instagram Adv'], keep=False)

# Salvar os nomes não duplicados em um novo arquivo Excel
unique_df.to_excel('nomes_nao_duplicados.xlsx', index=False)

print('Arquivo salvo como nomes_nao_duplicados.xlsx')

# Projeto de Filtragem e Processamento de Dados Excel

Este projeto utiliza a biblioteca `pandas` para carregar, filtrar e salvar dados de arquivos Excel. O objetivo é remover nomes duplicados e filtrar dados com base em um status específico.

## Arquivos

- **BPC Leads (1).xlsx**: Arquivo original contendo os dados a serem processados.
- **nomes_nao_duplicados.xlsx**: Arquivo gerado contendo apenas os nomes não duplicados.
- **nomes_aguardando.xlsx**: Arquivo gerado contendo os dados filtrados pelo status "Aguardando Resposta".

## Código

### Script 1: Remover Nomes Duplicados

```python
import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('../BPC Leads (1).xlsx')

# Filtrar os nomes não duplicados na coluna "Instagram Adv"
unique_df = df.drop_duplicates(subset=['Instagram Adv'], keep=False)

# Salvar os nomes não duplicados em um novo arquivo Excel
unique_df.to_excel('nomes_nao_duplicados.xlsx', index=False)

print('Arquivo salvo como nomes_nao_duplicados.xlsx')

# Como Executar
Certifique-se de ter a biblioteca pandas instalada:
pip install pandas

Execute o script Python para processar os dados:
python index.py