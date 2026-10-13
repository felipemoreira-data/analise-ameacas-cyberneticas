# Análise de Ameaças Cibernéticas

Webapp interativo para análise exploratória de dados sobre ameaças cibernéticas globais, com visualizações voltadas à identificação de padrões, tendências temporais e impactos financeiros.

## Funcionalidades

* **Visão Geral:** panorama dos registros de ameaças cibernéticas.
* **Impacto Financeiro:** análise dos prejuízos econômicos associados aos ataques.
* **Usuários Afetados:** exploração dos impactos sobre usuários e organizações.
* **Tempo de Resolução:** análise do tempo necessário para solucionar incidentes.
* **Tendências Temporais:** evolução das ameaças ao longo do tempo.
* **Insights:** síntese dos principais indicadores e padrões identificados nos dados.

## Tecnologias

* Python
* Pandas
* Streamlit
* Plotly

## Estrutura do Projeto

```text
analise-ameacas-ciberneticas/
├── data/                 # Base de dados
├── pages/                # Páginas de análise
├── streamlit/            # Configurações do Streamlit
├── styles/               # Estilos personalizados
├── Principal.py          # Aplicação principal
└── requirements.txt      # Dependências
```

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/felipemoreira-data/analise-ameacas-ciberneticas.git
   ```

2. Entre na pasta do projeto:

   ```bash
   cd analise-ameacas-ciberneticas
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:

   ```bash
   streamlit run Principal.py
   ```

## Objetivo

Explorar dados de ameaças cibernéticas por meio de visualizações interativas, facilitando a compreensão de seus impactos e tendências.

## Autor

Felipe Melo Moreira Nunes
