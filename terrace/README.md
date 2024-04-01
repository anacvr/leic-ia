# IA 2023/2024

## Project 1: Terrace Game

### Dependencies

#### Python **PyGame** library

To develop the game, we opted to use the pygame module.
This needs to be installed prior to running the game, in case you don't already have it.

```bash
pip install pygame
```

#### Audio Device

This game requires an output audio device because there is music included when the player wins.
If you are running the game on Windows, you don't need to do anything (and can skip this step).
If you are running this on ***wsl***, you need to install `pulseaudio`, so the program can access your audio device.

```bash
sudo apt-get install pulseaudio
```

### Running the Game

From the `terrace` folder, execute:

* on Linux:
```bash
python3 main.py
```

* on Windows:
```bash
python main.py
```

### About the game

#### Overview
* Strategy game played on 3D board with 64 squares
* Arranged in L-shaped levels (terraces) that rise from the lowest point in two diagonally opposite corners to highest points in the other two corners

#### Pieces
* Four different sizes and all of them move alike
* "T" piece serves a role similar to the king in chess

#### Objective
There are 2 ways a player can win:
* Moving his "T" piece from its starting corner to the opposite corner
* Capturing the opponent’s "T" piece

