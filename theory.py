#import roman
# Musical System
BASE_FREQUENCY = 440.0
EQUIVALENCE_RATIO = 2
NUMBER_ATOMIC_UNITS = 12

# SPECIFIC TO WESTERN SYSTEM
scales = {
    'maj': [2, 2, 1, 2, 2, 2, 1],
    'min': [2, 1, 2, 2, 1, 2, 2],
    # TODO define in terms of min
    'harm_min': [2, 1, 2, 2, 1, 3, 1],
    'mel_min': [2, 1, 2, 2, 2, 2, 1]
}

ROMAN_NUMERALS = [
     "I",
     "II",
     "III",
     "IV",
     "V",
     "VI",
     "VII",
     "VIII",
     "IX",
     "X",
     "XI",
     "XII"
]
ROMAN_NUMERALS_V2 = {
        "I": 'maj_tri',
        "II": 'maj_tri',
        "ii": 'min_tri',
        "III": 'maj_tri',
        "IV": 'maj_tri',
        "V": 'maj_tri',
        "VI": 'maj_tri',
        "VII": 'maj_tri',
        "VIII": 'maj_tri',
        "IX": 'maj_tri',
        "X": 'maj_tri',
        "XI": 'maj_tri',
        "XII": 'maj_tri'
}

LETTERS = ["C","D","E","F","G","A","B"]

intervals_to_semitone = {
        ('P1', 'd2'): 0,
        ('m2', 'A1'): 1,
        ('M2', 'd3'): 2,
        ('m3', 'A2'): 3,
        ('M3', 'd4'): 4,
        ('P4', 'A3'): 5,
        ('d5', 'A4'): 6,
        ('P5', 'd6'): 7,
        ('m6', 'A5'): 8,
        ('M6', 'd7'): 9,
        ('m7', 'A6'): 10 ,
        ('M7', 'd8'): 11 ,
        ('P8', 'A7', 'd9'): 12 ,
        ('m9', 'A8'): 13,
        ('M9', 'd10'): 14,
        ('m10', 'A9'): 15,
        ('M10', 'd11'): 16,
        ('P11', 'A10'): 17,
        ('d12', 'A11'): 18,
        ('P12', 'd13'): 19,
        ('m13', 'A12'): 20,
        ('M13', 'd14'): 21
        }

# CHORDS
chords = {
        'maj_tri': (0, 4, 7),
        'min_tri': (0, 3, 7),
        'dom7': (0, 4, 7, 10),
        'maj7': (0, 4, 7, 11),
        'min7': (0, 3, 7, 10), 
        'dim7': (0, 3, 6, 9),
        'half_dim7': (0, 3, 6, 10),
        'dom7flat9':(0, 3, 7, 11),
        'aug_maj7': (0, 4, 8, 10),
        'min7flat5':(0, 3, 6, 10),
        # Because 9 = 14 semitones, flat 9, 13 and 13 % 12 = 1
        'dom7flat9':(0, 4, 7, 10, 1), 
        'dom7sharp9': (0, 4, 7, 10, 3),
        'dom13': (0, 4, 7, 10, 17)
        }
# TODO do away with the one above, there for legacy for now
chord_to_interval = {
        'maj_tri': (0, 4, 7),
        'min_tri': (0, 3, 7),
        'dom7': (0, 4, 7, 10),
        'maj7': (0, 4, 7, 11),
        'min7': (0, 3, 7, 10), 
        'dim7': (0, 3, 6, 9),
        'half_dim7': (0, 3, 6, 10),
        #'dom7flat9':(0, 3, 7, 11),
        'aug_maj7': (0, 4, 8, 10),
        'min7flat5':(0, 3, 6, 10),
        'min7flat9':(0, 3, 7, 10, 13),
        # Because 9 = 14 semitones, flat 9, 13 and 13 % 12 = 1
        'dom7flat9':(0, 4, 7, 10, 13), 
        'dom7sharp9': (0, 4, 7, 10, 15),
        'dom13': (0, 4, 7, 10, 17),
        'dom7flat13':(0, 4, 7, 10,20 ) 
        }
interval_to_chord = {v: k for k, v in chord_to_interval.items()}
# TODO: Convert it to tuples and then get a one to one mapping
letter_to_semitone = {
        'C':0 ,
        'C#':1,
        'Db':1,
        'D':2,
        'D#':3,
        'Eb':3,
        'E':4,
        'F':5,
        'F#':6,
        'Gb':6,
        'G':7,
        'G#':8,
        'Ab':8,
        'A':9,
        'A#':10,
        'Bb':10,
        'B':11
}
semitone_to_letter = {v: k for k, v in letter_to_semitone.items()}
