"""
[Module] Tic-tac-toe bot utilities.
"""
from random import randint
from re import X
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
    return board[player_id]== " "

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
    if player_2 == 'X': 
        if board [4]== " ":
            return 4
        esquinas_vacias= []
        for i in [0,2,6,8]:
            if casilla_libre(board, i):
                esquinas_vacias.append(i)
        demas_vacias = []
        for i in [1,3,5,7]:
            if casilla_libre(board, i):
                demas_vacias.append(i)
        if len(esquinas_vacias) > 0:
            return randint.choice (esquinas_vacias)
        else: 
            return randint.choice(demas_vacias)

    if player_2 == "O":
        contador = 0 
        for i in range (9):
            if casilla_libre (board, i):
                contador +=1
        if contador == 7: 
            if board[4] == " ":
                return 4 

    while True: 
        casilla = randint(0,8)
        if not casilla_libre (board, player_id):
            casilla = randint (0,8)
        else:
            return casilla


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
