class TicTacToe:

    def __init__(self):
        self.rows = []

    def empty_table(self, ):
        print('---------')
        print('| _ _ _ |')
        print('| _ _ _ |')
        print('| _ _ _ |')
        print('---------')

    def who_won(self, player):
        return (self.rows[0][0] == player and self.rows[0][1] == player and self.rows[0][2] == player \
                or self.rows[1][0] == player and self.rows[1][1] == player and self.rows[1][2] == player \
                or self.rows[2][0] == player and self.rows[2][1] == player and self.rows[2][2] == player \
                or self.rows[0][0] == player and self.rows[1][0] == player and self.rows[2][0] == player \
                or self.rows[0][1] == player and self.rows[1][1] == player and self.rows[2][1] == player \
                or self.rows[0][2] == player and self.rows[1][2] == player and self.rows[2][2] == player \
                or self.rows[0][0] == player and self.rows[1][1] == player and self.rows[2][2] == player \
                or self.rows[0][2] == player and self.rows[1][1] == player and self.rows[2][0] == player)

    def initialize_state(self):
        table = input('Enter cells:')
        self.rows = [list(table[0:3]), list(table[3:6]), list(table[6:9])]

    def user_move(self):

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
                        self.rows[x][y] = 'X'
                        moved = True
                    else:
                        print('This cell is occupied! Choose another one!')

    def state(self):

        x_number = sum(l.count('X') for l in self.rows)
        o_number = sum(l.count('O') for l in self.rows)

        if x_number + o_number == 0:
            self.empty_table()
        else:
            print('---------')
            for row in self.rows:
                print('| ', end='')
                for c in row:
                    print(c + ' ', end='')
                print('|')
            print('---------')

        # if abs(x_number - o_number) > 1 or self.who_won('X') and self.who_won('O'):
        #     print('Impossible')
        # elif self.who_won('X'):
        #     print('X wins')
        # elif self.who_won('O'):
        #     print('O wins')
        # elif x_number + o_number != 9:
        #     print('Game not finished')
        # else:
        #     print('Draw')


if __name__ == '__main__':
    my_game = TicTacToe()
    my_game.initialize_state()
    my_game.state()
    my_game.user_move()
    my_game.state()
