#correlação 
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df = pd.read_csv("C:/Users/scleber/OneDrive/Desktop/Projeto Análise de Dados/Movie and Emotional Attachment Survey.csv")


corr = df.corr(numeric_only=True)
corr.to_csv("matriz_correlacao.csv")

corr_scores = df[["Emotional Storytelling Score", "Audience Attachment Score"]].corr()
print(corr_scores)

