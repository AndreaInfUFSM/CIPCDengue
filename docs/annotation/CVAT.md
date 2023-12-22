<!--
author:   Andrea Charão

email:    andrea@inf.ufsm.br

version:  0.0.1

language: PT-BR

narrator: Brazilian Portuguese Female

comment:  Review sobre Visão Computacional aplicada a contagem de ovos de mosquitos

-->



# Anotação de imagens com CVAT


> Resumo para projeto de contagem de ovos em ovitrampas

Profa. Andrea Schwertner Charão

Depto. de Linguagens e Sistemas de Computação, Centro de Tecnologia, UFSM


## Contexto

O que é anotação de imagens?

- Processo de demarcação e rotulagem de objetos em imagens
- Provê contexto e informação de entrada para algoritmos de aprendizagem de máquina

Por que é importante?

- Para treinar modelos de aprendizagem de máquina a reconhecer nossos objetos de interesse

- Para obter altas taxas de acertos e generalização no reconhecimento / contagem de objetos



## CVAT (Computer Vision Annotation Tool)

- Uma dentre várias ferramentas populares e em rápida evolução
- Ferramenta open source (https://github.com/opencv/cvat) associada a serviço em nuvem (https://www.cvat.ai/)
- Plano gratuito oferece recursos suficientes para nosso caso

![](img/cvat-home.png)

## Conceitos do workflow de anotação com CVAT

- **Organization**: grupo de usuários trabalhando em conjunto

  - Plano gratuito permite 1 organization com 3 usuários

- **Project**: conjunto de tarefas de anotação com características em comum

  - Aqui são definidos labels a serem usados nas anotações (exemplo: egg, cluster, unsure)

- **Task**: conjunto de uma ou mais imagens a anotar

  - Usa labels padronizados definidos em Project

- **Job**: realização de anotações sobre imagens de uma Task



## Passos


### Criar conta

Criar uma conta em: https://app.cvat.ai/auth/register (abrir email e clicar no link de confirmação para ativar a conta)

![](img/cvat-register.png)

### Login

Após Login, é mostrada uma tela com Tasks (inicialmente vazia)

![](img/cvat-empty.png)


### Criar Project

Conjunto de tarefas de anotaçõo com características em comum


![](img/cvat-newproject.png)

#### Configurar projeto

- Prencher nome do projeto: `eggcounting`
- Criar labels: clicar em `Add label`
- A cada novo label, clicar em `Continue`

- Label para um ovo (quando for possível distinguir com certeza)

  - Label name: `egg`
  - Selecionar `Ellipse`
  - Escolher cor


- Label para um agrupamento de ovos (quando houver sobreposição que impeça distinguir ovos isoladamente)

  - Label name: `cluster`
  - Selecionar `Any`
  - Escolher cor

- Label para possível ovo (incerteza)

  - Label name: `unsure`
  - Selecionar `Any`
  - Escolher cor


#### Projeto configurado com labels

Estado final da configuração do projeto após cadastro de labels

![](img/cvat-new-project-labels.png)


### Criar Task

Task é um conjunto de imagens a anotar.

![](img/cvat-newtask.png)


#### Configurar Task

- Clicar em botão `+` para adicionar Task (`Create a new task`)

- Name: definir nome da Task
- Project: selecionar  `eggcounting`
- Select files: `My computer` (selecionar imagens a serem anotadas)
- Submit & Open

#### Task configurada

![](img/cvat-task-jobs.png)

### Realizar Job

Job é uma sessão de anotações sobre imagens de uma Task.

- Quando uma Task é criada, automaticamente já é criado um Job

- Clicar sobre um Job para ver a imagem e as opções de anotação

![](img/cvat-task-jobs.png)


#### Ferramentas e imagem

Tela do job mostra a imagem e várias ferramentas

![](img/cvat-job-default.png)


#### Anotação de ovos

Controles

- Zoom in/out: scroll do mouse
- Mover imagem: segurar botão esquerdo do mouse

Ovos

- Selecionar Elipse e Shape no menu à esquerda
- Desenhar elipse próximo ao ovo
- Ajustar tamanho e rotação
- Usar atalhos e copy-paste para os próximos


![](img/cvat-job.png)

## Referências

- Tasks: https://opencv.github.io/cvat/docs/manual/basics/create_an_annotation_task/

- https://lapix.ufsc.br/ensino/visao/visao-computacionaldeep-learning/deep-learningensinando-rede-ferramentas-de-anotacao/?lang=en