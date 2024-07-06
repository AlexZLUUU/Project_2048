import random
import pygame

def setup_game():
    board=[[0]*4 for _ in range(4)]
    add_number(board)
    add_number(board)
    return board

def add_number(board):
    empty_slot=[(i,j) for i in range(4) for j in range(4) if board[i][j]==0]
    if empty_slot:
        i,j=random.choice(empty_slot)
        board[i][j]=2

def print_board(board):
    for row in board:
        print("+----" * 4 + "+")
        print("".join(f"| {num:4}" if num != 0 else "|    " for num in row) + "|")
    print("+----" * 4 + "+")

def slide_board(board):
    new_board=[[0]*4 for _ in range(4)]
    for i in range(4):
        p=0
        for j in range(4):
            if board[i][j]!=0:
                new_board[i][p]=board[i][j]
                p+=1
    return new_board

def merge_value(board):
    for i in range(4):
        for j in range(3):
            if board[i][j]==board[i][j+1] and board[i][j]!=0:
                board[i][j]=board[i][j]*2
                board[i][j+1]=0
    return board

def reverse(board):
    return [row[::-1] for row in board]

def transpose(board):
    return [[board[j][i] for j in range(4)] for i in range(4)]

def move_up(board):
    new_board=transpose(board)
    new_board=move_left(new_board)
    new_board=transpose(new_board)
    return new_board

def move_down(board):
    new_board=transpose(board)
    new_board=move_right(new_board)
    new_board=transpose(new_board)
    return new_board

def move_left(board):
    new_board=slide_board(board)
    new_board=merge_value(new_board)
    new_board=slide_board(new_board)
    return new_board

def move_right(board):
    new_board=reverse(board)
    new_board=move_left(new_board)
    new_board=reverse(new_board)
    return new_board

def user_input():
    direction = {"w": move_up, "a": move_left, "s": move_down, "d": move_right}
    while True:
        try:
            move = input("Enter move (w/a/s/d): ").strip().lower()
            if move not in direction:
                raise ValueError("Invalid move entered. Please enter one of 'w', 'a', 's', 'd'.")
            return direction[move]
        except ValueError as e:
            print(e)


                
                



    