# EXEMPLO 1
import polars as pl
from datetime import datetime

ENDERECO_DADOS = r'./dados/'

try:
    # Marcar a hora de início
    hora_inicio = datetime.now()

    # Carregando o arquivo CSV
    df_dados = pl.read_csv(ENDERECO_DADOS + 'dados_teste.csv', separator=',', encoding='utf-8')

    # Exibindo os dados
    df_dados_lazy = df_dados.lazy()

    df_dados_lazy = (
        df_dados_lazy
        .filter(pl.col("total_vendas") > 1000) # Filtrando por valor
        .group_by(["regiao","forma_pagamento"]) # Agrupando por regiao e forma de pagamento
        .agg(pl.col("quantidade").sum().alias('total de quantidade')) # Agregando 
    )

    # Mostrar o plano de execução
    print("Plano de Execução:")
    print(df_dados_lazy.explain())

    # Coletar os dados após a execução
    df_bf = df_dados_lazy.collect()

    # Exibir os dados
    print(df_bf)

    # Marcar a hora de término
    hora_fim = datetime.now()

    print(f'Tempo de execução: {hora_fim - hora_inicio}')

    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
