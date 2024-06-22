library(dplyr)

Dados <-read.csv('dados/original.csv', sep=';', encoding = 'UTF-8')

View(Dados) 

municipios <- Dados %>%
  group_by(MUN_LPI, SEXO) %>%
  summarise(frequencia = n()) %>%
  ungroup()

View(municipios)

#variância desigual
t.test(municipios$frequencia~municipios$SEXO)    

#variância igual
t.test(municipios$frequencia~municipios$SEXO, var.equal=T) 