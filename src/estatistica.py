import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv("src/dados/fa_casoshumanos_1994-2023_editado.csv")

#histograma casos por região
histograma_casos_por_regiao = plt.figure("histograma_casos_por_regiao")
casos_por_regiao = dados.groupby(by="MACRORREG_LPI")["MACRORREG_LPI"]
casos_por_regiao.hist(bins=2)
#poligono de frequencia casos por região
casos_por_regiao.value_counts().plot()

#histograma casos por ano
histograma_casos_por_ano = plt.figure("histograma_casos_por_ano")
casos_por_ano = dados.groupby(by="ANO_IS")["ANO_IS"]
casos_por_ano.hist(bins=2)
#poligono de frequencia casos por ano
casos_por_ano.value_counts().plot()

plt.figure("quartis").show()


# plt.show()

media_casos_por_ano = casos_por_ano.count().mean()
moda_casos_por_ano = casos_por_ano.count().mode()
mediana_casos_por_ano = casos_por_ano.count().median()
curtose_casos_por_ano = casos_por_ano.count().kurtosis()
variancia_casos_por_ano = casos_por_ano.count().var()
desvio_padrao_casos_por_ano = casos_por_ano.count().std()

print(f'Média -> {media_casos_por_ano}')
print(f'Moda -> {moda_casos_por_ano.to_list()}')
print(f'Mediana -> {mediana_casos_por_ano}')
print(f'Curtose -> {curtose_casos_por_ano}')
print(f'Variância -> {variancia_casos_por_ano}')
print(f'Desvio Padrão -> {desvio_padrao_casos_por_ano}')

quartis_casos_por_ano = casos_por_ano.count().quantile([.25, .5, .75]) 

quartis_casos_por_ano.plot.bar(color=['#2876EB', '#5728EB', '#2838EB'])

# ######## correlação:
# diagrama de dispersão (scatter plot):
dispersaoIdadeEstado = plt.figure("diagrama_dispersão_idade_estado")
# plt.plot(dados['UF_LPI'], dados['IDADE'], color='k') ta dando erro
plt.scatter(dados['UF_LPI'], dados['IDADE'], color='r')
plt.xlabel("Unidade Federativa")
plt.ylabel("Idade do infectado")
# plt.xticks([a-b]) -> definir intervalo

# diagrama de dispersão ano-estado
dispersaoAnoEstado = plt.figure("diagrama_dispersão_ano_estado")
# plt.plot(dados['UF_LPI'],dados['ANO_IS'], color='k')ta dando erro
plt.scatter(dados['UF_LPI'],dados['ANO_IS'], color='g')
plt.xlabel("Unidade Federativa")
plt.ylabel("Ano da incidência")

plt.show()

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