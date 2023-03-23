### Execute this file to create the dataset. You can select the size it will have.
# Author: Tomas E. Schattmann

import chess
import chess.engine
import random
import numpy
import time

# Generates a random chess.Board() 
def random_board(max_depth=200):
  board = chess.Board()
  depth = random.randrange(0, max_depth)

  for _ in range(depth):
    all_moves = list(board.legal_moves)
    random_move = random.choice(all_moves)
    board.push(random_move)
    if board.is_game_over():
      break

  return board


# this function will parse our random board through stockfish and creates another board
def stockfish(board, time):  
  with chess.engine.SimpleEngine.popen_uci('Stockfish/src/stockfish') as sf:
    result = sf.play(board, chess.engine.Limit(time=0.05))
    board.push(result.move)
    print('BEST MOVE PLAYABLE -> ' + str(result.move))
    print('FEN BOARD NOTATION -> ' + str(board.fen()))
    return str(result.move), str(board.fen()) 
  


def __init__(): 
  print('Working on it...')
  inicio = time.time()
  stockfish(random_board(), 0.3)
  fin = time.time()
  print('TIEMPO DE EJECUCION --> ', str(fin-inicio))
  print('TIEMPO DE EJECUCION DATASET COMPLETO (2MILLONES)--> ', str(((((fin-inicio)*2000000)/60)/60)/24), ' DIAS')
  return 0


if __name__ ==  "__main__":
  __init__()