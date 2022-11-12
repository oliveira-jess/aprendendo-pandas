import pandas as pd

df = pd.read_csv("C:/Users/jessi/Desktop/Curso DIO/Pandas/datasets/Gapminder.csv", sep=";")

#Visualizando as 5 primeiras linhas
#print(df.head())

#Renomear as colunas
df = df.rename(columns={"country":"Pais","continent":"Continente","year":"Ano","lifeExp":"Exp. Vida","pop":"Pop Total","gdpPercap":"PIB"})

#Pegar as 5 primeiras linhas do dataframe
#print(df.head())

#Total de linhas e colunas
#print(df.shape)

#Nomes das colunas
#print(df.columns)

#Tipos de cada coluna
#print(df.dtypes)

#Pegar as 5 últimas linhas do dataframe
#print(df.tail())

#Informações estatísticas do dataframe
#print(df.describe())

#Retornar valores únicos de uma coluna
#print(df["Continente"].unique())

#Pegar somente as linhas de um determinado dado
#oceania = df.loc[df["Continente"] == "Oceania"]
#print(oceania.head())

#Agrupar dados por algum parâmetro
#print(df.groupby("Continente")["Pais"].nunique())

#Media de um grupo de dados
#print(df.groupby("Ano")["Exp. Vida"].mean())