# KubaGame

## Overview
KubaGame is a Python implementation of the classic Kuba board game. In this strategic game, two players compete with the objective of capturing 7 neutral red marbles, capturing all of the opponent's marbles, or blocking all possible moves of the opponent. The game is played on a 7x7 grid filled with white, black, and red marbles.

## Installation
No specific installation process is required for KubaGame. It is written in Python and does not depend on external libraries.

## Usage
To start playing KubaGame, you need to initialize the game and set up the players. Here's a quick example of how to get started:

```python
from kubagame import KubaGame

# Initialize the game
game = KubaGame()

# Set up players
player1 = ("Player1", ["White", 8])
player2 = ("Player2", ["Black", 8])
game.set_players(player1, player2)

# Start the game loop
game.play_game()
```

### Features
- Interactive game loop with user input for moves.
- Checks for valid moves, including compliance with Kuba rules.
- Tracks captured marbles and determines game winner.

## Documentation
For detailed information on the game mechanics and the methods available in the KubaGame class, please refer to the [KubaGame Documentation]()

## License
KubaGame is released under the [MIT License](/LICENSE).

## Authors
- Deepak Saikumar Lukulapu
- Monika Kaminei

## Acknowledgments
- This project is completely inspired by Internet.

