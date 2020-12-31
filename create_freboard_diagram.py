from chord_generation import *

# PATTERNS

# Expand outward from the fingertips

# GEOMETRIC

EQUIVALENCE = [0]

NEARBY_INTERVALS = [
    4,5,6,
    11,0,1,
    6,7,8
]

MISSING_INTERVALS = [
    3,     
    10, 0  ,2,
            9
]

FURTHER_INTERVALS = [
    3,4,5,6,7,
    10,11,0,1,2,
    8,9
]

# LINES

LINE_Y_EQUALS_X = [0, 6]
LINE_Y_EQUALS_MINUS_X = [0, 4, 8]
# Because gcd(7, 12) = 1
LINE_Y_EQUALS_2X = [0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5]
LINE_Y_EQUALS_MINUS_2X = [0,3,6,9]

LINE_Y_EQUALS_3X = [0, 8, 4]
LINE_Y_EQUALS_MINUS_3X = [0,2,4,6,8,10]

PATTERNS = [
    EQUIVALENCE,
    NEARBY_INTERVALS,
    MISSING_INTERVALS,
    FURTHER_INTERVALS,
    LINE_Y_EQUALS_X,
    LINE_Y_EQUALS_MINUS_X,
    LINE_Y_EQUALS_2X,
    LINE_Y_EQUALS_MINUS_2X,
    LINE_Y_EQUALS_3X,
    LINE_Y_EQUALS_MINUS_3X,
    ]

# Linear interval demonstration
#from_six_pattern_across_strings = ''
#mod_from_six_pattern_across_strings = ''
#from_one_pattern_across_strings = ''
#mod_from_one_pattern_across_strings = ''
#string_intervals_six_to_one = [0,5, 5, 5, 4, 5]
#string_intervals_one_to_six = [7, 7, 7, 8, 7, 0]
#
#sum_down = 0
#sum_up = 0
#for i in range(6):
#    sum_down += string_intervals_six_to_one[i]
#    sum_up -= string_intervals_one_to_six[5-i]
#    from_six_pattern_across_strings += (" " if i != 0 else '') + str(sum_down)
#    from_one_pattern_across_strings =  str(sum_up) + " " + from_one_pattern_across_strings
#    mod_from_six_pattern_across_strings += (" " if i != 0 else '') + str(sum_down % 12)
#    mod_from_one_pattern_across_strings =  str(sum_up %12 - 12) + " " + mod_from_one_pattern_across_strings
#
#print("Patterns moving across strings, up and down in terms of semitones")
#print(from_six_pattern_across_strings,from_one_pattern_across_strings, sep='\n')
#print("Modulo 12")
#print(mod_from_six_pattern_across_strings,mod_from_one_pattern_across_strings, sep='\n')
#
##r_pos = random.randint(0, 12)
##equivalent_notes((5,r_pos), 'X')
##print_mat_v2(FRETBOARD)
##FRETBOARD = [["-"] * NUM_FRETS for _ in range(6)]
#
#
## settings for which ones will be blanks
#opts = [False for _ in PATTERNS]
#opts[0] = True
##opts[1] = True
#
## SHOW GEOMETRIC PATTERNS
#count = 0
#for c in PATTERNS:
#    # Randomize so player doesn't get unshifted pattern
#    title = namestr(c, globals())[0]
#    print(title)
#    if "INTERVAL" not in title:
#        r_pos = random.randint(0, 12)
#    chord_constructor(r_pos, c, opts[count])
#    print_mat_v2(FRETBOARD)
#    FRETBOARD = [["-"] * NUM_FRETS for _ in range(6)]
#    count += 1
#
# SHOW CHORDS

for s,c in chords.items():
    r_pos = random.randint(0, 12)
    print(s)
    tbm = chord_constructor(r_pos, c, False)
    mark_fretboard_no_gui(tbm, FRETBOARD)
    print_mat_v2(FRETBOARD)
    FRETBOARD = [["-"] * NUM_FRETS for _ in range(6)]

