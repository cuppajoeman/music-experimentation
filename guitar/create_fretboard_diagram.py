import os,sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from fretboard_position_generator import *
from fretboard_figure_generator import *
from fretboard_txt_generator import *

# PATTERNS

# Expand outward from the fingertips


PATTERNS = {
    "EQUIVALENCE": (
                               0,
                   ),
    "NEARBY_INTERVALS": (
                            4,5,6,
                            11,0,1,
                            6,7,8
                        ),
    "MISSING_INTERVALS": (
                            3,     
                            10, 0  ,2,
                                    9
                        ),
    "FURTHER_INTERVALS": (
                                    3,4,5,6,7,
                                    10,11,0,1,2,
                                    8,9
                            ),
    "LINE_Y_EQUALS_X": (0, 6 ),
    "LINE_Y_EQUALS_MINUS_X": (0, 4, 8 ),
    # Because gcd(7, 12) = 1
    "LINE_Y_EQUALS_2X": (0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5 ),
    "LINE_Y_EQUALS_MINUS_2X": ( 0,3,6,9 ),
    "LINE_Y_EQUALS_3X": (0, 8, 4 ),
    "LINE_Y_EQUALS_MINUS_3X": (0,2,4,6,8,10),
    "scale by hand": (0, 2, 4, 5, 7, 9, 11),
    "scale even": (0,  4,  7, 11),
    "scale odd": ( 0, 2,  5,  9 )
    }

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

#for s,c in chord_to_interval.items():
#    r_pos = random.randint(0, 12)
#    print(s)
#    tbm = chord_constructor(r_pos, c, False)
#    mark_fretboard_no_gui(tbm, FRETBOARD)
#    print_mat_v2(FRETBOARD)
#    FRETBOARD = [["-"] * NUM_FRETS for _ in range(6)]
#

blues = [("A", "dom7"), ("D", "dom7"), ("E", "dom7")]
create_fret_representation("blues",blues, True)

for s, c in PATTERNS.items():
    #r_pos = random.randint(0, 12)
    r_pos = 8
    create_fret_representation(s, [(r_pos, c)], True)

for s in chord_to_interval:
    #r_pos = random.randint(0, 12)
    r_pos = 8
    create_fret_representation(s, [(r_pos, s)], True)
    
for s,i in scales.items():
    r_pos = 8
    ps = 0
    pat = []
    for x in i:
        pat.append(ps)
        ps += x
    create_fret_representation(s, [(r_pos, tuple(pat))], True)



