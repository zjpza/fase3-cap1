"""
dados.py — Módulo de Leitura de Dados do Agronegócio Brasileiro
Projeto: Ir Além — Dashboard Agrícola (FIAP)
Carrega os dados reais da planilha agronegocio_brasil_2023_24.xlsx
"""

import pandas as pd
import os


def carregar_dados_agricolas():
    """Carrega DataFrame com dados reais do agronegócio brasileiro 2023/24."""
    # Caminho relativo à raiz do projeto (subindo um nível de src/)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho_excel = os.path.join(base_dir, "data", "agronegocio_brasil_2023_24.xlsx")

    # Ler pulando a primeira linha (título geral) e usando a segunda como header
    df = pd.read_excel(caminho_excel, header=1)

    # Renomear colunas para nomes limpos
    df.columns = [
        "n_obs", "estado", "cultura", "municipios_produtores",
        "produtividade_kg_ha", "mecanizacao", "regiao", "fonte"
    ]

    # Remover linhas com dados nulos ou lixo do header (linhas de metadados/resumo)
    df = df.dropna(subset=["estado", "cultura"]).copy()

    # Filtrar linhas que ainda contenham texto do header
    lixo_header = [
        "Obs.", "Qual. Nominal", "Quant. Discreta", "Quant. Contínua",
        "Qual. Ordinal", "Geográfica", "Principal", "Mecanização",
        "Nível de", "Fonte Principal"
    ]
    for col in ["estado", "cultura", "regiao", "mecanizacao", "fonte"]:
        for termo in lixo_header:
            df = df[~df[col].astype(str).str.contains(termo, na=False)]

    # Converter tipos numéricos
    df["n_obs"] = pd.to_numeric(df["n_obs"], errors="coerce")
    df["municipios_produtores"] = pd.to_numeric(df["municipios_produtores"], errors="coerce")
    df["produtividade_kg_ha"] = pd.to_numeric(df["produtividade_kg_ha"], errors="coerce")

    # Padronizar texto
    df["estado"] = df["estado"].astype(str).str.strip()
    df["cultura"] = df["cultura"].astype(str).str.strip()
    df["regiao"] = df["regiao"].astype(str).str.strip()
    df["mecanizacao"] = df["mecanizacao"].astype(str).str.strip()
    df["fonte"] = df["fonte"].astype(str).str.strip()

    # Ordenar por região e cultura
    df = df.sort_values(["regiao", "estado", "cultura"]).reset_index(drop=True)

    return df


if __name__ == "__main__":
    df = carregar_dados_agricolas()
    print(f"Total de registros: {len(df)}")
    print(f"\nColunas: {df.columns.tolist()}")
    print(f"\nCulturas únicas: {sorted(df['cultura'].unique().tolist())}")
    print(f"Regiões únicas: {sorted(df['regiao'].unique().tolist())}")
    print(f"Mecanização: {sorted(df['mecanizacao'].unique().tolist())}")
    print("\n--- Primeiras 10 linhas ---")
    print(df.head(10).to_string())
    print("\n--- Describe ---")
    print(df[["municipios_produtores", "produtividade_kg_ha"]].describe().round(2).to_string())
