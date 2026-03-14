import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/scleber/OneDrive/Desktop/Projeto Análise de Dados/Movie and Emotional Attachment Survey.csv")
#Distribuição por gênero 
df["Gender"].value_counts()
df["Gender"].value_counts().plot(kind="bar")
plt.title("Distribuição por gênero")
plt.show()