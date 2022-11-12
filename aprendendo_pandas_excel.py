import pandas as pd
import matplotlib.pylab as plt

df_aracaju = pd.read_excel("C:/Users/jessi/Desktop/Curso DIO/Pandas/datasets/Aracaju.xlsx")
df_fortaleza = pd.read_excel("C:/Users/jessi/Desktop/Curso DIO/Pandas/datasets/Fortaleza.xlsx")
df_natal = pd.read_excel("C:/Users/jessi/Desktop/Curso DIO/Pandas/datasets/Natal.xlsx")
df_recife = pd.read_excel("C:/Users/jessi/Desktop/Curso DIO/Pandas/datasets/Recife.xlsx")
df_salvador = pd.read_excel("C:/Users/jessi/Desktop/Curso DIO/Pandas/datasets/Salvador.xlsx")

#Juntando todos os arquivos
df = pd.concat([df_aracaju,df_fortaleza,df_natal,df_recife,df_salvador])

#Pegando amostra do conjunto de dados
#print(df.sample(5))

#Alterando o tipo da coluna
df["LojaID"] = df["LojaID"].astype("object")
#print(df.dtypes)

### TRATANDO VALORES FALTANTES ###

# Consultando linhas com valores faltantes
#print(df.isnull().sum())

#Substituindo os valores nulos pela média
#df["Vendas"].fillna(df["Vendas"].mean(),inplace=True)
#print(df.isnull().sum())

#Substituindo os valores nulos por 0 (zero)
#df["Vendas"].fillna(0,inplace=True)
#print(df.isnull().sum())

#Apagando as linhas com valores nulos
#df.dropna(inplace=True)

#Apagando as linhas com valores nulos em apenas 1 coluna
#df.dropna(subset=["Vendas"],inplace=True)
#print(df.isnull().sum())

#Apagando as linhas com valores faltantes em todas as colunas
#df.dropna(how="all", inplace=True)
#print(df.isnull().sum())

### CRIANDO NOVAS COLUNAS ###

#Criando uma nova coluna
df["Receita"] = df["Vendas"] * (df["Qtde"])
#print(df.head())

#Retornando a maior receita
#print(df["Receita"].max())

#Retornando a menor receita
#print(df["Receita"].min())

#Maiores valores de uma determinada coluna
#print(df.nlargest(3,"Receita"))

#Menores valores de uma determinada coluna
#print(df.nsmallest(3,"Receita"))

#Agrupamento por cidade
#print(df.groupby("Cidade")["Receita"].max()) #maior venda
#print(df.groupby("Cidade")["Receita"].sum()) #soma de todas as vendas

#Ordenando o conjunto de dados
#print(df.sort_values("Receita",ascending=False))

### TRABALHANDO COM DATAS ###

#Transformando coluna de datas em tipo Data
#df["Data"] = pd.to_datetime(df["Data"])
#print(df.dtypes)

#Agrupamento por ano
#print(df.groupby(df["Data"].dt.year)["Receita"].sum())

#Criar uma coluna de ano
#df["ano_venda"] = df["Data"].dt.year
#print(df.head())

#Extraindo mês e dia
#df["mes_venda"],df["dia_venda"] = df["Data"].dt.month,df["Data"].dt.day
#print(df.sample(5))

#Extrair a data mais antiga
#print(df["Data"].min())

#Calculando a diferença de dias
#df["diferenca_dias"] = df["Data"] - df["Data"].min()
#print(df.sample(5))

#Criando coluna de trimestre
#df["trimestre"] = df["Data"].dt.quarter
#print(df.sample(5))

#Filtrar de um determinado mês
#vendas_marco_2019 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
#print(vendas_marco_2019)

### VISUALIZAÇÃO DE DADOS ###

#Grafico de barras verticais
#df["LojaID"].value_counts().plot(kind='bar')
#plt.show()

#Grafico de barras horizontais
#df["LojaID"].value_counts(ascending=True).plot(kind='barh') #grafico do maior para o menor
#plt.show()

#Grafico de pizza
#df.groupby(df["Data"].dt.year)["Receita"].sum().plot(kind='pie')
#plt.show()
#df["Data"].dt.year.value_counts().plot(kind='pie')
#plt.show()

#Configurando o gráfico
#plt.style.use('ggplot')
#df["Cidade"].value_counts().plot(kind='line', color='red',marker="*") #color = cor das barras
#plt.title("Total de vendas por cidade") #adicionando título
#plt.xlabel("Cidade") #nomeando o eixo X
#plt.ylabel("Total de vendas") #nomeando o eixo Y
#plt.legend() #adicionando legenda
#plt.show()

#Gerando um histograma
#df["Qtde"].plot(kind='hist')
#plt.show()

#Gerando um gráfico de dispersão
#df_venda2019 = df.loc[df["Data"].dt.year == 2019]
#plt.scatter(x=df_venda2019["Data"].dt.day, y=df_venda2019["Receita"])
#plt.savefig("figura.png") #salvando a figura
#plt.show()