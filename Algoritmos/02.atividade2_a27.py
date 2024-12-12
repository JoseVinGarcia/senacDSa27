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

    # Filtrando os resultados 1
    # df_dados_lazy = (
    #     df_dados_lazy
    #     .group_by('produto')
    #     .agg((pl.col('quantidade') * pl.col('preco')).sum().alias('total'))
    # )

    # Filtrando os resultados 2
    # df_dados_lazy = (
    #     df_dados_lazy
    #     .filter((pl.col('quantidade')*pl.col('preco'))>3500)
    # )

    # Filtrando os resultados 3
    # df_dados_lazy = (
    #     df_dados_lazy
    #     .filter(pl.col('preco') > 1500)
    #     .select(['produto', 'preco', 'quantidade', 'regiao'])
    # )

    # Filtrando os resultados (Final)
    # ALIAS é um nome gerado para a coluna dos resultados
    # df_dados_lazy = (
    #     df_dados_lazy
    #     .filter(pl.col('preco') > 1500)
    #     .select(['produto', 'preco', 'quantidade'])
    #     .group_by('produto')
    #     .agg((pl.col('quantidade') * pl.col('preco')).sum().alias('total'))
    # )

    df_dados_lazy = (
        df_dados_lazy
        .filter(pl.col("preco")>1000)
        .group_by(("regiao","forma_pagamento"))
        .agg(pl.col("total_vendas").sum().alias('total de vendas'))
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
