import os, sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import random
from theory import *

NUM_FRETS = 24
NUM_STRINGS = 6
BASE_EQUIVALENCE_PATTERN = [0, -5, 2, -3, 5, 0]
FRETBOARD = [["-"] * NUM_FRETS for _ in range(6)]


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def print_mat(mat):
    print(' '.join())
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in mat]))

    FRETBOARD = [["-"] * NUM_FRETS for _ in range(6)]

def print_mat_v2(matrix):
    #matrix = [[str(x) for x in range(NUM_FRETS)]] + matrix
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

def equivalent_notes(n, symbol="X"):
    to_be_marked = []
    #Assuming s = 6
    s, f = n
    for i in range(NUM_STRINGS):
        shift = BASE_EQUIVALENCE_PATTERN[i]
        to_be_marked.extend(eqv_string(NUM_STRINGS-1-i, f + shift, symbol))
    return to_be_marked
    
def eqv_string(str_num, start_fret, symbol):
    to_be_marked = []
    # It's possible that start_fret could be invalid, so we have to make it positive (so it exists on the fretboard!)
    while start_fret < 0:
        start_fret += 12
    rem = start_fret % 12
    fret_pos = rem

    while fret_pos <= NUM_FRETS-1:
      to_be_marked.append( (str_num, fret_pos, symbol))
      fret_pos += 12
    return to_be_marked

def mark_fretboard_no_gui(to_be_marked, fb):
    for info in to_be_marked:
        str_num, fret_pos, symbol = info
        fb[str_num][fret_pos] = symbol

def chord_constructor(root, intervals, blank=False):
    to_be_marked = []
    for i in intervals:
        sym = 'X' if blank else str(i)
        to_be_marked.extend(equivalent_notes((5, root + i), sym))
    return to_be_marked

