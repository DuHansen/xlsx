import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('./nomes_nao_duplicados.xlsx')

# Imprimir as primeiras linhas para verificar o carregamento
print("Dados carregados:")
print(df.head())

# Verificar se a coluna "Status" existe e aplicar o filtro
if 'Status' in df.columns:
    # Filtrar pelo status "Aguardando Resposta"
    filtered_df = df[df['Status'] == 'Aguardando Resposta']
    
    # Imprimir para verificar a filtragem
    print("\nDados após filtragem por status:")
    print(filtered_df.head())
    
    # Salvar os resultados filtrados em um novo arquivo Excel
    if not filtered_df.empty:
        filtered_df.to_excel('nomes_aguardando.xlsx', index=False)
        print('Arquivo salvo como nomes_aguardando.xlsx')
    else:
        print('Nenhum dado encontrado com o status "Aguardando Resposta".')
else:
    print("Coluna 'Status' não encontrada no DataFrame.")
