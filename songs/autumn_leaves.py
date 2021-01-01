from create_song import *

intro = [
        ('A5', 'min7', 1), ('D5', 'dom7', 1), ('G5', 'maj7', 1), ('C5', 'maj7', 1),
        ('F#5', 'half_dim7', 1), ('B5', 'dom7', 1), ('E5', 'min6', 2)
]

body = [
        ('F#5', 'half_dim7', 1), ('B5', 'dom7', 1), ('E5', 'min6', 2),
        ('A5', 'min7', 1), ('D5', 'dom7', 1), ('G5', 'maj7', 2),
        ('F#5', 'half_dim7', 1), ('B5', 'dom7', 1), 
        ('E6', 'min7', .5), ('Eb6', 'dom7', .5), ('D6', 'min7', .5), ('Db6', 'dom7', .5), 
        ('C5', 'maj7', 1), ('B5', 'dom7', 1), ('E5', 'min6', 2)
]
changes = intro * 2 + body

create_song("autumn_leaves", 120, changes, 8)
