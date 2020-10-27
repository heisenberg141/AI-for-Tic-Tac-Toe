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
    emptyPos=0
    for row in board:           
        for position in row:
            if position == EMPTY:
                emptyPos+=1
    if emptyPos==0:
        return None

    if emptyPos%2==0:
        return O
    else :
        return X        
    
def actions(board):    
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleMoves=set()
    for i,row in enumerate(board):
        for j,position in enumerate(row):
            if position==EMPTY:         
                possibleMoves.add((i,j))

    if len(possibleMoves)==0:
        return None
    return possibleMoves
    
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    actionSet=action
    i=actionSet[0]
    j=actionSet[1]
    UpdatedBoard=copy.deepcopy(board)
    
    if player(board)!=None:
        if UpdatedBoard[i][j]==EMPTY:
            UpdatedBoard[i][j]=player(board)
            return UpdatedBoard
        else:
            raise Exception("INVALID MOVE! Please play on an empty space.")
    else:
        return None
        
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # diag
    if(board[0][0]!=None and board[0][0]==board[1][1] and board[0][0]==board[2][2]):
        return board[0][0]
    elif board[0][2]!=None and board[0][2]==board[1][1] and board[0][2]==board[2][0]:
        return board[0][2]
    #hoz
    else:
        for i in range(3):
            if board[i][0]!=None and board[i][0]==board[i][1] and board[i][0]==board[i][2]:
                
                return board[i][0]
    #vert
        for j in range(3):
            if board[0][j]!=None and board[0][j]==board[1][j] and board[0][j]==board[2][j]:
                return board[0][j]
        return(None)
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    IsWon=winner(board)
    if(IsWon!=None or player(board)==None):
        return True
    else:
        return False
   
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0

# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     Maximizer=X
#     Minimizer=O
#     boardCPY=copy.deepcopy(board) 
#     if player(board)==Maximizer:
#         val,bestMove=maxval(board)
#     else:
#         val,bestMove=minval(board)
    
#     return bestMove
  
# def maxval(board):
#     bestMove=()   
#     if terminal(board):
#         return utility(board),bestMove
#     v=-10
#     for action in actions(board):
#         BestVal,Move=minval(result(board,action))
#         if v<BestVal:
#             v=BestVal
#             bestMove=action
#     return v,bestMove

# def minval(board):
#     bestMove=() 
#     if terminal(board):
#         return utility(board), bestMove
#     v=10
#     for action in actions(board):
#         BestVal,Move=maxval(result(board,action))
#         if v>BestVal:
#             v=BestVal
#             bestMove=action
#     return v,bestMove






   

def max_value_alpha_beta(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    v = float("-inf")
    best = None
    for action in actions(board):
        min_v = min_value_alpha_beta(result(board, action), alpha, beta)[0]
        if min_v > v:
            v = min_v
            best = action
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v, best

def min_value_alpha_beta(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    v = float("inf")
    best = None
    for action in actions(board):
        max_v = max_value_alpha_beta(result(board, action), alpha, beta)[0]
        if max_v < v:
            v = max_v
            best = action
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v, best

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        return max_value_alpha_beta(board, float("-inf"), float("inf"))[1]
    elif player(board) == O:
        return min_value_alpha_beta(board, float("-inf"), float("inf"))[1]
    else:
        raise Exception("bug in minimax algorithm")