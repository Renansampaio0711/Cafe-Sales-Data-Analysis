#média de apego emocional
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/scleber/OneDrive/Desktop/Projeto Análise de Dados/Movie and Emotional Attachment Survey.csv")
df["Audience Attachment Score"].mean()
