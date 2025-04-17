import os
import pandas as pd
from modules.conexao_db import conectar, desconectar

def inferir_tipo(valor, col):
    
    if col == 'MATRICULA':
        return "INT"

    if pd.isna(valor):
        return "VARCHAR(255)"
    
    if isinstance(valor, int):
        return "INT"
    elif isinstance(valor, float):
        return "FLOAT"
    elif isinstance(valor, pd.Timestamp):
        return "DATE"
    else:
          try:
            pd.to_datetime(valor)
            return "DATE"
          except:
              return "VARCHAR(255)"
          

def criar_tabela_a_partir_planilha(caminho_planilha):
    
    dataframe = pd.read_excel(caminho_planilha)

    nome_arquivo = os.path.splitext(os.path.basename(caminho_planilha))[0]

    conexao = conectar()

    cursor = conexao.cursor()

    colunas = dataframe.columns

    #pega a primeira linha para inferir o tipo da coluna
    exemplo_linha = dataframe.iloc[0]

    sql_colunas = []
    for col in colunas:
        tipo = inferir_tipo(exemplo_linha[col], col.upper())

        linha_sql = f"`{col}` {tipo}"
        if col.upper() == "MATRICULA":
            linha_sql += " PRIMARY KEY"

        sql_colunas.append(linha_sql)

    sql = f"CREATE TABLE IF NOT EXISTS `{nome_arquivo}` ({', '.join(sql_colunas)});"

    try:
        cursor.execute(sql)
        conexao.commit()
        print(f"Table '{nome_arquivo}' criada com sucesso!")
    except Exception as error:
        print(f"Erro ao criar a  tabela: {error}")
    finally:
        cursor.close()
        desconectar(conexao)

def inserir_dados_planilha(caminho_planilha):
    dataframe = pd.read_excel(caminho_planilha)
    nome_arquivo = os.path.splitext(os.path.basename(caminho_planilha))[0]

    connection = conectar()
    cursor = connection.cursor()

    colunas = dataframe.columns.tolist()
    colunas_sql = ", ".join(f"`{col}`" for col in colunas)
    placeholders = ", ".join(["%s"] * len(colunas))

    insert_sql = f"INSERT INTO `{nome_arquivo}` ({colunas_sql}) VALUES ({placeholders})"

    try:
        dados = [
            tuple(row[col] if not pd.isna(row[col]) else None for col in colunas)
            for _, row in dataframe.iterrows()
        ]

        cursor.executemany(insert_sql, dados)
        connection.commit()
        print(f"Todos os dados foram inseridos com sucesso na tabela '{nome_arquivo}'.")
    except Exception as error:
        print(f"Erro ao inserir dados: {error}")
    finally:
        cursor.close()
        desconectar(connection)
