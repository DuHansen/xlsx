import pandas as pd

# Carregar a planilha 'lista.xlsx' e a planilha 'BPCFiltro.xlsx'
lista_df = pd.read_excel('./clientes (3).xlsx')
bpc_df = pd.read_excel('./BPC Leads (12).xlsx')

# Extrair a lista de nomes da coluna 'Instagram Adv' da planilha 'BPCFiltro.xlsx'
nomes_bpc = bpc_df['Instagram Adv'].tolist()

# Filtrar os nomes da coluna 'A' da planilha 'lista.xlsx' que não estão na lista de 'Instagram Adv'
filtrado_lista_df = lista_df[~lista_df['Nomes'].isin(nomes_bpc)]

# Salvar a planilha 'lista.xlsx' com os nomes filtrados
filtrado_lista_df.to_excel('lista_filtradasa.xlsx', index=False)

print('Arquivo salvo como lista_filtrada.xlsx')
