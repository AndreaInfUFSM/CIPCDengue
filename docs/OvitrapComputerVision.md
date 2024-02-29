<!--
author:   Andrea Charão

email:    andrea@inf.ufsm.br

version:  0.0.1

language: PT-BR

narrator: Brazilian Portuguese Female

comment:  Review sobre Visão Computacional aplicada a contagem de ovos de mosquitos

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/AndreaInfUFSM/CIPCDengue/master/docs/OvitrapComputerVision.md)

<!--
nvm use v10.23.0
liascript-devserver --input README.md --port 3001 --live
-->


# Contagem de ovos de mosquitos em ovitraps


> Revisão rápida de algumas referências sobre o assunto

Profa. Andrea Schwertner Charão

Depto. de Linguagens e Sistemas de Computação, Centro de Tecnologia, UFSM

## Seleção de publicações nacionais

Strings de busca:  

- visao computacional contagem ovos mosquito
- contagem ovos mosquito dengue


### [Brun et al. 2020]


[article] Brun, A.L., Moraes, P.L., Rizzi, C.B. e Rizzi, R.L. 2020. Uma revisão das técnicas computacionais para contagem de ovos de Aedes aegypti em imagens de ovitrampas. Revista Brasileira de Computação Aplicada. 12, 3 (jul. 2020), 1-15. DOI: https://doi.org/10.5335/rbca.v12i3.10947


- Revisão de 21 artigos que descrevem técnicas de processamento de imagens ou de aprendizagem de máquina aplicadas à contagem de ovos 
- Tabelas resumem as técnicas empregadas, a acurácia e a quantidade de imagens usadas para validação
- A maioria dos resultados tem baixas taxas de erro, embora muito sensíveis às imagens usadas para validação
- Autores sugerem o compartilhamento de imagens em repositórios que permitam avançar as pesquisas sobre métodos que se adaptem melhor a uma variedade de imagens





### [Silva et al. 2021]

[article] SILVA, Lucas M. de Sousa; SILVA, Lucas L.; BARROS, Veruska; ARAUJO, Flavio H. D.. Contagem de ovos do Aedes Aegypti em palhetas de ovitrampas baseada em Deep Learning. In: ENCONTRO UNIFICADO DE COMPUTAÇÃO DO PIAUÍ (ENUCOMPI), 14. , 2021, Picos. Anais [...]. Porto Alegre: Sociedade Brasileira de Computação, 2021 . p. 128-135. DOI: https://doi.org/10.5753/enucompi.2021.17763

- Artigo mais recente, não citado no artigo de revisão de Brun et al. (2020)
- Redes neurais para segmentação populares na literatura: U-Net, Segnet
- Resultados promissores com rede U-Net


### [Silva, R. 2021]

[mastersthesis] Rodrigo Emerson Valentim da Silva. Contagem automática de ovos do mosquito Aedes aegypti utilizando métodos de aprendizagem profunda e dispositivo de baixo custo. 2021. Dissertação (Mestrado em Ciências da Computação) - Universidade Federal de Pernambuco, Orientador: Leandro Maciel Almeida. https://repositorio.ufpe.br/handle/123456789/44637

- Disertação de mestrado abrangendo hardware e software
- Também não citado no artigo de revisão de Brun et al. (2020)
- Usa Redes Neurais Convolucionais (CNNs) 


## Seleção de publicações internacionais 

Strings de busca:

- computer vision counting mosquito eggs traps
- systematic review counting ovitraps


### [Hamesse et al. 2023]

[article] Charles Hamesse, Verónica Andreo, Carla Rodriguez Gonzalez, Charles Beumier, Jorge Rubio, Ximena Porcasi, Laura Lopez, Claudio Guzman, Rob Haelterman, Michal Shimoni, C. Marcelo Scavuzzo, Ovitrap Monitor - Online application for counting mosquito eggs and visualisation toolbox in support of health services, Ecological Informatics, v. 75, 2023. https://doi.org/10.1016/j.ecoinf.2023.102105

- *"an online open source and user-friendly integrated application that semi-automatically counts mosquito eggs from low-medium resolution mobile phone pictures"*
- validado com dataset de mais de 750 imagens

### [Santana Jr et al. 2020]

[article] Joaquim de Santana Junior, C., Alves Firmo, A. C., Albuquerque Paiva de Oliveira, R. F., Buarque Lins, P., Alves, G., & Ataide de Lima, R. (2020). A Solution for Counting Aedes aegypti and Aedes albopictus Eggs in Paddles from Ovitraps Using Deep Learning. IEEE Latin America Transactions, 17(12), 1987–1944. Retrieved from https://latamt.ieeer9.org/index.php/transactions/article/view/2459

- Solução baseada em deep learning (assim como outras mais recentes)

### [Gaburro et al. 2016]

[article] Gaburro J, Duchemin JB, Paradkar PN, Nahavandi S, Bhatti A. Assessment of ICount software, a precise and fast egg counting tool for the mosquito vector Aedes aegypti. Parasit Vectors. 2016 Nov 18;9(1):590. https://doi.org/10.1186%2Fs13071-016-1870-1

- Software muito citado em outros trabalhos
- Usado como referência para novos algoritmos




### [Chaves et al. 2022]

[article] Luis Fernando Chaves, José Angel Valerín Cordero, Gabriela Delgado, Carlos Aguilar-Avendaño, Ezequías Maynes, José Manuel Gutiérrez Alvarado, Melissa Ramírez Rojas, Luis Mario Romero, Rodrigo Marín Rodríguez, Modeling the association between Aedes aegypti ovitrap egg counts, multi-scale remotely sensed environmental data and arboviral cases at Puntarenas, Costa Rica (2017–2018), Current Research in Parasitology & Vector-Borne Diseases, v. 1, 2021 https://doi.org/10.1016/j.crpvbd.2021.100014

- Não é um trabalho sobre contagem automática, mas está relacionado
- Highlights

  - *"We sampled Ae. aegypti eggs using ovitraps for 80 weeks in Puntarenas, Costa Rica."*
  - *"We were able to correlate Ae. aegypti egg-counts and arboviral cases with remotely sensed data."*
  - *"Egg counts and arboviral cases were correlated with temperature and vegetation indices."*
  - *"Arboviral cases were not associated with egg counts."*


### [Brouazin et al. 2022]

[article] Brouazin, R., Claudel, I., Lancelot, R. et al. Optimization of oviposition trap settings to monitor populations of Aedes mosquitoes, vectors of arboviruses in La Reunion. Sci Rep 12, 18450 (2022). https://doi.org/10.1038/s41598-022-23137-5

- Não é um trabalho sobre contagem automática, mas está relacionado
- Traz recomendações sobre as armadilhas



## Software

- MECVision (Mosquito Egg Computer Vision) 

  - Project: https://gabrielkrieshok.com/blog/mosquito-egg-computer-vision/ (2020)
  - Source code: https://github.com/abtassociates/mecvision
  - Projeto sem publicação científica associada

- ICount

  - https://www.dropbox.com/sh/28vm6tv7wrm76ln/AADsCz8lQB37qU-n8j2qGjw_a?dl=0
  - Software citado em muitos artigos



## Questões

- Teremos acesso a uma grande quantidade/variedade de imagens?
- Tomaremos por referência imagens provenientes de alguma armadilha em particular?
- Integração com https://voceagente.fiocruz.br/: seria interessante conhecer o software existente antes de iniciar experimentos
- Experimentos já realizados (planilha mostrada em reunião online) usaram quais datasets e qual software?
