import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv("dados/fa_casoshumanos_1994-2023_editado.csv")

#histograma casos por região
histograma_casos_por_regiao = plt.figure("histograma_casos_por_regiao")
casos_por_regiao = dados.groupby(by="MACRORREG_LPI")["MACRORREG_LPI"]
casos_por_regiao.hist()
#poligono de frequencia casos por região
casos_por_regiao.value_counts().plot()

#histograma casos por ano
histograma_casos_por_ano = plt.figure("histograma_casos_por_ano")
casos_por_ano = dados.groupby(by="ANO_IS")["ANO_IS"]
casos_por_ano.hist()
#poligono de frequencia casos por ano
casos_por_ano.value_counts().plot()

plt.show()

media_casos_por_ano = casos_por_ano.count().mean()
moda_casos_por_ano = casos_por_ano.count().mode()
mediana_casos_por_ano = casos_por_ano.count().median()

print(f'Média -> {media_casos_por_ano}')
print(f'Moda -> {moda_casos_por_ano.to_list()}')
print(f'Mediana -> {mediana_casos_por_ano}')


'''
Histograma; poligono de frequencia; poligono de frequencia acumulada; 
Curva de frequencia -> curva polida; analisar a forma da curva; 
Media aritmetica -> dados não agrupados; desvio em relação a media; dados agrupados (sem intervalos de classe, com intervalos de classe)
Moda ->  dados não agrupados; dados agrupados (sem intervalos de classe, com intervalos de classe); expressões gráficas da moda; 
Mediana -> dados não agrupados; dados agrupados (sem intervalos de classe, com intervalos de classe)
posição relativa da media, mediana e moda;
Quartis;
Percentis;
Dispersão ou variabilidade; 
Amplitude total;
Variancia e desvio padrão
'''