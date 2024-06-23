library(dplyr)

Dados <-read.csv('dados/original.csv', sep=';', encoding = 'UTF-8')

View(Dados) 

municipios_sexo <- Dados %>%
  group_by(MUN_LPI, SEXO) %>%
  summarise(frequencia = n()) %>%
  ungroup()

View(municipios_sexo)

#variância desigual -> variação de Welch
#Hipótese nula -> A diferença da média de casos de mulheres e homens nas cidades do Brasil é = 0
#Hipótese alternativa -> A diferença da média de casos de mulheres e homens nas cidades do Brasil é != 0
t.test(municipios_sexo$frequencia~municipios$SEXO)    
