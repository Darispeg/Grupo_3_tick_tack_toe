# ------------PROYECTO IA -----------------------------
# poda alfa-beta :)
import time

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # Player X always plays first
        self.player_turn = 'X'
  #----------------------------------------------------------------------------------------------------
    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()
# Determina si el movimiento realizado es un movimiento valido
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
               return False
        else:
            return True 

#-------------------------------------------------------------------------------------------------
    # Comprueba si el juego ha terminado y devuelve el ganador en cada caso.
    def is_end(self):
    # Vertical 
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

    # Horizontal 
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                  return 'O'

    # Main diagonal 
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

    # Second diagonal 
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

    #¿Está llena toda la tabla?
        for i in range(0, 3):
            for j in range(0, 3):
            # hay un campo vacío, continuamos el juego
                if (self.current_state[i][j] == '.'):
                    return None

    # Es un empate !
        return '.'

#--------------------------------------------------------------------------------------------------------

    def max_alpha_beta(self, alpha, beta):
            maxv = -2
            px = None
            py = None

            result = self.is_end()

            if result == 'X':
                return (-1, 0, 0)
            elif result == 'O':
                return (1, 0, 0)
            elif result == '.':
                return (0, 0, 0)

            for i in range(0, 3):
                for j in range(0, 3):
                    if self.current_state[i][j] == '.':
                        self.current_state[i][j] = 'O'
                        (m, min_i, in_j) = self.min_alpha_beta(alpha, beta)
                        if m > maxv:
                            maxv = m
                            px = i
                            py = j
                        self.current_state[i][j] = '.'

                    # Los siguientes dos ifs en Max y Min son la única diferencia entre el algoritmo regular y minimax
                        if maxv >= beta:
                            return (maxv, px, py)

                        if maxv > alpha:
                            alpha = maxv

            return (maxv, px, py)
        #---------------------------------------------------------------------------------------
    def min_alpha_beta(self, alpha, beta):

            minv = 2

            qx = None
            qy = None

            result = self.is_end()

            if result == 'X':
                return (-1, 0, 0)
            elif result == 'O':
                return (1, 0, 0)
            elif result == '.':
                return (0, 0, 0)

            for i in range(0, 3):
                for j in range(0, 3):
                    if self.current_state[i][j] == '.':
                        self.current_state[i][j] = 'X'
                        (m, max_i, max_j) = self.max_alpha_beta(alpha, beta)
                        if m < minv:
                            minv = m
                            qx = i
                            qy = j
                        self.current_state[i][j] = '.'

                        if minv <= alpha:
                            return (minv, qx, qy)

                        if minv < beta:
                            beta = minv

            return (minv, qx, qy)
        #----------------------------------------------------------------------------------------------------
    def play_alpha_beta(self):
        while True:
            self.draw_board()
            self.result = self.is_end()

            if self.result != None:
                if self.result == 'X':
                    print('gano el Humano!')
                elif self.result == 'O':
                    print('Gano la IA!')
                elif self.result == '.':
                    print("Es un Empate!")


                self.initialize_game()
                return

            if self.player_turn == 'X':

                while True:
                    start = time.time()
                    (m, qx, qy) = self.min_alpha_beta(-2, 2)
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))

                    qx = px
                    qy = py

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')

            else:
                (m, px, py) = self.max_alpha_beta(-2, 2)
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'
#----------------------------------------------------------------------------------------
def main():
        g=Game()
        g.play_alpha_beta()
if __name__ == "__main__":
    main()