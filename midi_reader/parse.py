import mido
import pprint
#mid = mido.MidiFile('Chordify_boy-pablo-Everytime_Quantized_at_103_BPM.mid')
mid = mido.MidiFile('Chordify_Her-s-What-Once-Was_Quantized_at_97_BPM.mid')

letters = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

def mid_to_int(mid_num):
    return (mid_num - 72) % 12

def pos_mod(x,m):
    return (x%m + m) % m


song = {"chords": [], "bass": []}
chord = []
for i, track in enumerate(mid.tracks):
    #print('Track {}: {}'.format(i, track.name))
    # just for initial run
    # if i = 1, then we are on chords, if i = 2, then we are on bass
    song_part = "chords" if i == 1 else "bass"
    for msg in track:
        if msg.is_meta:
            print(msg)
            pass
        else:
            if msg.time != 0:
                #print(chord)
                song[song_part].append(chord)
                if msg.type == 'note_on':
                    chord = [mid_to_int(msg.note)]
                else:
                    chord = []
            else:
                if msg.type == 'note_on': 
                    chord.append(mid_to_int(msg.note))
            #print(msg)
            #print(mid_to_int(msg.note))
    #pprint.pprint(song)


chords = song["chords"]
bass = song["bass"]

chord_notation = []

for i in range(1, len(chords)):
    chord = chords[i]
    # Assuming singleton
    root_tone = bass[i][0]
    #print(chord,root_tone)

    intervals = []

    for chord_tone in chord:
        intervals.append(pos_mod(chord_tone - root_tone, 12))
    intervals.sort()

    chord_notation.append( [root_tone, intervals])


def abstract_key_away(key, chord_notation):
    for cn in chord_notation:
        cn[0] = pos_mod(cn[0] - key, 12)

#abstract_key_away(2, chord_notation)
abstract_key_away(8, chord_notation)

pprint.pprint(chord_notation)

