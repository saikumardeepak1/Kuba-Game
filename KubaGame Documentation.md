
# KubaGame Class Documentation

## Overview
The KubaGame class represents the game mechanics for the board game Kuba, a two-player abstract strategy game played on a 7x7 board. The game involves moving marbles on the board and capturing opponent marbles.

## Class Structure

### Attributes
- `_players`: A list containing information about the two players (name, marbles).
- `_player_banks`: A list containing the count of marbles captured by each player.
- `_current_player`: A string representing the name of the current player.
- `_board`: A 7x7 list representing the game board.
- `_prev_boards`: A list containing the previous state of the board for each player.
- `_winner`: A string representing the name of the winning player.

### Methods

#### `_init_(self)`
- Initializes a new KubaGame object with default values, including an initial game board.

#### `set_players(self, player1, player2)`
- Sets the information for Player 1 and Player 2.

#### `_initialize_prev_boards(self)`
- Initializes the previous state of the board for both players.

#### `_set_current_player(self, player_name)`
- Sets the current player if it's the first move.

#### `_get_current_player(self)`
- Returns the name of the current player.

#### `make_move(self, coordinates, direction)`
- Performs a move on the board based on user input.
- Validates the move and updates the board accordingly.

#### `_get_player_info(self, player_name)`
- Returns information about the player based on the provided player name.

#### `_validate_move(self, player, coordinates, direction)`
- Validates if the move is legal.

#### `_validate_player(self, player)`
- Validates if it's the correct player's turn.

#### `_validate_coordinates(self, row, column)`
- Validates if the coordinates are within the board.

#### `_validate_direction(self, row, column, direction)`
- Validates if the direction of the player's move is valid.

#### `_perform_move(self, row, column, direction, player_marble)`
- Performs the move and returns the move, end index, and captured marble.

#### `_make_forward_move(self, row, column, board_column, player_marble)`
- Makes a forward move and returns the move, end index, and captured marble.

#### `_make_backward_move(self, row, column, board_column, player_marble)`
- Makes a backward move and returns the move, end index, and captured marble.

#### `_make_left_move(self, row, column, board_row, player_marble)`
- Makes a left move and returns the move and end index.

#### `_make_right_move(self, row, column, board_row, player_marble)`
- Makes a right move and returns the move and end index.

#### `_update_board(self, row, column, move, direction)`
- Updates the board with the performed move.

#### `_check_ko_rule(self, player)`
- Checks the ko rule to ensure the move is valid.

#### `_restore_board(self, player)`
- Restores the board to its previous state.

#### `_check_winner(self, player, captured_marble)`
- Checks if there is a winner based on the move.

#### `_get_opponent(self, player)`
- Returns information about the opponent.

#### `_switch_turn(self)`
- Switches the turn to the next player.

#### `get_winner(self)`
- Returns the name of the winning player.

#### `get_captured(self, player_name)`
- Returns the number of Red marbles captured by the given player name.

#### `get_marble(self, coordinates)`
- Returns the marble present at the specified coordinates.

#### `get_marble_count(self)`
- Returns the count of white, black, and red marbles.

#### `play_game(self)`
- Starts and manages the Kuba game.

#### `_print_board(self)`
- Prints the current state of the game board.

#### `_print_player_turn(self)`
- Prints the current player's turn.

#### `_print_winner(self)`
- Prints the winner of the game.

#### `_print_captured(self, player_name)`
- Prints the number of Red marbles captured by the given player.

#### `_print_marble_count(self)`
- Prints the total count of white, black, and red marbles.

#### `_print_feedback(self, move_successful)`
- Prints feedback based on the success of the move.

## Usage
- Create a KubaGame object.
- Set players using the `set_players` method.
- Play the game using the `play_game` method.
