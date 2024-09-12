### Start Script:

py index.py

# Projeto de Filtragem e Processamento de Dados Excel

Este projeto utiliza a biblioteca `pandas` para carregar, filtrar e salvar dados de arquivos Excel. O objetivo é remover nomes duplicados e filtrar dados com base em um status específico.

## Arquivos

- **`PlanilhaPrincipal.xlsx`**: Arquivo original contendo os dados a serem processados.
- **`Planilha_nomes_nao_duplicados.xlsx`**: Arquivo gerado contendo apenas os nomes não duplicados.
- **`Planilha_nomes_aguardando.xlsx`**: Arquivo gerado contendo os dados filtrados pelo status "Aguardando Resposta".

## Código

### Script 1: Remover Nomes Duplicados

```python
import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('../PlanilhaPrincipal.xlsx')

# Filtrar os nomes não duplicados na coluna "Instagram Adv"
unique_df = df.drop_duplicates(subset=['Instagram Adv'], keep=False)

# Salvar os nomes não duplicados em um novo arquivo Excel
unique_df.to_excel('nomes_nao_duplicados.xlsx', index=False)

print('Arquivo salvo como nomes_nao_duplicados.xlsx')
