import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('../BPC Leads (1).xlsx')

# Filtrar os nomes não duplicados na coluna "Instagram Adv"
unique_df = df.drop_duplicates(subset=['Instagram Adv'], keep=False)

# Salvar os nomes não duplicados em um novo arquivo Excel
unique_df.to_excel('nomes_nao_duplicados.xlsx', index=False)

print('Arquivo salvo como nomes_nao_duplicados.xlsx')
