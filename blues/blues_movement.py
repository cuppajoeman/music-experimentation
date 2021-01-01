def print_mat_v2(matrix):
    #matrix = [[str(x) for x in range(NUM_FRETS)]] + matrix
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

def rotate(l, n): 
    pos = len(l) - n
    return l[pos:] + l[:pos]

chord_table = []

seventh = [0, 4, 7, 10]


chord_table.append(['intervals'] + [x % 12 for x in range(12 * 4)])

#In terms of semitones
#   I -> 0 IV -> 5 V -> 7
for s,r in [(0, 'I'), (5, 'IV'), (7, 'V')]:
    x = rotate([(x) % 12 if (x % 12) in seventh else " " for x in range(12 * 4)], s)
    chord_table.append([r] + x)


print_mat_v2(chord_table)





