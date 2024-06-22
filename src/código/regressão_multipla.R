library(lmtest)

dados <- read.csv('dados/dados_regressão_linear_multiplas.csv', sep=',')

View(dados)

par(mfrow=c(1,6))
boxplot(dados$IndiceGini, col=2, main="IndiceGini")
boxplot(dados$GDPperCapita, col=2, main="GDPperCapita")
boxplot(dados$UnemploymentRate, col=2, main="UnemploymentRate")
boxplot(dados$Inflation, col=2, main="Inflation")
boxplot(dados$AcessoEletricidade, col=2, main="AcessoEletricidade")
boxplot(dados$ExpectativaVida, col=2, main="ExpectativaVida")

par(mfrow=c(1,6))
hist(dados$IndiceGini, col=2,  nclass=10, main="IndiceGini")
hist(dados$GDPperCapita, col=2,  nclass=10, main="GDPperCapita")
hist(dados$UnemploymentRate, col=2,  nclass=10, main="UnemploymentRate")
hist(dados$Inflation, col=2,  nclass=10, main="Inflation")
hist(dados$AcessoEletricidade, col=2,  nclass=10, main="AcessoEletricidade")
hist(dados$ExpectativaVida, col=2,  nclass=10, main="ExpectativaVida")

#Modelo regressão linear múltipla
modelo_regressao<-lm(dados$Pobreza~dados$PopulacaoUrbana+dados$IndiceGini+dados$UnemploymentRate+dados$Inflation)
modelo_regressao #Coeficientes regressão

#Plot da adequação do modelo ao dados reais
par(mfrow=c(2,1))
plot(modelo_regressao) 

#Comparação da predição do modelo com os dados reais
par(mfrow=c(1,4))
cor(predict(modelo_regressao),dados$Pobreza) #Correlação com os dados reais

#ANOVA
anova(modelo_regressao)
summary(modelo_regressao)

#Analise dos Residuos
plot(modelo_regressao$residuals)
hist(modelo_regressao$residuals)

#Teste Shapiro
shapiro.test(modelo_regressao$residuals)

#Teste da independencia dos residuos (Box–Pierce)
Box.test(modelo_regressao$residuals)#

#Teste de homogeneidade dos residuos (Breusch-Pagan)
bptest(reglin2, varformula = NULL, studentize = FALSE, data = list(dados1))

#Correlação de cada variável independente com a variável dependente

cor(dados$Pobreza, dados$PopulacaoUrbana)
cor.test(dados$Pobreza, dados$PopulacaoUrbana)

cor(dados$Pobreza, dados$IndiceGini)
cor.test(dados$Pobreza, dados$IndiceGini)

cor(dados$Pobreza, dados$UnemploymentRate)
cor.test(dados$Pobreza, dados$UnemploymentRate)

cor(dados$Pobreza, dados$Inflation)
cor.test(dados$Pobreza, dados$Inflation)

#hipótese principal: verdadeira correlação é igual ao intervalo
#Aceita-se a hipotese
#hipótese alternativa: verdadeira correlação não é igual ao intervalo 
#confiança
#Aceita-se a hipotese alternativa
#se a probabilidade obtida com o t calculado for superior 
#ao "ponto de corte" do p-valor (5%).