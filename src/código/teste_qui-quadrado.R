# teste qui-quadrado com sexo e ocorrência de óbito ou não 

install.packages("haven")
install.packages("psych")
install.packages("janitor")
install.packages("effectsize")
install.packages("ggplot2")
library(ggplot2)
library(haven)
library(psych)
library(janitor)
library(effectsize) 
library(dplyr)
Dados <-read.csv('dados/original.csv', sep=';', encoding = 'UTF-8')
df_filtrado <- Dados %>%
  filter(OBITO != "IGN")
View(df_filtrado)


#dados <- as.factor(df_filtrado) 

#freq <- tabyl(dat = dados, var1 = SEXO, var2 = OBITO)

freq <- df_filtrado %>%
  tabyl(SEXO, OBITO)

View(freq)

qui.q <- chisq.test(freq)
qui.q

qui.q$expected
# expected -> Esta tabela mostra as frequências esperadas para cada combinação
#de sexo e ocorrência de óbito, com base nos dados observados.
qui.q$residuals
# residuals -> Os resíduos são as diferenças entre as frequências observadas e 
#as frequências esperadas. Valores positivos indicam uma frequência observada
#maior que a esperada, enquanto valores negativos indicam uma frequência 
#observada menor que a esperada.
qui.q$stdres
# stdres ->  Os resíduos padronizados são os resíduos divididos pelo desvio
#padrão. Eles ajudam a identificar células com contribuições desproporcionais 
#para o qui-quadrado.