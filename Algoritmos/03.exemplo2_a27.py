# EXEMPLO 3

# CORRELAÇÃO
# Vai calcular a correlação entre duas variaveis quantitativas sobre o ponto de vista de uma variavel qualitativa
# r (-1 a 1)
# r = 1 : Correlação positiva, as variaveis quantitativas se correlacionam diretamente
# r = -1 : Correlação negativa, variaveis se relacionam inversamente.
# r = 0 : Não há correlação
# GUIDELINE POR RUMSEY (2023):
# r = 1 (Correlação Perfeita)
# r >= 0.7 (Correlação Forte)
# r >= 0.3 (Correlação Moderada)
# r < 0.3 (Correlação Fraca)
# r = 0 (Não há Correlação)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Obter dados
try:
    os.system("cls")
    print("Obtendo dados...")

    ENDERECO_DADOS="https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"
    
    #encodings: utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=";", encoding="iso-8859-1")

    # Delimitando somente as variáveis
    df_veiculos = df_ocorrencias[["cisp","roubo_veiculo", "recuperacao_veiculos"]]

    # totalizar por CISP:
    df_total_veiculos = df_veiculos.groupby(["cisp"]).sum(["roubo_veiculo","recuperacao_veiculos"]).reset_index()

    # print(df_total_veiculos.head())

    print("\nDados obtidos com sucesso!")

except Exception as e:
    print(f"Erro ao obter dados: {e}")
    exit()

# CORRELAÇÃO
try:
    print("\nCalculando a correlação...")

    # Correlação de pearson
    correlacao = np.corrcoef(
        df_total_veiculos["roubo_veiculo"],
        df_total_veiculos["recuperacao_veiculos"])#[0,1] # se tirar o [0,1] ele printa como matriz
    
    print(f"\nCorrelação: {correlacao[0,1]}\nCorrelação em matriz:\n{correlacao}")

except ImportError as e:
    print(f"Erro: {e}")

# GRAFICO
try:
    # plotar grafico
    plt.scatter(df_total_veiculos['roubo_veiculo'],df_total_veiculos["recuperacao_veiculos"])
    plt.title(f"Correlação:\n{correlacao}")
    plt.xlabel("Roubo de veiculos")
    plt.ylabel("Recuperacao de veiculos")
    plt.show()

except ImportError as e:
    print(f"Erro: {e}")
