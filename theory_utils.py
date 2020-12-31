from theory import *
import math
# === CONVERT TO AND FROM SCIENTIFIC NOTATION TO FREQUENCY ===  

def sci_to_freq(sci_not):
    if len(sci_not) == 3:
        note = sci_not[0:2]
        octave = int(sci_not[2])
    else:
        note = sci_not[0]
        octave = int(sci_not[1])

    return 440 * (2 ** (octave -5 )) * (2 ** ((letter_to_semitone[note] - 9)/12.0))


def freq_to_sci(freq):
    # The fundemental observation is that any frequency is of the following form
    #           440 * 2 ** (x + y/12)  x in Z, and 0 <= y < 12
    # Think quotient remainder where the integers are the start points of each octave
    # x is the oct_range and y is the semi_count

    exp = math.log(freq/440.0, 2) 
    oct_range = math.floor(exp)
    # modulo one gives the decimal part of the number
    semi_count = round((exp % 1) * 12)
    # Since it's relative to A5, which is in the 5th octave range
    shifted_oct_range = oct_range+5
    letter = semitone_to_letter[semi_count]
    return letter + str(shifted_oct_range)

def generate_scale_frequencies(root_freq, scale_pattern):
    intervals = [0]

    semitones_from_root = 0
    scale = []

    # Add zero for the first note
    for skip in [0] + scale_pattern:
        semitones_from_root += skip
        interval = semitones_from_root
        scale.append(root_freq * (2 ** (interval/12)))

    return scale

print(freq_to_sci(220 * (2 ** (3/12.0))))
