import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr
import statsmodels.formula.api as smf 
import seaborn as sns

dados = pd.read_csv("src/dados/fa_casoshumanos_1994-2023_editado.csv")
dados_obitos_por_idade = pd.read_excel("src/dados/FrequenciaIdade.xlsx")

'''
    HISTOGRAMA CASOS POR REGIÃO
'''
histograma_casos_por_regiao = plt.figure("histograma_casos_por_regiao")
''''''
casos_por_regiao = dados.groupby(by="MACRORREG_LPI")["MACRORREG_LPI"]
casos_por_regiao.hist(bins=2)

''' poligono de frequencia ''' 
casos_por_regiao.value_counts().plot()

''' print '''
print(f'\n\nCASOS POR REGIÃO: \n{casos_por_regiao.value_counts()}\n\n')
''''''


'''
    HISTOGRAMA CASOS POR IDADE
'''
histograma_casos_por_idade = plt.figure("histograma_casos_por_idade")
''''''
casos_por_idade = dados.groupby(by="IDADE")["IDADE"]
casos_por_idade.hist(bins=1)
''''''

'''
    HISTOGRAMA CASOS POR ANO
'''
histograma_casos_por_ano = plt.figure("histograma_casos_por_ano")
agrupado_por_ano = dados.groupby(by="ANO_IS")
agrupado_por_ano["ANO_IS"].hist(bins=2)
''' poligono de frequencia ''' 
agrupado_por_ano["ANO_IS"].value_counts().plot()
''''''


'''
    ANÁLISE CASOS POR ANO
'''
df_casos_por_ano = agrupado_por_ano.size().reset_index(name="CASOS")
coluna_casos = df_casos_por_ano['CASOS']
''' média '''
media_casos_por_ano = coluna_casos.mean()
''' moda '''
moda_casos_por_ano = coluna_casos.mode()
''' mediana '''
mediana_casos_por_ano = coluna_casos.median()
''' curtose '''
curtose_casos_por_ano = coluna_casos.kurtosis()
''' variância '''
variancia_casos_por_ano = coluna_casos.var()
''' desvio padrão '''
desvio_padrao_casos_por_ano = coluna_casos.std()
''' quartis '''
quartis_casos_por_ano = coluna_casos.quantile([0.25, 0.75])
''' maior valor '''
linha_maior_valor_casos_por_ano = df_casos_por_ano.iloc[coluna_casos.idxmax()]
maior_valor_casos_por_ano = linha_maior_valor_casos_por_ano['CASOS']
ano_maior_valor_casos_por_ano = linha_maior_valor_casos_por_ano['ANO_IS']
''' menor valor '''
linha_menor_valor_casos_por_ano = df_casos_por_ano.iloc[coluna_casos.idxmin()]
menor_valor_casos_por_ano = linha_menor_valor_casos_por_ano['CASOS']
ano_menor_valor_casos_por_ano = linha_menor_valor_casos_por_ano['ANO_IS']
'''print'''
print(f'\n\nANÁLISE CASOS POR ANO:')
print(f'- Média -> {media_casos_por_ano}')
print(f'- Moda -> {moda_casos_por_ano.to_list()}')
print(f'- Mediana (Percentil 50) -> {mediana_casos_por_ano}')
print(f'- Curtose -> {curtose_casos_por_ano}')
print(f'- Variância -> {variancia_casos_por_ano}')
print(f'- Desvio Padrão -> {desvio_padrao_casos_por_ano}')
print(f'- Primeiro Quartil (Percentil 25) -> {quartis_casos_por_ano[0.25]}')
print(f'- Terceiro Quartil (Percentil 75) -> {quartis_casos_por_ano[0.75]}')
print(f'- Maior Quantidade de Casos -> {maior_valor_casos_por_ano}, ano {ano_maior_valor_casos_por_ano}')
print(f'- Menor Quantidade de Casos -> {menor_valor_casos_por_ano}, ano {ano_menor_valor_casos_por_ano}')
print("\n")

''' box plot '''
box_plot_df = df_casos_por_ano
iqr = box_plot_df['CASOS'].quantile(0.75) - box_plot_df['CASOS'].quantile(0.25)
box_plot_casos_por_ano = plt.figure("boxplot_casos_por_ano")
box_plot_casos_por_ano.gca().set_ylim([0, box_plot_df['CASOS'].quantile(0.75) + 1.5 * iqr])
_, bp = box_plot_df.boxplot(column =['CASOS'], grid = False, return_type='both')
''''''


# outliers = [flier.get_ydata() for flier in bp["fliers"]]
# boxes = [box.get_ydata() for box in bp["boxes"]]
# medians = [median.get_ydata() for median in bp["medians"]]
# whiskers = [whiskers.get_ydata() for whiskers in bp["whiskers"]]

# print(f"outlier -> {outliers}")
# print(f"box -> {boxes}")
# print(f"median -> {medians}")
# print(f"whisker -> {whiskers}")

# print(f'stats -> {box_plot_df["COUNT"].describe()}')

# quartis_casos_por_ano = casos_por_ano.count().quantile([.25, .5, .75]) 

# quartis_casos_por_ano.plot.bar(color=['#2876EB', '#5728EB', '#2838EB'])

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