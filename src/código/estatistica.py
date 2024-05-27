'''
    Alan Vitor de Almeida Nascimento
    Luiza de Sá Florentino Limoeiro
    Tatiana Ribeiro Oliveira
'''

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr
import statsmodels.formula.api as smf 
import seaborn as sns

dados = pd.read_csv("dados/colunas_filtradas.csv")
dados_obitos_por_idade = pd.read_excel("dados/frequencia_obitos_por_idade.xlsx")

'''
    HISTOGRAMA CASOS POR REGIÃO
'''
histograma_casos_por_regiao = plt.figure("histograma_casos_por_regiao")
plt.title("Casos agrupados por região")
plt.xlabel("Região")
plt.ylabel("Casos")
''''''
casos_por_regiao = dados.groupby(by="MACRORREG_LPI")["MACRORREG_LPI"]
casos_por_regiao.hist(bins=2)

''' poligono de frequencia ''' 
casos_por_regiao.value_counts().plot()


''' print '''
print(f'\n\nCASOS POR REGIÃO: \n{casos_por_regiao.value_counts()}\n\n')
''''''

plt.show()

'''
    HISTOGRAMA CASOS POR IDADE
'''
histograma_casos_por_idade = plt.figure("histograma_casos_por_idade")
plt.title("Casos agrupados por idade")
plt.xlabel("Idade")
plt.ylabel("Casos")
''''''
casos_por_idade = dados.groupby(by="IDADE")["IDADE"]
casos_por_idade.hist(bins=1)
''''''

plt.show()

'''
    ANÁLISE CASOS POR ANO
'''
agrupado_por_ano = dados.groupby(by="ANO_IS")

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
''' amplitude '''
amplitude_casos_por_ano = maior_valor_casos_por_ano - menor_valor_casos_por_ano
''' amplitude interquartil '''
amplitude_interquartil_casos_por_ano = quartis_casos_por_ano[0.75] - quartis_casos_por_ano[0.25]
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
print(f'- Amplitude de Casos -> {amplitude_casos_por_ano}')
print(f'- Amplitude Interquartil de Casos -> {amplitude_interquartil_casos_por_ano}')

print("\n")


'''
    HISTOGRAMA CASOS POR ANO
'''
histograma_casos_por_ano = plt.figure("histograma_casos_por_ano_completo")
plt.title("Casos agrupados por ano")
plt.xlabel("Ano")
plt.ylabel("Casos")
agrupado_por_ano["ANO_IS"].hist(bins=1)

histograma_casos_por_ano = plt.figure("histograma_casos_por_ano_y_limitado")
histograma_casos_por_ano.gca().set_ylim([0, quartis_casos_por_ano[0.75] + 1.5 * amplitude_interquartil_casos_por_ano])
plt.title("Casos agrupados por ano com eixo Y limitado")
plt.xlabel("Ano")
plt.ylabel("Casos")
agrupado_por_ano["ANO_IS"].hist(bins=1)
''''''

plt.show()

'''
    BOX PLOT CASOS POR ANO 
'''
''' completo, com eixo y original'''
box_plot_casos_por_ano = plt.figure("boxplot_casos_por_ano_completo")
plt.title("Casos agrupados por ano")
plt.ylabel("Casos")
_, bp = df_casos_por_ano.boxplot(column =['CASOS'], whis=1.5, grid = False, return_type='both')
''' eixo y limitado a somente o box plot'''
box_plot_casos_por_ano_limitado = plt.figure("boxplot_casos_por_ano_limitado_eixo_y")
plt.title("Casos agrupados por ano com eixo Y limitado")
plt.ylabel("Casos")
box_plot_casos_por_ano_limitado.gca().set_ylim([0, quartis_casos_por_ano[0.75] + 1.5 * amplitude_interquartil_casos_por_ano])
_, bp = df_casos_por_ano.boxplot(column =['CASOS'], whis=1.5, grid = False, return_type='both')
'''print'''
print(f'\n\n DADOS BOX PLOT CASOS POR ANO:')
outliers = [flier.get_ydata() for flier in bp["fliers"]]
print(f'- Valores discrepantes (outliers) -> {outliers[0]}')
limites = [whiskers.get_ydata() for whiskers in bp["whiskers"]]
limite_superior = limites[1][1]
print(f'- Limite superior -> {limite_superior}')

print("\n")
''''''
plt.show()

'''
    CORRELAÇÃO LINEAR
'''
# ######## correlação ########:
# diagrama de dispersão (scatter plot):
dispersaoObitosIdade = plt.figure("diagrama_dispersão_idade_óbitos")
plt.scatter(dados_obitos_por_idade['IDADE'], dados_obitos_por_idade['OBITOS'], color='r')
plt.title("Óbitos agrupados por idade")
plt.xlabel("Idade")
plt.ylabel("Óbitos")

dispersaoCasosPorAno = plt.figure("dispersão_casos_por_ano")
dfCasosPorAno = dados.groupby(["ANO_IS"]).size().reset_index(name="COUNT")
plt.scatter(dfCasosPorAno['ANO_IS'], dfCasosPorAno['COUNT'], color='r')
plt.title("Casos agrupados por ano")
plt.xlabel("Ano")
plt.ylabel("Casos")

plt.show()

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
print(regression.fit().summary())
plt.figure("regressão_óbitos_por_idade")
sns.regplot(x='IDADE', y='OBITOS', data=dados_obitos_por_idade)

regression2 = smf.ols('COUNT ~ ANO_IS', data=dfCasosPorAno)
print(regression2.fit().summary())
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
