import pandas as pd
import matplotlib.pyplot as plt

#lendo o arquivo
df = pd.read_excel("C:/Users/jessi/Desktop/Curso DIO/Pandas/datasets/AdventureWorks.xlsx")

df["custo"] = df["Custo Unitário"] * df["Quantidade"]
df["lucro"] = df["Valor Venda"] - df["custo"]
df["tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days


#print("Custo total = ",df["custo"].sum())
#print("Lucro total = ", df["lucro"].sum())
#print(df.groupby("Marca")["tempo_envio"].mean()) #Media de tempo de envio
pd.options.display.float_format = '{:20,.2f}'.format
#print(df.groupby([df["Data Venda"].dt.year,"Marca"])["lucro"].sum()) #lucro por ano e marca
#lucro_ano = df.groupby([df["Data Venda"].dt.year,"Marca"])["lucro"].sum().reset_index()
#print(lucro_ano)
#print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)) #grafico produto x quantidade
#df.groupby("Produto")["Quantidade"].sum().plot(kind="barh")
#plt.show()

#df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot(kind='bar') #grafico lucro x ano
#plt.show()

#Grafico de bloxplot
plt.boxplot(df["tempo_envio"])
plt.show()