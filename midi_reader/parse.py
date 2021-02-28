import mido
from pprint import pprint
from sys import argv
from prettytable import PrettyTable
import prettytable




"""
INSTRUCTIONS: Download FIXED TEMPO MIDI file from the chordify page

SAMPLE CALL: python3 parse.py Chordify_Her-s-What-Once-Was_Quantized_at_97_BPM.mid 8
"""

letters = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

def mid_to_int(mid_num):
    return (mid_num - 72) % 12

def pos_mod(x,m):
    return (x%m + m) % m

def convert_same_len(lst, row_size):
    for i in range(0, len(lst), row_size):
        yield lst[i: i + row_size]


def matrix_print_diff_size_ele(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    return '\n\n'.join(table)

def matrix_print_simple(matrix):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix])


print(matrix_print_diff_size_ele(list(convert_same_len([x for x in range(100)], 5))))

def construct_song(mid):
    song = {"chords": [], "bass": []}
    chord = []
    duration = 0
    for i, track in enumerate(mid.tracks):
        #print('Track {}: {}'.format(i, track.name))
        # just for initial run
        # if i = 1, then we are on chords, if i = 2, then we are on bass
        song_part = "chords" if i == 1 else "bass"
        for msg in track:
            if msg.is_meta:
                #print(msg)
                pass
            else:
                #print(msg)
                if msg.time != 0:
                    #print(chord)
                    #if chord != []: 
                    duration = msg.time/384
                    song[song_part].append((chord, duration))
                    if msg.type == 'note_on':
                        chord = [mid_to_int(msg.note)]
                    else:
                        chord = []
                else:
                    if msg.type == 'note_on': 
                        chord.append(mid_to_int(msg.note))
                #print(msg)
                #print(mid_to_int(msg.note))
    #pprint(song)
    return song

def convert_to_chord_integer_notation(song):
    chords = song["chords"]
    bass = song["bass"]

    chord_notation = []

    for i in range(1, len(chords)):
        chord = chords[i][0]
        duration = chords[i][1]
        # Assuming singleton
        root_tone = bass[i][0][0]
        #print(root_tone)
        #print(chord,root_tone)

        intervals = []

        for chord_tone in chord:
            intervals.append(pos_mod(chord_tone - root_tone, 12))
        intervals.sort()

        chord_notation.append( [root_tone, intervals, duration])
    return chord_notation


def abstract_key_away(key, chord_notation):
    for cn in chord_notation:
        cn[0] = pos_mod(cn[0] - key, 12)

if __name__ == "__main__":
    mid = mido.MidiFile(argv[1])
    key = int(argv[2])
    s = construct_song(mid)
    cin = convert_to_chord_integer_notation(s)
    abstract_key_away(key, cin)
    cin = list(convert_same_len(cin, 5))

    with open(argv[1][:-4] + '.txt', 'wt') as out:


        p = PrettyTable()
        p.padding_width = 2
        p.border = True
        p.hrules = prettytable.ALL

        for row in cin:
            if len(row) < 5:
                for i in range(5-len(row)):
                    row.append([])
            p.add_row(row)

        print("KEY: ", key, file=out)
        print(p.get_string(header=False), file=out)


        #print(matrix_print_diff_size_ele(cin), file=out)
        #print(matrix_print_simple(cin), file=out)
            #pprint(cin, stream=out)



