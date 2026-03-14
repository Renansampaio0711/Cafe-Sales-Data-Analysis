#Relação entre storytelling e apego emocional 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/scleber/OneDrive/Desktop/Projeto Análise de Dados/Movie and Emotional Attachment Survey.csv")
# Emotional Storytelling Score X  Audience Attachment Score  
plt.scatter(df["Emotional Storytelling Score"], df["Audience Attachment Score"])
plt.xlabel("Storytelling")
plt.ylabel("Apego emocional")
plt.title("Storytelling vs Apego emocional")
plt.show()

df.corr(numeric_only=True)
corr_table = df.corr(numeric_only=True)
print(corr_table)

