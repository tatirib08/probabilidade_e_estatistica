library(lmtest)

dados <- read.csv('dados/dados_regressão_linear_multiplas.csv', sep=',')

View(dados)

par(mfrow=c(1,6))
boxplot(dados$Pobreza, col=2, main="Pobreza")
boxplot(dados$PopulacaoUrbana, col=2, main="PopulacaoUrbana")
boxplot(dados$IndiceGini, col=2, main="IndiceGini")
boxplot(dados$TaxaDesemprego, col=2, main="TaxaDesemprego")
boxplot(dados$Inflacao, col=2, main="Inflacao")

par(mfrow=c(1,6))
hist(dados$Pobreza, col=2,  nclass=10, main="Pobreza")
hist(dados$PopulacaoUrbana, col=2,  nclass=10, main="PopulacaoUrbana")
hist(dados$IndiceGini, col=2,  nclass=10, main="IndiceGini")
hist(dados$TaxaDesemprego, col=2,  nclass=10, main="TaxaDesemprego")
hist(dados$Inflacao, col=2,  nclass=10, main="Inflacao")

#Modelo regressão linear múltipla
modelo_regressao<-lm(dados$Pobreza~dados$PopulacaoUrbana+dados$IndiceGini+dados$TaxaDesemprego+dados$Inflacao)
modelo_regressao #Coeficientes regressão

#Plot da adequação do modelo ao dados reais
par(mfrow=c(1,2))
plot(modelo_regressao) 

#Comparação da predição do modelo com os dados reais
par(mfrow=c(1,4))
cor(predict(modelo_regressao),dados$Pobreza) #Correlação com os dados reais

#ANOVA
anova(modelo_regressao)
summary(modelo_regressao)

#Análise gráfica dos resíduos
plot(modelo_regressao$residuals)
hist(modelo_regressao$residuals)

#Teste da normalidade dos resíduos (Shapiro)
shapiro.test(modelo_regressao$residuals)

#Teste da autocorrelação/independencia dos resíduos (Box–Pierce)
Box.test(modelo_regressao$residuals)#

#Teste de autocorrelação/independencia dos resíduos (Durbin-Watson)
dwtest(modelo_regressao)

#Teste de homogeneidade dos resíduos (Breusch-Pagan)
bptest(modelo_regressao, varformula = NULL, studentize = FALSE, data = list(dados1))

#Correlação de cada variável independente com a variável dependente
cor(dados$Pobreza, dados$PopulacaoUrbana)
cor.test(dados$Pobreza, dados$PopulacaoUrbana)

cor(dados$Pobreza, dados$IndiceGini)
cor.test(dados$Pobreza, dados$IndiceGini)

cor(dados$Pobreza, dados$TaxaDesemprego)
cor.test(dados$Pobreza, dados$TaxaDesemprego)

cor(dados$Pobreza, dados$Inflacao)
cor.test(dados$Pobreza, dados$Inflacao)
