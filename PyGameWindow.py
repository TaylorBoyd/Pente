import pygame, sys, time
from pygame.locals import *
from PenteMainCode import *

black = (0, 0, 0)
white = (128, 128, 128)
green = (0, 176, 0)
red = (176, 0, 0)

width = 20
height = 20
margin = 5

num_players = 2
standard_board = Board(19, 19)
players = []
turn = 0
winner = "None"

for i in range(num_players):
        players.append(Player(standard_board, str(i)))

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Calibri', 30)

screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption("Pente")
finished = False
clock = pygame.time.Clock()

while not finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN and winner == "None":
            player_turn = (turn % num_players)
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            if row <= 18 and column <= 18 and not standard_board.is_stone_at_position(column, row) and winner == "None":
                players[player_turn].take_turn(column, row)
                if standard_board.is_winner():
                        winner = ("Player {}".format((turn % num_players + 1)))
                turn +=1
                
        elif event.type == pygame.MOUSEBUTTONDOWN and winner != "None":
            end_pos = pygame.mouse.get_pos()
            
            if (120 <= end_pos[0] <= 180) and (200 <= end_pos[1] <= 220):
                winner = "None"
                turn = 0
                standard_board.clear_board()
                for p in players:
                    p.reset()
                    
            if (360 <= end_pos[0] <= 420) and (200 <= end_pos[1] <= 220):
                pygame.quit()

    screen.fill(black)

    if winner == "None":
        
        for row in range(19):
            for column in range(19):
                if standard_board.spaces[(column, row)] == "+":
                    color = white
                elif standard_board.spaces[(column, row)] == "0":
                    color = red
                elif standard_board.spaces[(column, row)] == "1":
                    color = green
                        
                pygame.draw.rect(screen,
                                 color,
                                 [(margin + width)*column+ margin,
                                  (margin + height) * row + margin,
                                  width,
                                  height])

    else:
        textsurface1 = myfont.render((winner +" WINS!!!"), False, (255, 255, 255))
        textsurface2 = myfont.render(("Play Again"), False, (255, 255, 255))
        textsurface3 = myfont.render(("Quit"), False, (255, 255, 255))
        screen.blit(textsurface1, (200, 10))
        screen.blit(textsurface2, (120, 200))
        screen.blit(textsurface3, (360, 200))
        
        
    clock.tick(60)
    pygame.display.flip()
    


pygame.quit()
