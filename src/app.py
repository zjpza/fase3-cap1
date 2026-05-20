"""
app.py — Dashboard Agrícola Interativo
Projeto: Ir Além — FIAP
Visualização de dados reais do agronegócio brasileiro (Safra 2023/24).
Utiliza Streamlit + Plotly para gráficos interativos.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from dados import carregar_dados_agricolas

# ==============================================================
# Configuração da página
# ==============================================================
st.set_page_config(
    page_title="🌱 Ir Além — Dashboard Agrícola | FIAP",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================
# Paleta de cores do agronegócio (tons de verde)
# ==============================================================
CORES = {
    'verde_escuro': '#1B5E20',
    'verde_medio': '#2E7D32',
    'verde_claro': '#43A047',
    'verde_lima': '#66BB6A',
    'verde_pastel': '#A5D6A7',
    'dourado': '#F9A825',
    'terra': '#795548',
    'fundo': '#0E1117',
    'texto': '#FAFAFA',
}

PALETA_CULTURAS = {
    'Soja': '#43A047',
    'Milho': '#F9A825',
    'Milho 2ª S.': '#FFB300',
    'Café': '#795548',
    'Algodão': '#E53935',
    'Mandioca': '#FF7043',
    'Cana-de-açúcar': '#8E24AA',
    'Trigo': '#5C6BC0',
    'Dendê (azeite)': '#26A69A',
    'Arroz': '#00ACC1',
    'Laranja': '#FB8C00',
}

PALETA_MECANIZACAO = {
    'Muito Baixo': '#E53935',
    'Baixo': '#FF7043',
    'Médio': '#F9A825',
    'Alto': '#66BB6A',
    'Muito Alto': '#2E7D32',
}

PALETA_SEQUENCIAL = ['#1B5E20', '#2E7D32', '#388E3C', '#43A047',
                     '#66BB6A', '#81C784', '#A5D6A7', '#C8E6C9']

# ==============================================================
# CSS customizado para visual profissional
# ==============================================================
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 50%, #43A047 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(27, 94, 32, 0.3);
    }
    .main-header h1 {
        color: white;
        font-size: 2.2rem;
        margin-bottom: 0.3rem;
    }
    .main-header p {
        color: #C8E6C9;
        font-size: 1.05rem;
    }

    .metric-card {
        background: linear-gradient(135deg, #1B5E2022, #2E7D3222);
        border: 1px solid #2E7D3244;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        text-align: center;
    }
    .metric-card h3 {
        color: #66BB6A;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.3rem;
    }
    .metric-card .valor {
        color: #FAFAFA;
        font-size: 1.8rem;
        font-weight: 700;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a1a0a 0%, #112211 100%);
    }
    section[data-testid="stSidebar"] .stMarkdown h2 {
        color: #66BB6A;
    }

    .separator {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #2E7D32, transparent);
        margin: 2rem 0;
    }

    .footer {
        text-align: center;
        color: #666;
        padding: 2rem 0 1rem;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================
# Carregar dados (com cache para performance)
# ==============================================================
@st.cache_data
def carregar_dados():
    """Carrega e faz cache dos dados reais da planilha."""
    return carregar_dados_agricolas()

df = carregar_dados()

# ==============================================================
# SIDEBAR — Filtros Interativos
# ==============================================================
with st.sidebar:
    st.markdown("## 🌿 Filtros")
    st.markdown("---")

    # Filtro por cultura
    st.markdown("### 🌾 Cultura")
    culturas_disponiveis = sorted(df['cultura'].unique())
    culturas_selecionadas = st.multiselect(
        "Selecione as culturas:",
        options=culturas_disponiveis,
        default=culturas_disponiveis,
        label_visibility="collapsed"
    )

    st.markdown("---")

    # Filtro por região
    st.markdown("### 📍 Região")
    regioes_disponiveis = sorted(df['regiao'].unique())
    regioes_selecionadas = st.multiselect(
        "Selecione as regiões:",
        options=regioes_disponiveis,
        default=regioes_disponiveis,
        label_visibility="collapsed"
    )

    st.markdown("---")

    # Filtro por mecanização
    st.markdown("### ⚙️ Mecanização")
    mecanizacao_disponiveis = sorted(df['mecanizacao'].unique())
    mecanizacao_selecionadas = st.multiselect(
        "Selecione os níveis:",
        options=mecanizacao_disponiveis,
        default=mecanizacao_disponiveis,
        label_visibility="collapsed"
    )

    st.markdown("---")

    # Filtro por estado
    st.markdown("### 🏛️ Estado (UF)")
    estados_disponiveis = sorted(df['estado'].unique())
    estados_selecionados = st.multiselect(
        "Selecione os estados:",
        options=estados_disponiveis,
        default=estados_disponiveis,
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; color:#555; font-size:0.8rem;'>"
        "🌱 FIAP — Ir Além<br>Dashboard Agrícola v2.0<br>"
        "Dados reais: CONAB · IBGE/PAM · MAPA · Embrapa"
        "</div>",
        unsafe_allow_html=True
    )

# ==============================================================
# Aplicar filtros ao DataFrame
# ==============================================================
df_filtrado = df[
    (df['cultura'].isin(culturas_selecionadas)) &
    (df['regiao'].isin(regioes_selecionadas)) &
    (df['mecanizacao'].isin(mecanizacao_selecionadas)) &
    (df['estado'].isin(estados_selecionados))
].copy()

# ==============================================================
# CABEÇALHO PRINCIPAL
# ==============================================================
st.markdown(
    '<div class="main-header">'
    '<h1>🌾 Ir Além — Dashboard Agrícola</h1>'
    '<p>Projeto acadêmico FIAP — Visualização interativa de dados do agronegócio '
    'brasileiro (Safra 2023/24). Dados reais: CONAB, IBGE/PAM, MAPA e Embrapa.</p>'
    '</div>',
    unsafe_allow_html=True
)

# ==============================================================
# CARDS DE MÉTRICAS RESUMO
# ==============================================================
if len(df_filtrado) == 0:
    st.warning("⚠️ Nenhum dado encontrado com os filtros selecionados. Ajuste os filtros na barra lateral.")
    st.stop()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(
        f'<div class="metric-card"><h3>📊 Registros</h3>'
        f'<div class="valor">{len(df_filtrado)}</div></div>',
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        f'<div class="metric-card"><h3>📍 Municípios (média)</h3>'
        f'<div class="valor">{df_filtrado["municipios_produtores"].mean():.0f}</div></div>',
        unsafe_allow_html=True
    )
with col3:
    st.markdown(
        f'<div class="metric-card"><h3>🏆 Prod. Média (kg/ha)</h3>'
        f'<div class="valor">{df_filtrado["produtividade_kg_ha"].mean():,.0f}</div></div>',
        unsafe_allow_html=True
    )
with col4:
    st.markdown(
        f'<div class="metric-card"><h3>📈 Prod. Máx (kg/ha)</h3>'
        f'<div class="valor">{df_filtrado["produtividade_kg_ha"].max():,.0f}</div></div>',
        unsafe_allow_html=True
    )
with col5:
    st.markdown(
        f'<div class="metric-card"><h3>🗺️ Estados</h3>'
        f'<div class="valor">{df_filtrado["estado"].nunique()}</div></div>',
        unsafe_allow_html=True
    )

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# GRÁFICO 1 — Produtividade por Cultura (Barras)
# ==============================================================
st.markdown("### 🏆 Produtividade Média por Cultura")

df_prod_cultura = (
    df_filtrado
    .groupby('cultura')['produtividade_kg_ha']
    .agg(['mean', 'count'])
    .reset_index()
    .rename(columns={'mean': 'prod_media', 'count': 'registros'})
    .sort_values('prod_media', ascending=False)
)

fig_prod_cultura = px.bar(
    df_prod_cultura,
    x='cultura',
    y='prod_media',
    color='cultura',
    color_discrete_map=PALETA_CULTURAS,
    labels={'cultura': 'Cultura', 'prod_media': 'Produtividade Média (kg/ha)'},
    title='',
    text_auto='.0f'
)
fig_prod_cultura.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color=CORES['texto'],
    showlegend=False,
    xaxis=dict(gridcolor='#333'),
    yaxis=dict(gridcolor='#333', title='Produtividade (kg/ha)'),
    height=420,
)
st.plotly_chart(fig_prod_cultura, use_container_width=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# GRÁFICO 2 — Produtividade por Região e Cultura (Barras Agrupadas)
# ==============================================================
st.markdown("### 📍 Produtividade por Região e Cultura")

df_reg_cult = (
    df_filtrado
    .groupby(['regiao', 'cultura'])['produtividade_kg_ha']
    .mean()
    .reset_index()
)

fig_reg_cult = px.bar(
    df_reg_cult,
    x='regiao',
    y='produtividade_kg_ha',
    color='cultura',
    barmode='group',
    color_discrete_map=PALETA_CULTURAS,
    labels={'regiao': 'Região', 'produtividade_kg_ha': 'Produtividade (kg/ha)', 'cultura': 'Cultura'},
    title=''
)
fig_reg_cult.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color=CORES['texto'],
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    xaxis=dict(gridcolor='#333'),
    yaxis=dict(gridcolor='#333'),
    height=420,
)
st.plotly_chart(fig_reg_cult, use_container_width=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# GRÁFICO 3 — Mecanização vs Produtividade (Box Plot)
# ==============================================================
st.markdown("### ⚙️ Produtividade por Nível de Mecanização")

# Ordem natural da mecanização
ordem_mec = ['Muito Baixo', 'Baixo', 'Médio', 'Alto', 'Muito Alto']
df_filtrado['mecanizacao_cat'] = pd.Categorical(
    df_filtrado['mecanizacao'], categories=ordem_mec, ordered=True
)

fig_mec = px.box(
    df_filtrado,
    x='mecanizacao_cat',
    y='produtividade_kg_ha',
    color='mecanizacao',
    color_discrete_map=PALETA_MECANIZACAO,
    labels={'mecanizacao_cat': 'Mecanização', 'produtividade_kg_ha': 'Produtividade (kg/ha)'},
    title=''
)
fig_mec.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color=CORES['texto'],
    showlegend=False,
    xaxis=dict(gridcolor='#333'),
    yaxis=dict(gridcolor='#333'),
    height=420,
)
st.plotly_chart(fig_mec, use_container_width=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# GRÁFICO 4 — Municípios Produtores por Estado (Barras Horizontais)
# ==============================================================
st.markdown("### 📊 Número de Municípios Produtores por Estado")

df_mun = (
    df_filtrado
    .groupby(['estado', 'regiao'])['municipios_produtores']
    .sum()
    .reset_index()
    .sort_values('municipios_produtores', ascending=True)
)

fig_mun = px.bar(
    df_mun,
    y='estado',
    x='municipios_produtores',
    color='regiao',
    orientation='h',
    labels={'estado': 'Estado', 'municipios_produtores': 'Municípios Produtores', 'regiao': 'Região'},
    title=''
)
fig_mun.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color=CORES['texto'],
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    xaxis=dict(gridcolor='#333'),
    yaxis=dict(gridcolor='#333'),
    height=500,
)
st.plotly_chart(fig_mun, use_container_width=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# GRÁFICO 5 — Mapa de Calor: Produtividade por Estado × Cultura
# ==============================================================
st.markdown("### 🔥 Produtividade Média por Estado e Cultura")

df_heatmap = (
    df_filtrado
    .groupby(['estado', 'cultura'])['produtividade_kg_ha']
    .mean()
    .reset_index()
    .pivot(index='estado', columns='cultura', values='produtividade_kg_ha')
)

# Garantir que todas as culturas apareçam
for c in culturas_selecionadas:
    if c not in df_heatmap.columns:
        df_heatmap[c] = None

fig_heatmap = px.imshow(
    df_heatmap.values,
    x=df_heatmap.columns.tolist(),
    y=df_heatmap.index.tolist(),
    color_continuous_scale=['#1B5E20', '#43A047', '#A5D6A7', '#F9A825', '#FF8F00'],
    labels={'x': 'Cultura', 'y': 'Estado', 'color': 'Prod. (kg/ha)'},
    text_auto='.0f',
    title=''
)
fig_heatmap.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color=CORES['texto'],
    height=500,
)
st.plotly_chart(fig_heatmap, use_container_width=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# GRÁFICO 6 — Dispersão: Municípios vs Produtividade
# ==============================================================
st.markdown("### 🌿 Relação: Municípios Produtores × Produtividade")

fig_disp = px.scatter(
    df_filtrado,
    x='municipios_produtores',
    y='produtividade_kg_ha',
    color='cultura',
    color_discrete_map=PALETA_CULTURAS,
    size='municipios_produtores',
    size_max=25,
    hover_data=['estado', 'regiao', 'mecanizacao'],
    labels={
        'municipios_produtores': 'Municípios Produtores',
        'produtividade_kg_ha': 'Produtividade (kg/ha)',
        'cultura': 'Cultura'
    },
    title=''
)
# Adicionar linha de tendência por cultura
for cultura in df_filtrado['cultura'].unique():
    df_cult = df_filtrado[df_filtrado['cultura'] == cultura]
    if len(df_cult) > 2:
        z = np.polyfit(df_cult['municipios_produtores'], df_cult['produtividade_kg_ha'], 1)
        p = np.poly1d(z)
        x_range = np.linspace(df_cult['municipios_produtores'].min(), df_cult['municipios_produtores'].max(), 50)
        fig_disp.add_trace(go.Scatter(
            x=x_range, y=p(x_range),
            mode='lines',
            line=dict(color=PALETA_CULTURAS.get(cultura, '#888'), dash='dash', width=2),
            name=f'{cultura} (tendência)',
            showlegend=True
        ))

fig_disp.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color=CORES['texto'],
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    xaxis=dict(gridcolor='#333'),
    yaxis=dict(gridcolor='#333'),
    height=500,
)
st.plotly_chart(fig_disp, use_container_width=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# TABELA DE DADOS BRUTOS FILTRADOS
# ==============================================================
st.markdown("### 📋 Dados Brutos Filtrados")

col_display = st.columns([3, 1])
with col_display[1]:
    n_linhas = st.selectbox("Linhas por página:", [10, 25, 50, 100], index=1)

df_display = df_filtrado.copy()
df_display = df_display.rename(columns={
    'n_obs': 'Nº Obs.',
    'estado': 'Estado (UF)',
    'cultura': 'Cultura Principal',
    'municipios_produtores': 'Municípios Produtores',
    'produtividade_kg_ha': 'Produtividade (kg/ha)',
    'mecanizacao': 'Nível de Mecanização',
    'regiao': 'Região Geográfica',
    'fonte': 'Fonte Principal'
})
if 'mecanizacao_cat' in df_display.columns:
    df_display = df_display.drop(columns=['mecanizacao_cat'])

st.dataframe(
    df_display.head(n_linhas),
    use_container_width=True,
    height=400
)

# Botão para download dos dados filtrados
csv = df_display.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Baixar dados filtrados (CSV)",
    data=csv,
    file_name="dados_agronegocio_filtrados.csv",
    mime="text/csv",
)

# ==============================================================
# RODAPÉ
# ==============================================================
st.markdown(
    '<div class="footer">'
    '🌱 Projeto Ir Além — FIAP | Dashboard Agrícola | '
    'Dados reais do agronegócio brasileiro — Safra 2023/24<br>'
    'Fontes: CONAB · IBGE/PAM · MAPA · Embrapa · INPE · CNA Brasil<br>'
    'Desenvolvido com Streamlit + Plotly'
    '</div>',
    unsafe_allow_html=True
)
