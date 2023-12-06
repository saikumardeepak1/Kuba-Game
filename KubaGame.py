class KubaGame:
    """Represents a KubaGame object with game mechanics."""

    def __init__(self, player1, player2):
        """Creates a KubaGame with players, a board, and a marble count."""
        self._players = [player1, player2]
        self._player_banks = [[0, 0], [0, 0]]
        self._current_player, self._board = None, [
            ["W", "W", "X", "X", "X", "B", "B"],
            ["W", "W", "X", "R", "X", "B", "B"],
            ["X", "X", "R", "R", "R", "X", "X"],
            ["X", "R", "R", "R", "R", "R", "X"],
            ["X", "X", "R", "R", "R", "X", "X"],
            ["B", "B", "X", "R", "X", "W", "W"],
            ["B", "B", "X", "X", "X", "W", "W"]
        ]
        self._prev_boards = [None, None]
        self._winner = None
        self._initialize_prev_boards()

    def _initialize_prev_boards(self):
        """Initialize previous boards for both players."""
        self._prev_boards[0] = [row[:] for row in self._board]
        self._prev_boards[1] = [row[:] for row in self._board]

    def _set_current_player(self, player_name):
        """Set the current player if it's the first move."""
        if self._current_player is None:
            self._current_player = player_name

    def get_current_turn(self):
        """Returns the player name whose turn it is. Otherwise, returns None if no player has made the first move."""
        return self._current_player

    def make_move(self, player_name, coordinates, direction):
        """Makes a move on the board through user input validation."""
        self._set_current_player(player_name)

        player, player_marble = self._get_player_info(player_name)
        if not self._validate_move(player, coordinates, direction):
            return False

        row, column = coordinates
        move, end_index, captured_marble = self._perform_move(row, column, direction, player_marble)
        self._update_board(row, column, move, direction)

        if not self._check_ko_rule(player):
            self._restore_board(player)
            return False

        winner = self._check_winner(player, captured_marble)
        if winner:
            self._winner = winner
        else:
            self._switch_turn()

        return True

    def _get_player_info(self, player_name):
        """Get player information based on the provided player name."""
        for player in self._players:
            if player[0] == player_name:
                return player

        raise ValueError(f"Invalid player name: {player_name}")

    def _validate_move(self, player, coordinates, direction):
        """Validate if the move is legal."""
        if not self._validate_player(player):
            return False
        row, column = coordinates
        if not self._validate_coordinates(row, column):
            return False
        if not self._validate_direction(row, column, direction):
            return False
        return True

    def _validate_player(self, player):
        """Validate if it's the correct player's turn."""
        if player[0] != self._current_player:
            raise ValueError(f"Invalid move. It's not {player[0]}'s turn.")

    def _validate_coordinates(self, row, column):
        """Validate if the coordinates are within the board."""
        if not (0 <= row <= 6 and 0 <= column <= 6):
            raise ValueError("Invalid coordinates. Coordinates must be within the range (0,0) to (6,6).")

    def _validate_direction(self, row, column, direction):
        """Validate if the direction of the player's move is valid."""
        forward, backward, right, left = row - 1, row + 1, column + 1, column - 1

        if direction == "F" and backward != 7:
            if row == 0 or self._board[backward][column] != "X":
                raise ValueError("Invalid move.")
        elif direction == "B" and forward != -1:
            if row == 6 or self._board[forward][column] != "X":
                raise ValueError("Invalid move.")
        elif direction == "R" and left != -1:
            if column == 6 or self._board[row][left] != "X":
                raise ValueError("Invalid move.")
        elif direction == "L" and right != 7:
            if column == 0 or self._board[row][right] != "X":
                raise ValueError("Invalid move.")

    def _perform_move(self, row, column, direction, player_marble):
        """Perform the move and return the move, end index, and captured marble."""
        move, end_index, captured_marble = [], None, None
        board_column = [rows[column] for rows in self._board]

        if direction == "F":
            move, end_index, captured_marble = self._make_forward_move(row, column, board_column, player_marble)
        elif direction == "B":
            move, end_index, captured_marble = self._make_backward_move(row, column, board_column, player_marble)
        elif direction == "L":
            move, end_index, captured_marble = self._make_left_move(row, column, self._board[row], player_marble)
        elif direction == "R":
            move, end_index, captured_marble = self._make_right_move(row, column, self._board[row], player_marble)

        return move, end_index, captured_marble

    def _make_forward_move(self, row, column, board_column, player_marble):
        """Make forward move and return the move, end index, and captured marble."""
        move, end_index, captured_marble = [], None, None

        for square in range(row, -1, -1):
            if board_column[square] == "X":
                end_index = square
                break

        if end_index is not None:
            move = ["X"] + move + [board_column[square] for square in range(len(board_column) - 1, -1, -1) if square != end_index]
        else:
            captured_marble = board_column[0]
            if captured_marble == player_marble:
                return move, end_index, captured_marble
            move = ["X"] + move + [board_column[square] for square in range(len(board_column) - 1, 0, -1)]

        return move, end_index, captured_marble

    def _make_backward_move(self, row, column, board_column, player_marble):
        """Make backward move and return the move, end index, and captured marble."""
        move, end_index, captured_marble = [], None, None

        for square in range(row, len(board_column)):
            if board_column[square] == "X":
                end_index = square
                break

        if end_index is not None:
            move = ["X"] + move + [board_column[square] for square in range(len(board_column)) if square != end_index]
        else:
            captured_marble = board_column[len(board_column) - 1]
            if captured_marble == player_marble:
                return move, end_index, captured_marble
            move = ["X"] + move + [board_column[square] for square in range(len(board_column) - 1)]

        return move, end_index, captured_marble

    def _make_left_move(self, row, column, board_row, player_marble):
        """Make left move and return the move."""
        move, end_index = [], None

        for square in range(column, -1, -1):
            if board_row[square] == "X":
                end_index = square
                break

        if end_index is not None:
            move = ["X"] + move + [board_row[square] for square in range(len(board_row) - 1, -1, -1) if square != end_index]
        else:
            captured_marble = board_row[0]
            if captured_marble == player_marble:
                return move, end_index
            move = ["X"] + move + [board_row[square] for square in range(len(board_row) - 1, 0, -1)]

        return move, end_index

    def _make_right_move(self, row, column, board_row, player_marble):
        """Make right move and return the move."""
        move, end_index = [], None

        for square in range(column, len(board_row)):
            if board_row[square] == "X":
                end_index = square
                break

        if end_index is not None:
            move = move + [board_row[square] for square in range(len(board_row)) if square != end_index] + ["X"]
        else:
            captured_marble = board_row[len(board_row) - 1]
            if captured_marble == player_marble:
                return move, end_index
            move = move + [board_row[square] for square in range(len(board_row) - 1)]

        return move, end_index

    def _update_board(self, row, column, move, direction):
        """Update the board with the performed move."""
        if direction == "F" or direction == "B":
            index = 0
            for r in range(len(self._board)):
                self._board[r][column] = move[index]
                index += 1
        elif direction == "L" or direction == "R":
            self._board[row] = move

    def _check_ko_rule(self, player):
        """Check the ko rule to ensure the move is valid."""
        prev_board = self._prev_boards[0] if player[0] == self._players[0][0] else self._prev_boards[1]
        if prev_board == self._board:
            self._restore_board(player)
            return False
        else:
            prev_board = [row[:] for row in self._board]
            return True

    def _restore_board(self, player):
        """Restore the board to its previous state."""
        if player[0] == self._players[0][0]:
            self._board = [row[:] for row in self._prev_boards[0]]
        else:
            self._board = [row[:] for row in self._prev_boards[1]]

    def _check_winner(self, player, captured_marble):
        """Check if there is a winner based on the move."""
        if captured_marble == "R":
            player[1][0] += 1
        elif captured_marble == self._get_opponent(player)[1]:
            player[1][1] += 1

        if player[1][0] == 7 or player[1][1] == 8:
            return player[0]
        elif self._get_opponent(player)[1][0] == 7 or self._get_opponent(player)[1][1] == 8:
            return self._get_opponent(player)[0]

    def _get_opponent(self, player):
        """Get the opponent's information."""
        return self._players[0] if player[0] == self._players[1][0] else self._players[1]

    def _switch_turn(self):
        """Switch the turn to the next player."""
        self._current_player = self._players[1][0] if self._current_player == self._players[0][0] else self._players[0][0]
        raise ValueError("Invalid move. Failed to switch turn.")

    def get_winner(self):
        """Returns the name of the winning player."""
        return self._winner

    def get_captured(self, player_name):
        """Returns the number of Red marbles captured by the given player name. Else, returns None."""
        player = self._players[0] if player_name == self._players[0][0] else self._players[1]
        return player[1][0]

    def get_marble(self, coordinates):
        """Returns the marble that is present at the coordinate location."""
        return self._board[coordinates[0]][coordinates[1]]

    def get_marble_count(self):
        """Returns the number of white, black, and red marbles as a tuple in the order (W,B,R)."""
        player1_marbles, player2_marbles = self._players[0][1][1], self._players[1][1][1]
        total_white = 8 - player1_marbles - player2_marbles
        total_black = player1_marbles + player2_marbles
        total_red = self._player_banks[0][0] + self._player_banks[1][0]

        return total_white, total_black, total_red
