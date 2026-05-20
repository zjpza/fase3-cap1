# 🌾 Ir Além — Dashboard Agrícola Interativo

**Projeto acadêmico FIAP** — Visualização interativa de dados agrícolas coletados em fases anteriores do projeto, focando em variáveis de solo (umidade, pH, fósforo, potássio) e produtividade para as culturas de Soja, Milho e Café.

---

## 📋 Sobre o Projeto

Este dashboard foi desenvolvido como parte do projeto **"Ir Além"** da FIAP, com o objetivo de visualizar e analisar dados agrícolas de forma interativa. O sistema permite:

- **Filtros interativos** por cultura, região, período e tipo de solo
- **Gráfico de linha** — Variação da umidade do solo ao longo do tempo
- **Gráfico de barras** — Comparação de pH médio por tipo de solo
- **Gráfico de dispersão** — Relação entre Fósforo/Potássio e produtividade
- **Mapa de calor** — Produtividade média por região e cultura
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

### Passo a Passo

1. **Clone ou baixe o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd ir-alem-dashboard
   ```

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   # No macOS/Linux:
   source venv/bin/activate
   # No Windows:
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o dashboard:**
   ```bash
   streamlit run app.py
   ```

5. **Acesse no navegador:**
   O Streamlit abrirá automaticamente em `http://localhost:8501`

---

## 📁 Estrutura de Arquivos

```
ir-alem-dashboard/
├── app.py              # Dashboard principal (Streamlit)
├── dados.py            # Módulo de geração de dados simulados
├── requirements.txt    # Dependências do projeto
└── README.md           # Este arquivo
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
3. **Gráfico de umidade** — Variação temporal por cultura
4. **Gráfico de pH** — Comparação por tipo de solo
5. **Gráfico de dispersão P/K** — Com linhas de tendência
6. **Tabela de dados** — Dados brutos filtrados

---

## 📊 Dados Utilizados

Os dados são **simulados** pelo módulo `dados.py`, mas seguem parâmetros realistas baseados em:

- Faixas de pH típicas para Latossolo, Argissolo, etc.
- Níveis de fósforo e potássio comuns em lavouras brasileiras
- Variação sazonal de umidade e precipitação
- Produtividades médias de soja, milho e café no Brasil

**Total:** 1.500 registros | **Período:** Jan/2024 a Dez/2025

---

## 🎥 Link do Vídeo de Apresentação

> ⚠️ **Insira aqui o link do vídeo de apresentação do projeto:**
>
> `[INSERIR LINK DO VÍDEO AQUI]`

---

## 👥 Equipe

- <a href="https://github.com/HenriqueSanchesSilva">Henrique Sanches Silva — RM 570527</a>
- <a href="https://github.com/zjpza">João Pedro Zavanela Andreu — RM 570231</a>
- <a href="https://github.com/Kayckxz">Kayck Gabriel Evangelista da Silva — RM 572331</a>
- <a href="https://github.com/lhboschi">Luis Henrique Laurentino Boschi — RM 571352</a>
- <a href="https://github.com/Trickmelo">Patrick Borges de Melo — RM 574030</a>

---

## 📄 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
