import pygame
import sys
import numpy as np

pygame.init()

width = 600
hieght = width
line_width=12
board_rows=3
board_colums=3
circle_rad=60
circle_width=15
cross_width=25
space=55
#الالوان
color= (255, 255, 255)
line_color= (0, 0, 0)
circle = (204,0,0)
cross = (64,64,64)

board_bg = pygame.display.set_mode((width,hieght))
board_bg.fill( color )
pygame.display.set_caption('Tic Tac')


board = np.zeros((board_rows, board_colums))

def draw_lines():
    #الخطوط الي بالعرض
    pygame.draw.line( board_bg, line_color, (0, 200), (600, 200), line_width)
    pygame.draw.line(board_bg, line_color, (0, 400), (600, 400), line_width)
    #الخطوط الي بالطول
    pygame.draw.line( board_bg, line_color, (200, 0), (200, 600), line_width)
    pygame.draw.line( board_bg, line_color, (400, 0), (400, 600), line_width)

def draw_figures():
    for row in range(board_rows):
        for col in range(board_colums):
            if board[row][col]==1:
                pygame.draw.circle(board_bg ,circle, (int( col*200 +100), int(row*200+100)), circle_rad, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(board_bg,cross, ( col * 200 + space , row * 200 + 200 -space ), (col * 200 + 200 - space, row * 200 + space),cross_width)
                pygame.draw.line(board_bg,cross, ( col * 200 + space , row *200 + space ), (col * 200 + 200 - space, row * 200 + 200 - space),cross_width)

#المربعات
def mark_square(row, col, player):
    board[row][col] = player
#متاح ولا لا     

def available_square(row,col):
    if board[row][col]== 0:
        return True
    else:
        return False


#
def is_board_full():
    for row in range(board_rows):
        for col in range(board_colums):
            if board[row][col] ==0:
                return False
    return True 

def check_win(player):
    #vertical
    for col in range(board_colums):
        if board[0][col] == player and board[1][col] == player and board[2][col] ==player:
            draw_vertical_winning_line(col,player)
            
            return True
        
    #horizntal
    for row in range(board_rows):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_winning_line(row,player)
            return True

    #asc diagonal
    if board[2][0] == player and board[1][1] == player and board[0][2]==player:
        draw_asc_diagonal(player)
        return True
    #desc diagonal
    if board[0][0]== player and board[1][1] == player and board[2][2] ==player:
        draw_desc_diagonal(player)
        return True
    return False

def draw_vertical_winning_line(col,player):
    posx = col * 200 + 100

    if player ==1:
        color=circle
    elif player==2:
        color=cross
    pygame.draw.line(board_bg,color ,(posx,15),(posx, hieght-15 ),15)
def draw_horizontal_winning_line(row,player):
    posy = row *200 + 100
    if player ==1:
        color=circle
    elif player ==2:
        color=cross
    pygame.draw.line(board_bg, color,(15,posy), (width -15, posy), 15)

#الخط المايل
def draw_asc_diagonal(player):
    if player ==1:
        color=circle
    elif player ==2:
        color=cross
    pygame.draw.line(board_bg, color, (15,hieght-15), (width-15,15), 15)

def draw_desc_diagonal(player):
    if player ==1:
        color=circle
    elif player ==2:
        color=cross
    pygame.draw.line(board_bg,color,(15,15),(width-15,hieght-15),15)



draw_lines()
player = 1
game_over= False

#pygame main loop
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        if event.type ==pygame.MOUSEBUTTONDOWN and not game_over:
            mousex = event.pos[0]
            mousey = event.pos[1]

            clicked_row = int(mousey // 200)
            clicked_col = int(mousex // 200)
            
        
            if available_square(clicked_row, clicked_col):
                if player ==1 :
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over=True
                        
                    player = 2
                elif player ==2:
                    mark_square(clicked_row,clicked_col, 2)
                    if check_win(player):
                        game_over=True
                    player = 1
                draw_figures()
        
                    


        
    pygame.display.update()