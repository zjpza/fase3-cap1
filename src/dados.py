"""
dados.py — Módulo de Geração de Dados Simulados
Projeto: Ir Além — Dashboard Agrícola (FIAP)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def gerar_dados_agricolas(n_registros=1500, seed=42):
    """Gera DataFrame com dados agrícolas simulados realistas."""
    np.random.seed(seed)

    culturas = {
        'Soja': {
            'umidade_media': 65, 'umidade_std': 8,
            'ph_medio': 6.0, 'ph_std': 0.4,
            'fosforo_medio': 15, 'fosforo_std': 5,
            'potassio_medio': 120, 'potassio_std': 30,
            'temp_media': 26, 'temp_std': 3,
            'precip_media': 130, 'precip_std': 40,
            'prod_base': 3200, 'prod_std': 400,
        },
        'Milho': {
            'umidade_media': 60, 'umidade_std': 10,
            'ph_medio': 5.8, 'ph_std': 0.5,
            'fosforo_medio': 20, 'fosforo_std': 6,
            'potassio_medio': 150, 'potassio_std': 35,
            'temp_media': 25, 'temp_std': 4,
            'precip_media': 120, 'precip_std': 35,
            'prod_base': 8500, 'prod_std': 1200,
        },
        'Café': {
            'umidade_media': 55, 'umidade_std': 7,
            'ph_medio': 5.5, 'ph_std': 0.3,
            'fosforo_medio': 12, 'fosforo_std': 4,
            'potassio_medio': 180, 'potassio_std': 40,
            'temp_media': 22, 'temp_std': 3,
            'precip_media': 150, 'precip_std': 45,
            'prod_base': 2400, 'prod_std': 350,
        }
    }

    regioes = {
        'Cerrado (GO/MT)': {'ajuste_umidade': -3, 'ajuste_temp': 2},
        'Sul (PR/RS)': {'ajuste_umidade': 5, 'ajuste_temp': -3},
        'Sudeste (SP/MG)': {'ajuste_umidade': 0, 'ajuste_temp': 0},
        'Nordeste (BA/PI)': {'ajuste_umidade': -8, 'ajuste_temp': 4},
        'MATOPIBA': {'ajuste_umidade': -5, 'ajuste_temp': 3},
    }

    tipos_solo = ['Latossolo Vermelho', 'Argissolo', 'Neossolo', 'Cambissolo', 'Nitossolo']

    data_inicio = datetime(2024, 1, 1)
    data_fim = datetime(2025, 12, 31)
    intervalo_dias = (data_fim - data_inicio).days

    registros = []

    for i in range(n_registros):
        cultura_nome = np.random.choice(list(culturas.keys()))
        regiao_nome = np.random.choice(list(regioes.keys()))
        tipo_solo = np.random.choice(tipos_solo)

        c = culturas[cultura_nome]
        r = regioes[regiao_nome]

        dias_offset = np.random.randint(0, intervalo_dias)
        data = data_inicio + timedelta(days=int(dias_offset))
        mes = data.month
        fator_sazonal = np.sin(2 * np.pi * (mes - 1) / 12)

        # Umidade do solo (%)
        umidade = np.clip(
            np.random.normal(c['umidade_media'] + r['ajuste_umidade'] + fator_sazonal * 8, c['umidade_std']),
            20, 95
        )
        # pH do solo
        ph = np.clip(np.random.normal(c['ph_medio'], c['ph_std']), 4.0, 8.0)
        # Fósforo (mg/dm³)
        fosforo = np.clip(np.random.normal(c['fosforo_medio'], c['fosforo_std']), 2, 50)
        # Potássio (mg/dm³)
        potassio = np.clip(np.random.normal(c['potassio_medio'], c['potassio_std']), 30, 300)
        # Temperatura (°C)
        temperatura = np.clip(
            np.random.normal(c['temp_media'] + r['ajuste_temp'] - fator_sazonal * 3, c['temp_std']),
            10, 42
        )
        # Precipitação (mm)
        precipitacao = np.clip(
            np.random.normal(c['precip_media'] + fator_sazonal * 50, c['precip_std']),
            0, 400
        )

        # Produtividade (kg/ha) — correlacionada com variáveis do solo
        fator_umidade = 1 + 0.003 * (umidade - c['umidade_media'])
        fator_ph = 1 - 0.05 * abs(ph - c['ph_medio'])
        fator_pk = 1 + 0.001 * (fosforo + potassio * 0.1 - 25)
        fator_temp = 1 - 0.02 * abs(temperatura - c['temp_media'])

        produtividade = np.clip(
            np.random.normal(c['prod_base'] * fator_umidade * fator_ph * fator_pk * fator_temp, c['prod_std']),
            c['prod_base'] * 0.3, c['prod_base'] * 1.8
        )

        registros.append({
            'data': data, 'cultura': cultura_nome, 'regiao': regiao_nome,
            'tipo_solo': tipo_solo, 'umidade': round(umidade, 1),
            'pH': round(ph, 2), 'fosforo': round(fosforo, 1),
            'potassio': round(potassio, 1), 'temperatura': round(temperatura, 1),
            'precipitacao': round(precipitacao, 1), 'produtividade': round(produtividade, 0),
        })

    df = pd.DataFrame(registros)
    df = df.sort_values('data').reset_index(drop=True)
    df['data'] = pd.to_datetime(df['data'])
    return df


if __name__ == '__main__':
    df = gerar_dados_agricolas()
    print(f"Total de registros: {len(df)}")
    print(f"Período: {df['data'].min().date()} a {df['data'].max().date()}")
    print(df.describe().round(2))
