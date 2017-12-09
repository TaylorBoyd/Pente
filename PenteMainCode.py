class Board(object):

    def __init__(self, height, width):

        self.width = width
        self.height = height
        self.winner = False
        self.spaces = {}

        for x in range(self.width):
            for y in range(self.height):
                self.spaces[(x, y)] = "+"

    def is_stone_at_position(self, x, y):

        if self.spaces[(x, y)] == "+":
            return False
        else:
            return True
        
    def clear_board(self):
        for x in range(self.width):
            for y in range(self.height):
                self.spaces[(x, y)] = "+"
        self.winner = False

    def is_winner(self):
        return self.winner

    def set_winner(self):
        self.winner = True
        
    def is_on_board(self, x, y):

        return (0 <= x <= self.width - 1) and (0 <= y <= self.height - 1)

    def place_stone(self, x, y, stone):

        
        if not self.is_stone_at_position(x, y):
            self.spaces[(x, y)] = stone
        else:
            print("Already a stone at that position")

    def show_board(self):

        for y in range(self.height - 1, -1, -1):
            board_line = ""
            for x in range(self.width):
                board_line = board_line + self.spaces[(x, y)] + " "

            print(board_line)

    def remove_stone(self, x, y):

        self.spaces[(x, y)] = "+"

    def capture_stones(self, x, y, stone):
        """Takes in a position and a players stone
        Looks first to see if a capture is even possible by a player having a stone 3 spaces away
        Then checks the space in between for possible captures
        Removes the stones and returns the number of captures made
        """

        captures = 0

        try:
            if self.spaces[(x+3, y+0)] == stone:
                if self.spaces[(x+1, y+0)] != stone and self.is_stone_at_position(x+1, y+0):
                    if self.spaces[(x+2, y+0)] != stone and self.is_stone_at_position(x+2, y+0):
                        captures += 1
                        self.remove_stone(x+1, y)
                        self.remove_stone(x+2, y)
        except KeyError:
            pass

        try:            
            if self.spaces[(x-3, y+0)] == stone:
                if self.spaces[(x-1, y+0)] != stone and self.is_stone_at_position(x-1, y+0):
                    if self.spaces[(x-2, y+0)] != stone and self.is_stone_at_position(x-2, y+0):
                        captures += 1
                        self.remove_stone(x-1, y)
                        self.remove_stone(x-2, y)
        except KeyError:
            pass
        
        try:            
            if self.spaces[(x+0, y+3)] == stone:
                if self.spaces[(x+0, y+1)] != stone and self.is_stone_at_position(x+0, y+1):
                    if self.spaces[(x+0, y+2)] != stone and self.is_stone_at_position(x+0, y+2):
                        captures += 1
                        self.remove_stone(x, y+1)
                        self.remove_stone(x, y+2)
        except KeyError:
            pass
                    
        try:
            if self.spaces[(x+0, y-3)] == stone:
                if self.spaces[(x+0, y-1)] != stone and self.is_stone_at_position(x+0, y-1):
                    if self.spaces[(x+0, y-2)] != stone and self.is_stone_at_position(x+0, y-2):
                        captures += 1
                        self.remove_stone(x, y-1)
                        self.remove_stone(x, y-2)
        except KeyError:
            pass

        try:            
            if self.spaces[(x+3, y+3)] == stone:
                if self.spaces[(x+1, y+1)] != stone and self.is_stone_at_position(x+1, y+1):
                    if self.spaces[(x+2, y+2)] != stone and self.is_stone_at_position(x+2, y+2):
                        captures += 1
                        self.remove_stone(x+1, y+1)
                        self.remove_stone(x+2, y+2)
        except KeyError:
            pass

        try:            
            if self.spaces[(x+3, y-3)] == stone:
                if self.spaces[(x+1, y-1)] != stone and self.is_stone_at_position(x+1, y-1):
                    if self.spaces[(x+2, y-2)] != stone and self.is_stone_at_position(x+2, y-2):
                        captures += 1
                        self.remove_stone(x+1, y-1)
                        self.remove_stone(x+2, y-2)
        except KeyError:
            pass

        try:            
            if self.spaces[(x-3, y+3)] == stone:
                if self.spaces[(x-1, y+1)] != stone and self.is_stone_at_position(x-1, y+1):
                    if self.spaces[(x-2, y+2)] != stone and self.is_stone_at_position(x-2, y+2):
                        captures += 1
                        self.remove_stone(x-1, y+1)
                        self.remove_stone(x-2, y+2)
        except KeyError:
            pass

        try:            
            if self.spaces[(x-3, y-3)] == stone:
                if self.spaces[(x-1, y-1)] != stone and self.is_stone_at_position(x-1, y-1):
                    if self.spaces[(x-2, y-2)] != stone and self.is_stone_at_position(x-2, y-2):
                        captures += 1
                        self.remove_stone(x-1, y-1)
                        self.remove_stone(x-2, y-2)
        except KeyError:
            pass

        return captures

    def five_in_a_row(self, x, y, stone):
        """ Takes in the stone position and a player stone
        Checks in each direction for 5 in a row
        Returns True if there is a Pente or False otherwise
        """
        
        count_vertical = 0
        count_horizontal = 0
        count_diagonal_1 = 0
        count_diagonal_2 = 0
        
        
        for i in range(-4, 5):
            
            if self.is_on_board(x+i, y):
                if self.spaces[(x+i, y)] == stone:
                    count_vertical += 1
                else:
                    count_vertical = 0

                if count_vertical >= 5:
                    return True

            if self.is_on_board(x, y+i):
                if self.spaces[(x, y+i)] == stone:
                    count_horizontal += 1
                else:
                    count_horizontal = 0

                if count_horizontal >= 5:
                    return True

            if self.is_on_board(x+i, y+i):
                if self.spaces[(x+i, y+i)] == stone:
                    count_diagonal_1 += 1
                else:
                    count_diagonal_1 = 0

                if count_diagonal_1 >= 5:
                    return True

            if self.is_on_board(x+i, y-i):
                if self.spaces[(x+i, y-i)] == stone:
                    count_diagonal_2 += 1
                else:
                    count_diagonal_2 = 0

                if count_diagonal_2 >= 5:
                    return True

        return False
            

class Player(object):

    def __init__(self, board, stone):

        self.captures = 0
        self.player_stone = stone
        self.board = board

    def __str__(self):

        return("The player has {} captures and is using stone {}".format(self.captures, self.player_stone))

    def take_turn(self, x, y):
        self.board.place_stone(x, y, self.player_stone)
        self.captures += self.board.capture_stones(x, y, self.player_stone)

        if self.captures >= 5 or self.board.five_in_a_row(x, y, self.player_stone):
            self.board.set_winner()

    def reset(self):
        self.captures = 0

        
            
if __name__ == "__main__":

    num_players = 2
    standard_board = Board(19, 19)
    players = []
    turn = 0

    for i in range(num_players):
        players.append(Player(standard_board, str(i)))

    while not standard_board.is_winner():
        player_turn = (turn % num_players)        
        players[player_turn].take_turn()
        turn +=1

    print("")
    print("")
    print("Player{} WINS!!!".format((turn % num_players)+ 1))
    print("")
    print("")
