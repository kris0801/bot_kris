"""
[Module] Tic-tac-toe bot utilities.
"""
from random import randint
from re import X
from sqlite3 import Row
from tkinter.tix import COLUMN
import requests
from urllib.parse import unquote


API_URL = "http://127.0.0.1:8000"


def is_registry_open() -> bool:
    """
    Checks if registry is available via API.
    """
    try:
        url = "{}/registry".format(API_URL)
        res = requests.get(url)

        if res.text == "true":
            return True
        elif res.text == "false":
            return False

    except:
        return False


def register_user(name: str) -> str:
    """
    Registers user in API game.
    """
    url = "{}/register_player/{}".format(API_URL, name)
    res = requests.post(url)
    player_id = res.text[1]
    return player_id


def is_my_turn(player_id: str) -> bool: 
    """
    Checks if it is our turn via API.
    """
    url = "{}/turn/{}".format(API_URL, player_id)
    res = requests.get(url)
    
    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def read_board() -> list:
    """
    Gets game board via API.
    """
    url = "{}/board".format(API_URL)
    res = requests.get(url)
    board_str = res.text
    board = [
        [board_str[1], board_str[2], board_str[3]], 
        [board_str[4], board_str[5], board_str[6]], 
        [board_str[7], board_str[8], board_str[9]]
    ]

    return board

def casilla_libre(board, player_id):
    return board[player_id]== "-"

def decide_move(board: list, player_id: str) -> list:    
    """
    Decides next move to make.
    """
    
    player_2= None 
    if player_id == 'X':
        player_2 = 'O'
    else:
        player_2='X'
    # cuando lo toque X
    
    if player_id == 'X': 
        if board[1][1]== "-":
            return [1,1]

        esquinas_vacias == "-"
        if board[0][0]== "-":
            return [0,0] 
        elif board[0][2]== "-":
            return [0,2] 

        elif board[2][0]== "-":
            return [2,0] 
        elif board[2][2]== "-":
            return [2,2]
             
        demas_vacias == "-"
        if board[0][1]== "-":
            return [0,1] 
        elif board[1][0]== "-":
            return [1,0] 

        elif board[1][1]== "-":
            return [1,1] 
        elif board[1][2]== "-":
            return [1,2]
        elif board[2][1]== "-":
            return [2,1]
    

    if player_id == "O":
        if board[1][1]== "-":
            return [1,1]

        esquinas_vacias= "-"
        if board[0][0]== "-":
            return [0,0] 
        elif board[0][2]== "-":
            return [0,2] 
        elif board[2][0]== "-":
            return [2,0] 
        elif board[2][2]== "-":
            return [2,2]

        demas_vacias = "-"
        if board[0][1]== "-":
            return [0,1] 
        elif board[1][0]== "-":
            return [1,0] 

        elif board[1][1]== "-":
            return [1,1] 
        elif board[1][2]== "-":
            return [1,2]
        elif board[2][1]== "-":
            return [2,1]
    
        
def validate_move(board: list, move: list) -> bool:
    """
    Checks if the desired next move hits an empty position.
    """
    row, col = move[0], move[1]

    if board[row][col] == "-":
        return True

    return False


def send_move(player_id: str, move: list) -> None:
    """
    Sends move to API.
    """
    row, col = move[0], move[1]
    url = "{}/move/{}/{}/{}".format(API_URL, player_id, row, col)
    res = requests.post(url)
    return None


def does_game_continue() -> bool:
    """
    Checks if the current match continues via API.
    """
    url = "{}/continue".format(API_URL)
    res = requests.get(url)

    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def print_board(board: list) -> None:
    '''
    Prints the baord in console to watch the game.
    '''
    print("\nCurrent board: \n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2], "\n")
