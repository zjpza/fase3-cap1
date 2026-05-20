"""
app.py — Dashboard Agrícola Interativo
Projeto: Ir Além — FIAP
Visualização de dados de umidade, pH, Fósforo/Potássio e produtividade.
Utiliza Streamlit + Plotly para gráficos interativos.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from dados import gerar_dados_agricolas

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
    'Café': '#795548',
}

PALETA_SEQUENCIAL = ['#1B5E20', '#2E7D32', '#388E3C', '#43A047',
                     '#66BB6A', '#81C784', '#A5D6A7', '#C8E6C9']

# ==============================================================
# CSS customizado para visual profissional
# ==============================================================
st.markdown("""
<style>
    /* Cabeçalho principal */
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

    /* Cards de métricas */
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

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a1a0a 0%, #112211 100%);
    }
    section[data-testid="stSidebar"] .stMarkdown h2 {
        color: #66BB6A;
    }

    /* Separadores */
    .separator {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #2E7D32, transparent);
        margin: 2rem 0;
    }

    /* Rodapé */
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
    """Carrega e faz cache dos dados simulados."""
    return gerar_dados_agricolas(n_registros=1500)

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

    # Filtro por período
    st.markdown("### 📅 Período")
    data_min = df['data'].min().date()
    data_max = df['data'].max().date()
    periodo = st.date_input(
        "Selecione o intervalo:",
        value=(data_min, data_max),
        min_value=data_min,
        max_value=data_max,
        label_visibility="collapsed"
    )

    st.markdown("---")

    # Filtro por tipo de solo
    st.markdown("### 🏔️ Tipo de Solo")
    solos_disponiveis = sorted(df['tipo_solo'].unique())
    solos_selecionados = st.multiselect(
        "Selecione os tipos de solo:",
        options=solos_disponiveis,
        default=solos_disponiveis,
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; color:#555; font-size:0.8rem;'>"
        "🌱 FIAP — Ir Além<br>Dashboard Agrícola v1.0"
        "</div>",
        unsafe_allow_html=True
    )

# ==============================================================
# Aplicar filtros ao DataFrame
# ==============================================================
# Garantir que o período tenha duas datas
if isinstance(periodo, tuple) and len(periodo) == 2:
    data_inicio, data_fim = periodo
else:
    data_inicio, data_fim = data_min, data_max

df_filtrado = df[
    (df['cultura'].isin(culturas_selecionadas)) &
    (df['regiao'].isin(regioes_selecionadas)) &
    (df['tipo_solo'].isin(solos_selecionados)) &
    (df['data'].dt.date >= data_inicio) &
    (df['data'].dt.date <= data_fim)
].copy()

# ==============================================================
# CABEÇALHO PRINCIPAL
# ==============================================================
st.markdown(
    '<div class="main-header">'
    '<h1>🌾 Ir Além — Dashboard Agrícola</h1>'
    '<p>Projeto acadêmico FIAP — Visualização interativa de dados de solo, '
    'clima e produtividade para Soja, Milho e Café no agronegócio brasileiro.</p>'
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
        f'<div class="valor">{len(df_filtrado):,}</div></div>',
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        f'<div class="metric-card"><h3>💧 Umidade Média</h3>'
        f'<div class="valor">{df_filtrado["umidade"].mean():.1f}%</div></div>',
        unsafe_allow_html=True
    )
with col3:
    st.markdown(
        f'<div class="metric-card"><h3>🧪 pH Médio</h3>'
        f'<div class="valor">{df_filtrado["pH"].mean():.2f}</div></div>',
        unsafe_allow_html=True
    )
with col4:
    st.markdown(
        f'<div class="metric-card"><h3>🌿 P Médio (mg/dm³)</h3>'
        f'<div class="valor">{df_filtrado["fosforo"].mean():.1f}</div></div>',
        unsafe_allow_html=True
    )
with col5:
    st.markdown(
        f'<div class="metric-card"><h3>🏆 Prod. Média (kg/ha)</h3>'
        f'<div class="valor">{df_filtrado["produtividade"].mean():,.0f}</div></div>',
        unsafe_allow_html=True
    )

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# GRÁFICO 1 — Variação de Umidade ao Longo do Tempo (Linha)
# ==============================================================
st.markdown("### 💧 Variação da Umidade do Solo ao Longo do Tempo")

# Agrupar por mês e cultura para suavizar a visualização
df_umidade = (
    df_filtrado
    .assign(mes=df_filtrado['data'].dt.to_period('M').astype(str))
    .groupby(['mes', 'cultura'])['umidade']
    .mean()
    .reset_index()
)

fig_umidade = px.line(
    df_umidade,
    x='mes',
    y='umidade',
    color='cultura',
    color_discrete_map=PALETA_CULTURAS,
    markers=True,
    labels={'mes': 'Mês', 'umidade': 'Umidade Média (%)', 'cultura': 'Cultura'},
    title=''
)
fig_umidade.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color=CORES['texto'],
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    xaxis=dict(gridcolor='#333', tickangle=-45),
    yaxis=dict(gridcolor='#333', title='Umidade (%)'),
    hovermode='x unified',
    height=420,
)
st.plotly_chart(fig_umidade, use_container_width=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# GRÁFICO 2 — pH Médio por Tipo de Solo (Barras)
# ==============================================================
st.markdown("### 🧪 pH Médio por Tipo de Solo")

df_ph = (
    df_filtrado
    .groupby(['tipo_solo', 'cultura'])['pH']
    .mean()
    .reset_index()
)

fig_ph = px.bar(
    df_ph,
    x='tipo_solo',
    y='pH',
    color='cultura',
    barmode='group',
    color_discrete_map=PALETA_CULTURAS,
    labels={'tipo_solo': 'Tipo de Solo', 'pH': 'pH Médio', 'cultura': 'Cultura'},
    title=''
)
fig_ph.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color=CORES['texto'],
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    xaxis=dict(gridcolor='#333'),
    yaxis=dict(gridcolor='#333', range=[4, 7.5]),
    height=420,
)
# Linha de referência para pH ideal
fig_ph.add_hline(y=6.0, line_dash="dash", line_color="#66BB6A",
                 annotation_text="pH ideal ≈ 6.0", annotation_position="top right")
st.plotly_chart(fig_ph, use_container_width=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# GRÁFICO 3 — Dispersão P/K vs Produtividade
# ==============================================================
st.markdown("### 🌿 Relação Fósforo/Potássio × Produtividade")

# Criar coluna P+K combinada
df_filtrado['pk_index'] = df_filtrado['fosforo'] + df_filtrado['potassio'] * 0.1

fig_dispersao = px.scatter(
    df_filtrado,
    x='pk_index',
    y='produtividade',
    color='cultura',
    color_discrete_map=PALETA_CULTURAS,
    opacity=0.6,
    size='umidade',
    size_max=12,
    labels={
        'pk_index': 'Índice P/K (P + K×0.1)',
        'produtividade': 'Produtividade (kg/ha)',
        'cultura': 'Cultura',
        'umidade': 'Umidade (%)'
    },
    title=''
)
# Adicionar linha de tendência
for cultura in df_filtrado['cultura'].unique():
    df_cult = df_filtrado[df_filtrado['cultura'] == cultura]
    if len(df_cult) > 2:
        z = np.polyfit(df_cult['pk_index'], df_cult['produtividade'], 1)
        p = np.poly1d(z)
        x_range = np.linspace(df_cult['pk_index'].min(), df_cult['pk_index'].max(), 50)
        fig_dispersao.add_trace(go.Scatter(
            x=x_range, y=p(x_range),
            mode='lines',
            line=dict(color=PALETA_CULTURAS.get(cultura, '#888'), dash='dash', width=2),
            name=f'{cultura} (tendência)',
            showlegend=True
        ))

fig_dispersao.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color=CORES['texto'],
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    xaxis=dict(gridcolor='#333'),
    yaxis=dict(gridcolor='#333'),
    height=500,
)
st.plotly_chart(fig_dispersao, use_container_width=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# GRÁFICO 4 — Bônus: Distribuição por Região (Mapa de Calor)
# ==============================================================
st.markdown("### 📍 Produtividade Média por Região e Cultura")

df_heatmap = (
    df_filtrado
    .groupby(['regiao', 'cultura'])['produtividade']
    .mean()
    .reset_index()
    .pivot(index='regiao', columns='cultura', values='produtividade')
)

fig_heatmap = px.imshow(
    df_heatmap.values,
    x=df_heatmap.columns.tolist(),
    y=df_heatmap.index.tolist(),
    color_continuous_scale=['#1B5E20', '#43A047', '#A5D6A7', '#F9A825', '#FF8F00'],
    labels={'x': 'Cultura', 'y': 'Região', 'color': 'Prod. (kg/ha)'},
    text_auto='.0f',
    title=''
)
fig_heatmap.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color=CORES['texto'],
    height=380,
)
st.plotly_chart(fig_heatmap, use_container_width=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# ==============================================================
# TABELA DE DADOS BRUTOS FILTRADOS
# ==============================================================
st.markdown("### 📋 Dados Brutos Filtrados")

# Configuração de exibição
col_display = st.columns([3, 1])
with col_display[1]:
    n_linhas = st.selectbox("Linhas por página:", [10, 25, 50, 100], index=1)

# Formatar dados para exibição
df_display = df_filtrado.copy()
df_display['data'] = df_display['data'].dt.strftime('%d/%m/%Y')
df_display = df_display.rename(columns={
    'data': 'Data', 'cultura': 'Cultura', 'regiao': 'Região',
    'tipo_solo': 'Tipo de Solo', 'umidade': 'Umidade (%)',
    'pH': 'pH', 'fosforo': 'Fósforo (mg/dm³)',
    'potassio': 'Potássio (mg/dm³)', 'temperatura': 'Temp. (°C)',
    'precipitacao': 'Precip. (mm)', 'produtividade': 'Prod. (kg/ha)'
})
# Remover coluna auxiliar se existir
if 'pk_index' in df_display.columns:
    df_display = df_display.drop(columns=['pk_index'])

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
    file_name="dados_agricolas_filtrados.csv",
    mime="text/csv",
)

# ==============================================================
# RODAPÉ
# ==============================================================
st.markdown(
    '<div class="footer">'
    '🌱 Projeto Ir Além — FIAP | Dashboard Agrícola | '
    'Dados simulados para fins acadêmicos<br>'
    'Desenvolvido com Streamlit + Plotly'
    '</div>',
    unsafe_allow_html=True
)
