"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    available_moves = []
    
    if not terminal(board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    available_moves.append((i,j))
        return available_moves
    
    return []
                
    
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    for row in board:
        if action in row:
            raise Exception("Cell is already taken!")
    
    
    if(action[0] > 2 or action[0] < 0 or action[1] > 2 or action[0] < 0):
        raise Exception("Action is out of bounds!")
    
    new_board = copy.deepcopy(board)

    if action is not None:
        new_board[action[0]][action[1]] = player(board)
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """ 
    players = (X, O)
    
    for player in players:
        for row in board:
            if all(cell == player for cell in row):
                return player
            
        for col in range(3):
            if all(row[col] == player for row in board):
                return player
        
        if all(board[i][i] == player for i in range(3)):
            return player
        
        if all(board[i][2-i] == player for i in range(3)):
            return player
    
    return None
    
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is not None:
        return True
    
    if all(cell != EMPTY for row in board for cell in row):
        return True
    
    return False
        


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0
    



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None
    
    def max_value(board):
        v = -float('inf')
        
        if terminal(board):
            return utility(board)
        
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v    
        
    def min_value(board):
        v = float('inf')
        
        if terminal(board):
            return utility(board)
        
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v
    
    # Determine optimal action for player
    
    current_player = player(board)
    best_action = None
    
    if current_player == X:
        
        best_value = -float('inf')
        
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
    
    else:
        
        best_value = float('inf')
        
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
    
    return best_action
    
    