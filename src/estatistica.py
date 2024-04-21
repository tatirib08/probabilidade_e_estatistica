import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, spearmanr, kendalltau
import csv 
import statsmodels.formula.api as smf 
import seaborn as sns

dados = pd.read_csv("src/dados/fa_casoshumanos_1994-2023_editado.csv")
dados_correlacao = pd.read_csv("src/dados/fa_casoshumanos_1994-2023_correlacao.csv")
dados_obitos_por_idade = pd.read_excel("src/dados/FrequenciaIdade.xlsx")
#histograma casos por região
histograma_casos_por_regiao = plt.figure("histograma_casos_por_regiao")
casos_por_regiao = dados.groupby(by="MACRORREG_LPI")["MACRORREG_LPI"]
casos_por_regiao.hist(bins=2)
#poligono de frequencia casos por região
casos_por_regiao.value_counts().plot()

# IDADE
histograma_casos_por_idade = plt.figure("histograma_casos_por_idade")
casos_por_idade = dados_correlacao.groupby(by="IDADE")["IDADE"]
casos_por_idade.hist(bins=1)
#obitos é outro dataframe 
obitos = dados_correlacao.loc[dados_correlacao['OBITO'] == "SIM"]
# print(obitos.to_string())

histograma_casos_por_ano = plt.figure("histograma_casos_por_ano")
casos_por_ano = dados.groupby(by="ANO_IS")["ANO_IS"]
casos_por_ano.hist(bins=2)
#poligono de frequencia casos por ano
casos_por_ano.value_counts().plot()

plt.figure("quartis").show()

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

'''
    CORRELAÇÃO LINEAR
'''
# ######## correlação ########:
# diagrama de dispersão (scatter plot):
dispersaoObitosIdade = plt.figure("diagrama_dispersão_idade_óbitos")
plt.scatter(dados_obitos_por_idade['IDADE'], dados_obitos_por_idade['OBITOS'], color='r')
plt.xlabel("Idade")
plt.ylabel("Óbitos")

dispersaoCasosPorAno = plt.figure("dispersão_casos_por_ano")
dfCasosPorAno = dados.groupby(["ANO_IS"]).size().reset_index(name="COUNT")
plt.scatter(dfCasosPorAno['ANO_IS'], dfCasosPorAno['COUNT'], color='r')
plt.xlabel("Ano")
plt.ylabel("Casos")

# coeficiente de pearson 
''' 
    Coeficiente de Pearson(r): mede o grau da correlação linear entre duas variáveis quantitativas
    r = +1 -> correlação positiva perfeita
    r = 0 -> não há correlação ou a correlação não é linear
    r =-1 -> correlação negativa perfeita 
'''
coef_pearson, p_valor = pearsonr(dados_obitos_por_idade['IDADE'], dados_obitos_por_idade['OBITOS'])
# coeficiente de correlação de spearman
''' 
    Coeficiente de Spearman(rho): medida não paramétrica da dependência dos postos das variáveis. 
    O valor varia de -1 a +1, sendo que quanto mais próximo dos extremos, maior é a correlação. 
'''
coef_spearman, p_valor = spearmanr(dados_obitos_por_idade['IDADE'], dados_obitos_por_idade['OBITOS'])

''' 
    Coeficiente de correlação de Kendall
'''

print(dados_obitos_por_idade["IDADE"].corr(dados_obitos_por_idade["OBITOS"]))

print(f"COEFICIENTE DE PEARSON:  {coef_pearson}")
# coef de pearson output = -0.00675470470148104
print(f"COEFICIENTE DE SPEARMAN:  {coef_spearman}")
# coef de spearman output = 0.015121537240898921

# ######## Análise de Regressão 
'''
    Descrever por meio de um modelo matemático a relação entre duas variáveis, a partir de
    n observações das mesmas.
    Regressão linear simples: um pra um. -> função do primeiro grau: ML
    Regressão linear múltipla: um pra muitos
'''
regression = smf.ols('OBITOS ~ IDADE', data=dados_obitos_por_idade)
regression.fit().summary()
plt.figure("regressão_óbitos_por_idade")
sns.regplot(x='IDADE', y='OBITOS', data=dados_obitos_por_idade)

regression2 = smf.ols('COUNT ~ ANO_IS', data=dfCasosPorAno)
regression2.fit().summary()
plt.figure("regressão_casos_por_ano")
sns.regplot(x='ANO_IS', y='COUNT', data=dfCasosPorAno)

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