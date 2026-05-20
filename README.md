# 🌾 Ir Além — Dashboard Agrícola Interativo

**Projeto acadêmico FIAP** — Visualização interativa de dados reais do agronegócio brasileiro (Safra 2023/24), provenientes de fontes oficiais como CONAB, IBGE/PAM, MAPA e Embrapa. O dashboard analisa produtividade, mecanização e municípios produtores por estado, região e cultura.

---

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte do **PBL (Project-Based Learning)** da FIAP — Fase 3, Capítulo 1, da disciplina de Inteligência Artificial. A startup fictícia **FarmTech Solutions** atua como consultoria em soluções para o agronegócio, uma das áreas mais promissoras para aplicação de IA no Brasil.

O repositório contempla:
- **Entrega obrigatória:** Banco de dados Oracle com carga e consultas SQL
- **Programa Ir Além (opcional):** Dashboard interativo em Python (Streamlit + Plotly)

O sistema permite:

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
| Streamlit | Framework para o dashboard web |
| Plotly | Gráficos interativos |
| Pandas | Manipulação de dados |
| NumPy | Cálculos e linhas de tendência |

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

#### 4. Adicione a base de dados Excel

> **O arquivo `agronegocio_brasil_2023_24.xlsx` não está versionado no repositório.**  
> Baixe-o do material da disciplina ou solicite ao professor, e coloque na pasta `data/`.

```bash
ls data/
# ou no Windows: dir data\
```

Você deve ver:
```
agronegocio_brasil_2023_24.xlsx   <-- adicionar manualmente
```

#### 5. Execute o dashboard

```bash
streamlit run src/app.py
```

#### 6. Acesse no navegador

O Streamlit abrirá automaticamente em `http://localhost:8501`. Se não abrir, copie o link do terminal e cole no navegador.

---

### 🛠️ Resolução de Problemas Comuns

| Problema | Solução |
|---|---|
| `ModuleNotFoundError: No module named 'openpyxl'` | Rode `pip install openpyxl` |
| `FileNotFoundError: agronegocio_brasil_2023_24.xlsx` | Confirme que o `.xlsx` está na pasta `data/` |
| `ImportError: No module named src.dados` | Execute de dentro da raiz do projeto (`cd FIAP/Fase\ 3\ Cap\ 1`)
| Porta 8501 ocupada | Use `streamlit run src/app.py --server.port 8502` |
| Ambiente virtual não ativa | Confirme o comando de ativação para seu sistema operacional |

---

## 🗄️ Entrega Obrigatória — Oracle SQL Developer

### Passo a passo completo

#### 1. Baixe o Oracle SQL Developer

Acesse https://www.oracle.com/database/sqldeveloper/technologies/download/ e baixe a versão para seu sistema operacional (Windows, Linux ou Mac). Extraia o arquivo ZIP e execute o programa `sqldeveloper`.

#### 2. Crie a conexão com o banco da FIAP

Clique no ícone **"Nova Conexão"** (símbolo de + verde) e preencha:

| Campo | Valor |
|---|---|
| Nome da Conexão | `FIAP` (ou qualquer nome) |
| Nome do Usuário | `RM12345` (use **seu RM** com as letras RM) |
| Senha | `DDMMYY` (sua data de nascimento com 6 dígitos) |
| Host | `oracle.fiap.com.br` |
| Porta | `1521` |
| SID | `ORCL` |

Clique em **"Testar"**. Se aparecer "Sucesso", clique em **"Salvar"** e depois **"Conectar"**.

> Se der erro de conta bloqueada, entre em contato com o suporte da FIAP.  
> Se der erro de usuário/senha, confirme que digitou o RM com as letras `RM` e sem espaços.

#### 3. Execute o script SQL

No painel esquerdo, com a conexão `FIAP` aberta, localize **"Tabelas (Filtrado)"**. Clique com o botão direito e selecione **"Abrir Editor SQL"** (ou use `Ctrl + N`).

Cole o conteúdo do arquivo `sql/oracle_insert_dados.sql` e aperte `Ctrl + Enter` para executar tudo.

O script executa automaticamente:
```sql
DROP TABLE DADOS_AGRICOLAS;
CREATE TABLE DADOS_AGRICOLAS (...);
INSERT INTO DADOS_AGRICOLAS VALUES (1, 'RS', 'Soja', ...);
-- (35 INSERTs no total)
COMMIT;
SELECT * FROM DADOS_AGRICOLAS;
SELECT COUNT(*) AS TOTAL_REGISTROS FROM DADOS_AGRICOLAS;
SELECT REGIAO, AVG(PRODUTIVIDADE_KG_HA) AS PRODUTIVIDADE_MEDIA FROM DADOS_AGRICOLAS GROUP BY REGIAO;
SELECT CULTURA, SUM(MUNICIPIOS_PRODUTORES) AS TOTAL_MUNICIPIOS FROM DADOS_AGRICOLAS GROUP BY CULTURA ORDER BY TOTAL_MUNICIPIOS DESC;
```

#### 4. Valide que os dados foram inseridos

Na aba "Resultado" deve aparecer:
- `Tabela DADOS_AGRICOLAS criada`
- `35 linhas inseridas`
- A tabela com todos os registros listados
- O `COUNT(*)` retornando **35**

#### 5. Consultas SQL para explorar os dados

Abaixo estão consultas adicionais que você pode rodar no editor SQL (`Ctrl + Enter`):

```sql
-- 1. Listar todas as culturas distintas
SELECT DISTINCT CULTURA FROM DADOS_AGRICOLAS ORDER BY CULTURA;

-- 2. Produtividade média por estado (top 10)
SELECT ESTADO, AVG(PRODUTIVIDADE_KG_HA) AS PROD_MEDIA
FROM DADOS_AGRICOLAS
GROUP BY ESTADO
ORDER BY PROD_MEDIA DESC;

-- 3. Estados com mecanização 'Muito Alto'
SELECT ESTADO, CULTURA, PRODUTIVIDADE_KG_HA
FROM DADOS_AGRICOLAS
WHERE MECANIZACAO = 'Muito Alto'
ORDER BY PRODUTIVIDADE_KG_HA DESC;

-- 4. Total de municípios produtores por região
SELECT REGIAO, SUM(MUNICIPIOS_PRODUTORES) AS TOTAL_MUNICIPIOS
FROM DADOS_AGRICOLAS
GROUP BY REGIAO
ORDER BY TOTAL_MUNICIPIOS DESC;

-- 5. Culturas com produtividade acima de 10.000 kg/ha
SELECT CULTURA, ESTADO, PRODUTIVIDADE_KG_HA
FROM DADOS_AGRICOLAS
WHERE PRODUTIVIDADE_KG_HA > 10000
ORDER BY PRODUTIVIDADE_KG_HA DESC;
```

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
├── src/
│   ├── app.py                         # Dashboard principal (Streamlit)
│   └── dados.py                       # Módulo de leitura de dados reais do Excel
├── data/
│   └── agronegocio_brasil_2023_24.xlsx # Base de dados reais (Safra 2023/24)
├── sql/
│   └── oracle_insert_dados.sql        # Script de INSERTs para Oracle DB
├── assets/
│   └── (prints, imagens, vídeos)      # Recursos visuais do projeto
├── requirements.txt                   # Dependências do projeto
└── README.md                          # Este arquivo
```

---

## 📸 Como Capturar Prints da Interface

Para incluir screenshots no relatório ou apresentação:

### Método 1 — Print Screen do Sistema
1. Execute o dashboard com `streamlit run src/app.py`
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

Projeto acadêmico — FIAP © 2025
