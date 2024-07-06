from game import *


def main():
    board=setup_game()
    print_board(board)
    while True:
        user_move=user_input()
        new_board=user_move(board)
        if new_board != board:
            add_number(new_board)
            board=new_board
            print_board(board)
            for m in board:
                if 2048 in m:
                    print("Congratulation!")
                    break
        else:
            if any(0 in row for row in board):
                continue
            else:
                print("Game Over")
                break
    
if __name__=="__main__":
    while True:
        main()
        flag=input("Start new game y/n:")
        if flag.lower()!="y":
            break
    print("Game session end.")