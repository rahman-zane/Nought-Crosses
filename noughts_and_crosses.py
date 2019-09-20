# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:45:14 2019

@author: Rahman Al-Shabazz
"""

import random

#function to display the updated board as thw game is played
def display_board(board):
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('-----------')
    print(f' {board[1]} | {board[2]} | {board[3]} ')

#give the player a choice of what marker to use
def player_input():
    marker = ''
    p = ()
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        p = ('X', 'O')
        return p
    else:
        p = ('O', 'X')
        return p
 
#place marker in certain position on the board    
def place_marker(board, marker, position):
    board[position] = marker

#check for every combination that would result in a win
def win_check(board, mark):
    return ((board[1:4] == [mark,mark,mark]) or (board[4:7] == [mark,mark,mark]) or (board[7:10] == [mark,mark,mark])
            or (board[1:10:3] == [mark,mark,mark]) or (board[2:10:3] == [mark,mark,mark]) or (board[3:10:3] == [mark,mark,mark])
            or (board[1:10:4] == [mark,mark,mark]) or (board[3:8:2] == [mark,mark,mark]))
    
#decied which player goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#check if a selected space is free on the baord - used before placing a naught or cross
def space_check(board, position):
    return board[position] == ' '  

#check for a full board - used to check for a draw scenario
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True  

#player input position
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) ')) 
    return position

#let the user choose to play again or end the game
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


###START GAME
    
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
