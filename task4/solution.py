import re


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:
    COLUMNS_VALUES = {'A': 0, 'B': 1, 'C': 2}
    ROW_VALUES = {'3': 0, '2': 1, '1': 2}
    SQUARE_VALUES = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self):
        self.deck = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        self.next_turn_value = 0
        self.winner = 0
        self.number_of_moves = 0

    def __str__(self):
        row_index = 3
        result = "\n  -------------\n"
        for x in self.deck:
            result += "{} |".format(row_index.__str__())
            for y in x:
                result += ' {} |'.format(self.SQUARE_VALUES[y])
            result += "\n  -------------\n"
            row_index -= 1
        result += "    A   B   C  \n"
        return result

    def get_position_indexes(self, key):
        result = list()
        result.append(self.ROW_VALUES[key[1]])
        result.append(self.COLUMNS_VALUES[key[0]])
        return result

    def check_for_invalid_key(self, key):
        pattern = r'[A-C][1-3]'
        result = bool(re.search(pattern, key))
        if not result:
            raise InvalidKey()

    def calculate_game_status(self):
        result = False
        first_diagonal_result = True
        second_diagonal_result = True
        for i in range(0, 3):
            #check diagonals
            if self.deck[i][i] != self.next_turn_value:
                first_diagonal_result = False
            if self.deck[i][2 - i] != self.next_turn_value:
                second_diagonal_result = False
            #check columns
            this_column_result = True
            for row in self.deck:
                if row[i] != self.next_turn_value:
                    this_column_result = False
                    break
            result = result or this_column_result
            #check rows
            this_row_result = True
            for square in self.deck[i]:
                if square != self.next_turn_value:
                    this_row_result = False
                    break
            result = result or this_row_result
        result = result or first_diagonal_result or second_diagonal_result
        if result:
            self.winner = self.next_turn_value

    def __getitem__(self, key):
        self.check_for_invalid_key(key)
        position = self.get_position_indexes(key)
        value_key = self.deck[position[0]][position[1]]
        return self.SQUARE_VALUES[value_key]

    def __setitem__(self, key, value):
        self.check_for_invalid_key(key)
        #check value
        if value != 'X' and value != 'O':
            raise InvalidValue()
        position = self.get_position_indexes(key)
        #check position
        if self.deck[position[0]][position[1]] != 0:
            raise InvalidMove()
        #check turn
        next_turn_value_string = self.SQUARE_VALUES[self.next_turn_value]
        if next_turn_value_string != value and next_turn_value_string != ' ':
            raise NotYourTurn()
        value_key = [k for k, v in self.SQUARE_VALUES.items() if v == value][0]
        self.deck[position[0]][position[1]] = value_key
        self.calculate_game_status()
        if value == 'X':
            self.next_turn_value = 2
        else:
            self.next_turn_value = 1
        self.number_of_moves += 1

    def game_status(self):
        if self.winner == 0:
            if self.number_of_moves < 9:
                return 'Game in progress.'
            else:
                return 'Draw!'
        elif self.winner == 1:
            return 'X wins!'
        else:
            return 'O wins!'
