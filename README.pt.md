[[🇬🇧] Read in English](./README.md)

# Asteroids

Uma recriação moderna do clássico **Asteroids (1979)** da Atari, desenvolvida em **Python** utilizando **Pygame**.

Controle sua nave espacial em um campo de asteroides infinito, destrua discos voadores inimigos, acumule pontos e sobreviva o máximo possível. O projeto busca reproduzir a experiência do arcade original enquanto aplica boas práticas de desenvolvimento de software, com uma arquitetura modular e orientada a objetos.

## Visão Geral

O jogo apresenta gráficos vetoriais inspirados na versão original de 1979, sistema de pontuação, vidas extras, efeitos sonoros clássicos e mecânicas fiéis ao arcade.

## Funcionalidades

### Jogabilidade

* Mecânicas inspiradas no Asteroids original
* Ondas contínuas de asteroides
* Asteroides grandes, médios e pequenos
* Sistema de fragmentação de asteroides
* Movimentação com efeito de "wrap-around" nas bordas da tela
* Sistema de vidas
* Vida extra a cada **10.000 pontos**
* Discos voadores inimigos (Saucers)
* Projéteis inimigos
* Sistema de pausa
* Tela de Game Over e reinício da partida

### Recursos Visuais

* Gráficos vetoriais em estilo retrô
* Asteroides gerados proceduralmente
* Efeitos de explosão com partículas
* HUD inspirado no arcade original
* Fonte clássica Hyperspace

### Áudio

* Sons de disparo
* Sons de propulsão da nave
* Sons de explosão
* Sons dos discos voadores
* Efeito sonoro de vida extra

### Arquitetura

* Desenvolvimento orientado a objetos
* Gerenciador de colisões dedicado
* Gerenciador de estados do jogo
* Sistema centralizado de áudio
* Separação entre lógica, interface e entidades

## Controles

| Tecla              | Ação               |
| ------------------ | ------------------ |
| ← / →              | Rotacionar nave    |
| ↑                  | Propulsão          |
| Espaço             | Disparar           |
| Enter              | Iniciar jogo       |
| P                  | Pausar / Continuar |
| Espaço (Game Over) | Reiniciar partida  |

## Estrutura do Projeto

```text
asteroids/
├── run_game.py
├── res/
│   ├── FIRE.WAV
│   ├── LIFE.WAV
│   ├── THRUST.WAV
│   ├── EXPLODE1.WAV
│   ├── EXPLODE2.WAV
│   ├── EXPLODE3.WAV
│   ├── SSAUCER.WAV
│   ├── LSAUCER.WAV
│   └── Hyperspace.otf
│
└── src/
    ├── audio/
    ├── core/
    ├── entities/
    ├── ui/
    └── constants.py
```

## Instalação

### Requisitos

* Python 3.10 ou superior
* Pygame

### Clonando o repositório

```bash
git clone https://github.com/ericshantos/asteroids.git
cd asteroids
```

### Instalando as dependências

```bash
pip install pygame
```

## Executando o Jogo

```bash
python run_game.py
```

## Mecânicas de Pontuação

| Alvo                 | Pontos |
| -------------------- | ------ |
| Asteroide Grande     | 20     |
| Asteroide Médio      | 50     |
| Asteroide Pequeno    | 100    |
| Disco Voador Grande  | 200    |
| Disco Voador Pequeno | 1000   |

### Vidas Extras

Uma vida extra é concedida a cada:

```text
10.000 pontos
```

## Destaques Técnicos

### Sistema de Colisão

O jogo utiliza um gerenciador centralizado responsável por:

* Colisões entre jogador e asteroides
* Colisões entre projéteis e asteroides
* Colisões entre projéteis e discos voadores
* Colisões entre projéteis inimigos e o jogador

### Fragmentação dos Asteroides

Os asteroides se dividem conforme seu tamanho:

```text
Grande → 3 Médios
Médio → 2 Pequenos
Pequeno → Destruído
```

### Gerenciamento de Estados

O fluxo do jogo é controlado pelos estados:

```text
START
PLAYING
PAUSE
GAME_OVER
```

## Objetivos de Aprendizagem

Este projeto foi desenvolvido com foco em estudos e aprimoramento de conhecimentos em:

* Programação Orientada a Objetos (POO)
* Desenvolvimento de jogos com Pygame
* Programação orientada a eventos
* Detecção de colisões
* Gerenciamento de estados
* Arquitetura de software modular

## Recursos Utilizados

* Efeitos sonoros inspirados no arcade original
* Fonte Hyperspace
* Renderização vetorial personalizada

## Licença

Este projeto está licenciado sob a licença MIT.

Consulte o arquivo `LICENSE` para mais informações.