# IA 2023/2024

## Project 1: Terrace Game

### Dependencies

#### Python **PyGame** library

To develop the game, we opted to use the pygame module. This needs to be installed prior to running the game, in case you don't already have it.

```bash
pip install pygame
```

### Running the Game

From the `terrace` folder, execute:

* Linux
```bash
python3 main.py
```

* Windows
```bash
python main.py
```

### Checkpoint (11/Março)

Each group must **submit in Moodle** a brief presentation (max. 5 slides), in **PDF format**, which will be used in the class to analyze, together with the teacher, the progress of the work.

The presentation should contain:
1. Specification of the work to be performed (definition of the game or optimization problem to be solved)

2. Related work with references to works found in a bibliographic search (articles, web pages, and/or source code)

3. Formulation of the problem as a search problem (state representation, initial state, objective test, operators (names, preconditions, effects, and costs), heuristics/evaluation function) or optimization problem (solution representation, neighborhood/mutation and crossover functions, hard constraints, evaluation functions)

4. Implementation work already carried out (programming language, development environment, data structures, among others)

### TODO Checklist

- [x] Criar representação básica do tabuleiro

- [x] Fazer os slides

- [x] Melhorar a representação das peças, para terem diferentes tamanhos e serem facilmente indentificadas (talvez usar contorno de cores diferentes)

- [x] Melhorar a representação das plataformas para ser mais facilmente distinguível quais estão mais acima e quais mais abaixo? Ou pôr uma legenda ao lado a explicar qual côr é a mais baixa e qual a mais alta?

- [x] Criar user input para selecionar e mover peças

- [x] Criar um menu para poder decidir qual o modo de jogo (player vs player, ai vs ai, ai vs player)

- [ ] Definir o problema como um search problem para colocar nos slides a entregar no checkpoint

- [x] Dividir a implementação de AI para o seu próprio ficheiro

- [ ] Definir estrutura de dados a usar para o jogo ??

- ...
