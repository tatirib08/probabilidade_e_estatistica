library(dplyr)

Dados <-read.csv('dados/original.csv', sep=';', encoding = 'UTF-8')

View(Dados) 

municipios <- Dados %>%
  group_by(MUN_LPI, UF_LPI) %>%
  summarise(frequencia = n()) %>%
  ungroup() %>%
  mutate(pertence_sp = if_else(UF_LPI == "SP", "Cidade de São Paulo", "Cidade fora de São Paulo"))

View(municipios)

#variância desigual
#Hipótese nula -> A diferença da média de casos das cidades do estado de São Paulo comparado às cidades fora do estado de São Paulo são = 0
#Hipótese alternativa -> A diferença da média de casos das cidades do estado de São Paulo comparado às cidades fora do estado de São Paulo são > 0
t.test(municipios$frequencia~municipios$pertence_sp, alternative = "greater")    
