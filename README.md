
#  Exploratory Data Analysis of ENEM 2020 Microdata

##  Objective

This project performs an exploratory data analysis of the ENEM 2020 microdata, aiming to understand how socioeconomic factors such as income and geographic region, influence student performance.

The project uses Python, SQL (SQLite), and data visualization techniques.

---

##  Dataset

The dataset comes from the official ENEM 2020 microdata provided by INEP.

Source: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

Due to the large size of the dataset, a sample was created for analysis.

##  Technologies Used

- Python
- Pandas
- SQLite
- SQL (Jupyter Notebook)
- Matplotlib
- VS Code
- Jupyter Notebook

##  Project Structure

```txt
Projeto-Análise-de-Dados/
│
├── .venv/
│   └── (ambiente virtual Python)
│
├── DADOS/
│   ├── MICRODADOS_ENEM_2020.csv
│   ├── enem_amostra.csv
│   ├── enem.db
│   └── Dicionário_Microdados_Enem_2020.ods
│
├── Imagens/
│   ├── income.png
│   └── region.png
│
├── Notebooks/
│   ├── 01_criation_database.ipynb
│   ├── 02_region_analysis.ipynb
│   ├── 03_income_analysis.ipynb
│
├── SQL/
│   ├── 01_region_analysis_SQL.ipynb
│   ├── 02_income_analysis_SQL.ipynb
│   └── enem.db
│
├── reports/
│   └── project_presentation.pdf
│
├── README.md
└── requirements.txt

```
## Data Processing
A random sample of the dataset was created due to its large size. The data was then stored in a SQLite database to allow SQL-based analysis.

## Regional Analysis
Students were grouped into Brazilian regions based on their state (UF):

North
Northeast
Southeast
South
Center-West

![Gráfico](imagens/region.png)

## Income Analysis
Students were grouped based on their income.
![Gráfico](imagens/income.png)

## Key Analyses
Income vs performance
Household size vs performance
Regional differences in scores

## Key Insights
Socioeconomic factors have a strong influence on student performance in the ENEM exam.

## How to Run
```bash
pip install -r requirements.txt
```
## Author

Renan Barreto Sampaio