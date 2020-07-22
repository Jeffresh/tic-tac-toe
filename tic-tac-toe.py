class TicTacToe:

    def __init__(self):
        self.rows = [['_', '_', '_'] for _ in range(3)]

    def who_won(self, player):
        return (any(all([True if self.rows[i][j] == player else False for j in range(3)]) for i in range(3)) \
                or any(all([True if self.rows[j][i] == player else False for j in range(3)]) for i in range(3)) \
                or all(True if self.rows[i][i] == player else False for i in range(3)) \
                or all(True if self.rows[2 - i][i] == player else False for i in range(3)))

    def initialize_state(self):
        table = list(input('Enter cells:'))
        self.rows = [[table[i] for i in range(n, n + 3)] for n in (0, 3, 6)]

    def user_move(self, player):

        moved = False
        while not moved:
            try:
                x, y = input('Enter de coordinates:').split()
                x = int(x)
                y = int(y)
            except (UnboundLocalError, ValueError):
                print('You should enter numbers!')
            else:
                if x > 3 or y > 3 or x < 1 or y < 1:
                    print('Coordinates should be from 1 to 3!')
                else:
                    x, y = 3 - y, x - 1

                    if self.rows[x][y] in ['_', ' ']:
                        self.rows[x][y] = player
                        moved = True
                    else:
                        print('This cell is occupied! Choose another one!')

    def print_state(self):
        print('---------')
        for row in self.rows:
            print('|', *row, '|')
        print('---------')

    def game_state(self):
        x_number = sum(l.count('X') for l in self.rows)
        o_number = sum(l.count('O') for l in self.rows)

        game_ended = False

        if self.who_won('X'):
            print('X wins')
            game_ended = True
        elif self.who_won('O'):
            print('O wins')
            game_ended = True
        elif x_number + o_number != 9:
            print('Game not finished')
        else:
            print('Draw')
            game_ended = True

        return game_ended

    def new_game(self):
        players = ['X', 'O']
        time = 0
        self.print_state()
        while not self.game_state():
            self.user_move(players[time % 2])
            self.print_state()
            time += 1
        print('This game ends in {} rounds!'.format(time))


if __name__ == '__main__':
    my_game = TicTacToe()
    my_game.new_game()
