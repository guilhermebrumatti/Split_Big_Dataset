import pandas as pd

#Lendo tabela .csv
df = pd.read_csv('world_population.csv')

#Usando a propriedado Dataframe.iloc[], dividimos a base aberta.
#Nesta linha, definimos que a variavel df1 receberá o Dataframe da linha 0 até a linha 100
df1 = df.iloc[0:100]
#Neste linha, definimos que a variavel df2 receberá o Dataframe da linha 101 até a última linha
df2 = df.iloc[100:]

#Podemos ver que a divisão foi feita printando o len() de cada variavel
print(len(df))
print(len(df1))
print(len(df2))

#exportando os dataframes divididos em duas partes
df1.to_csv("world_population_pt1.csv", encoding="UTF-8")
df2.to_csv("world_population_pt2.csv", encoding="UTF-8")

