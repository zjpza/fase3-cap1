# 🌾 Ir Além — Dashboard Agrícola Interativo

**Projeto acadêmico FIAP** — Visualização interativa de dados reais do agronegócio brasileiro (Safra 2023/24), provenientes de fontes oficiais como CONAB, IBGE/PAM, MAPA e Embrapa. O dashboard analisa produtividade, mecanização e municípios produtores por estado, região e cultura.

---

## 📋 Sobre o Projeto

Este dashboard foi desenvolvido como parte do projeto **"Ir Além"** da FIAP, com o objetivo de visualizar e analisar dados reais do agronegócio brasileiro de forma interativa. O sistema permite:

- **Filtros interativos** por cultura, região, mecanização e estado
- **Gráfico de barras** — Produtividade média por cultura
- **Gráfico de barras agrupadas** — Produtividade por região e cultura
- **Box plot** — Produtividade por nível de mecanização
- **Barras horizontais** — Municípios produtores por estado
- **Mapa de calor** — Produtividade média por estado e cultura
- **Dispersão com tendência** — Relação entre municípios produtores e produtividade
- **Tabela interativa** com dados brutos filtrados e opção de download

### Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.10+ | Linguagem principal |
| Streamlit 1.30+ | Framework para o dashboard web |
| Plotly 5.18+ | Gráficos interativos |
| Pandas 2.1+ | Manipulação de dados |
| NumPy | Geração de dados simulados |

---

## 🚀 Como Instalar e Rodar

### Pré-requisitos

- Python 3.10 ou superior instalado
- pip (gerenciador de pacotes Python)
- `openpyxl` instalado (para leitura do Excel — já incluso no `requirements.txt`)

### Passo a Passo Completo

#### 1. Clone ou baixe o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd ir-alem-dashboard
```

Ou baixe o `.zip`, extraia e entre na pasta do projeto.

#### 2. Crie um ambiente virtual (recomendado)

Isso isola as dependências e evita conflitos com outros projetos.

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

> 💡 **Dica:** Quando o ambiente estiver ativado, seu terminal mostrará `(venv)` no início da linha.

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Isso instala: `streamlit`, `plotly`, `pandas`, `numpy`, `openpyxl`.

#### 4. Verifique se o arquivo Excel está presente

O `dados.py` lê o arquivo `agronegocio_brasil_2023_24.xlsx` automaticamente. Confirme que ele está na mesma pasta do `app.py`.

```bash
ls
# ou no Windows: dir
```

Você deve ver:
```
app.py
dados.py
agronegocio_brasil_2023_24.xlsx
requirements.txt
```

#### 5. Execute o dashboard

```bash
streamlit run app.py
```

#### 6. Acesse no navegador

O Streamlit abrirá automaticamente em `http://localhost:8501`. Se não abrir, copie o link do terminal e cole no navegador.

---

### 🛠️ Resolução de Problemas Comuns

| Problema | Solução |
|---|---|
| `ModuleNotFoundError: No module named 'openpyxl'` | Rode `pip install openpyxl` |
| `FileNotFoundError: agronegocio_brasil_2023_24.xlsx` | Confirme que o `.xlsx` está na mesma pasta dos `.py` |
| Porta 8501 ocupada | Use `streamlit run app.py --server.port 8502` |
| Ambiente virtual não ativa | Confirme o comando de ativação para seu sistema operacional |

---

### 🔄 Desativar o ambiente virtual

Quando terminar, desative com:

```bash
deactivate
```

---

## 📁 Estrutura de Arquivos

```
ir-alem-dashboard/
├── app.py                             # Dashboard principal (Streamlit)
├── dados.py                           # Módulo de leitura de dados reais do Excel
├── agronegocio_brasil_2023_24.xlsx    # Base de dados reais (Safra 2023/24)
├── requirements.txt                   # Dependências do projeto
└── README.md                          # Este arquivo
```

---

## 📸 Como Capturar Prints da Interface

Para incluir screenshots no relatório ou apresentação:

### Método 1 — Print Screen do Sistema
1. Execute o dashboard com `streamlit run app.py`
2. Navegue pelas diferentes seções
3. Use os atalhos do sistema:
   - **macOS:** `Cmd + Shift + 4` (selecionar área) ou `Cmd + Shift + 3` (tela inteira)
   - **Windows:** `Win + Shift + S` (Ferramenta de Recorte)
   - **Linux:** `PrtSc` ou `Shift + PrtSc`

### Método 2 — DevTools do Navegador
1. Pressione `F12` para abrir as ferramentas de desenvolvedor
2. Clique no ícone de dispositivo (📱) para simular resoluções
3. Use `Ctrl + Shift + P` → "Capture full size screenshot"

### Prints Recomendados para o Relatório
1. **Visão geral** — Dashboard completo com todos os gráficos
2. **Filtros ativos** — Sidebar com filtros selecionados
3. **Gráfico de produtividade por cultura** — Barras comparativas
4. **Gráfico de produtividade por região** — Barras agrupadas por cultura
5. **Gráfico de mecanização** — Box plot por nível de mecanização
6. **Gráfico de municípios** — Barras horizontais por estado
7. **Mapa de calor** — Produtividade por estado e cultura
8. **Gráfico de dispersão** — Municípios produtores vs produtividade
9. **Tabela de dados** — Dados brutos filtrados

---

## 📊 Dados Utilizados

Os dados são **reais** e provenientes da base **"Agronegócio Brasileiro — Safra 2023/2024"**, compilada a partir de fontes oficiais:

- **CONAB** — Companhia Nacional de Abastecimento
- **IBGE/PAM** — Pesquisa Agrícola Municipal
- **MAPA** — Ministério da Agricultura, Pecuária e Abastecimento
- **Embrapa** — Empresa Brasileira de Pesquisa Agropecuária
- **INPE** — Instituto Nacional de Pesquisas Espaciais
- **CNA Brasil** — Confederação da Agricultura e Pecuária do Brasil

### Variáveis da Base

| Variável | Tipo | Descrição |
|---|---|---|
| Estado (UF) | Qualitativa Nominal | Estado brasileiro com sigla |
| Cultura Principal | Qualitativa Nominal | Cultura agrícola (Soja, Milho, Café, Cana-de-açúcar, etc.) |
| Nº de Municípios Produtores | Quantitativa Discreta | Contagem de municípios |
| Produtividade (kg/ha) | Quantitativa Contínua | Produtividade média |
| Nível de Mecanização | Qualitativa Ordinal | Muito Baixo → Baixo → Médio → Alto → Muito Alto |
| Região Geográfica | Qualitativa Nominal | Norte, Nordeste, Centro-Oeste, Sudeste, Sul |
| Fonte Principal | Qualitativa Nominal | Órgão de origem do dado |

**Total:** 35 registros | **Culturas:** 11 | **Regiões:** 5

---

## 🎥 Link do Vídeo de Apresentação

> ⚠️ **Insira aqui o link do vídeo de apresentação do projeto:**
>
> `[INSERIR LINK DO VÍDEO AQUI]`

---

## 👥 Equipe

| Nome | RM | GitHub |
|---|---|---|
| Henrique Sanches Silva | 570527 | [@HenriqueSanchesSilva](https://github.com/HenriqueSanchesSilva) |
| João Pedro Zavanela Andreu | 570231 | [@zjpza](https://github.com/zjpza) |
| Kayck Gabriel Evangelista da Silva | 572331 | [@Kayckxz](https://github.com/Kayckxz) |
| Luis Henrique Laurentino Boschi | 571352 | [@lhboschi](https://github.com/lhboschi) |
| Patrick Borges de Melo | 574030 | [@Trickmelo](https://github.com/Trickmelo) |

---

## 📄 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
