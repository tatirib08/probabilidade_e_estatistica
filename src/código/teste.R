library(dplyr)

Dados <-read.csv('dados/original.csv', sep=';', encoding = 'UTF-8')

#inserir dados#visualizar os dados
attach(Dados)
names (Dados)
View(Dados) 
#ler coluna da tabela
#municipios <- table(Dados$MUN_LPI)

municipios <- Dados %>%
  group_by(MUN_LPI, UF_LPI) %>%
  summarise(frequencia = n()) %>%
  ungroup()

View(municipios)


#Tabela de Referência Cruzada

table(Dados$Genero, Dados$Escola)
table(Dados$Genero, Dados$Nota_Biol)

#Frequências Relativas
prop.table(table(Dados$Genero))
prop.table(table(Dados$Escola)
           
           
 #Teste de hipotese - Nota de Física x Escola
 # Tapply
 tapply(Nota_Fis, Escola, mean)
 # teste T variancias desiguais
 t.test(Nota_Fis~Escola)    
 # teste T variancias iguais
 t.test(Nota_Fis~Escola, var.equal=T) 
 
 
 #Bonus
 #Teste de hipotese - Nota de Física x Genero
 # Tapply
 tapply(Nota_Fis, Genero, mean)
 # teste T variancias desiguais
 t.test(Nota_Fis~Genero)    
 # teste T variancias iguais
 t.test(Nota_Fis~Genero, var.equal=T)