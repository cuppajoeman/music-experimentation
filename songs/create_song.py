import os,sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from midiutil import MIDIFile
from theory_utils import *
from sound_utils import *

midi_inst_to_name_perc = {
35: "Acoustic Bass Drum",
36: "Electric Bass Drum",
37: "Side Stick",
38: "Acoustic Snare",
39: "Hand Clap",
40: "Electric Snare",
41: "Low Floor Tom",
42: "Closed Hi-hat",
43: "High Floor Tom",
44: "Pedal Hi-hat",
45: "Low Tom",
46: "Open Hi-hat",
47: "Low-Mid Tom",
48: "Hi-Mid Tom",
49: "Crash Cymbal 1",
50: "High Tom",
51: "Ride Cymbal 1",
52: "Chinese Cymbal",
53: "Ride Bell",
54: "Tambourine",
55: "Splash Cymbal",
56: "Cowbell",
57: "Crash Cymbal 2",
58: "Vibra Slap",
59: "Ride Cymbal 2",
60: "High Bongo",
61: "Low Bongo",
62: "Mute High Conga",
63: "Open High Conga",
64: "Low Conga",
65: "High Timbale",
66: "Low Timbale",
67: "High Agogô",
68: "Low Agogô",
69: "Cabasa",
70: "Maracas",
71: "Short Whistle",
72: "Long Whistle",
73: "Short Guiro",
74: "Long Guiro",
75: "Claves",
76: "High Woodblock",
77: "Low Woodblock",
78: "Mute Cuica",
79: "Open Cuica",
80: "Mute Triangle"
}

name_perc_to_midi_inst =  {v: k for k, v in midi_inst_to_name_perc.items()}

class SongEvent:
    # Represents a moment of sound in a song (the start of notes ringing)
    # The time it should be sounded at is implied by the duration of events before it
    def __init__(self, notes, duration):
        self.notes = notes
        self.duration = duration


def create_song(title, BPM, chord_changes, times=1):
    all_waves = np.array([])
    final = np.array([])

    BPS = BPM/60.0
    SPB = 1/BPS
    SPMEA = 4 * SPB

    for chord_change in chord_changes:
        root_freq = sci_to_freq(chord_change[0])
        chord_type = chord_change[1]
        duration = chord_change[2]
        chord_movement = chord_generator(root_freq, chord_to_interval[chord_type], duration * SPMEA)
        all_waves = np.append(all_waves, chord_movement)

    final = np.tile(all_waves, times)

    # Write the samples to a file
    wavio.write('generated_songs/' + title + ".wav", final, RATE, sampwidth=3)

def parse_song_into_notes(song):
    new_song = []
    for event in song:
        root_octave_band, root_number, intervals, beats = event[0][0], event[0][1], event[1], event[2]    
        notes = root_and_intervals_to_int(root_octave_band, root_number, intervals)
        new_song.append( (notes, beats))
    return new_song

def parse_note_song_into_objects(song):
    new_song = []
    for event in song:
        se = SongEvent(event[0], event[1]) 
        new_song.append(se)
    return new_song

def parse_drum_beat_into_objects(drum_part):
    new_song = []
    for event in drum_part:
        converted = [name_perc_to_midi_inst[x] for x in event[0]]
        se = SongEvent(converted, event[1]) 
        new_song.append(se)
    return new_song


def create_midi_song(title, BPM, song, beat = {}):
    track    = 0
    channel  = 0
    time     = 0    # In beats
    duration = 1    # In beats
    tempo    = 60   # In BPM
    tempo    = BPM   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                          # automatically)
    MyMIDI.addTempo(track, time, tempo)

    current_beat = 0
    for se in song:
        # looks like (int_not, {0,4,7,11}, 4)
        for note in se.notes:
            # Have some counter so that we know when to play the beat
            # Means you have to be explicit about your rests
            pitch = int_to_midi(note.octave_band, note.number)
            print(track, channel, pitch, current_beat, se.duration, volume)
            MyMIDI.addNote(track, channel, pitch, current_beat, se.duration, volume)
        current_beat += se.duration


    current_beat = 0
    for k, v in beat.items():
        moment_occured = k
        events = v
        for e in events:
            midi_instrument = name_perc_to_midi_inst[e[0]]
            print(track, 9, midi_instrument, moment_occured, e[1], volume)
            MyMIDI.addNote(track, 9, midi_instrument, moment_occured, e[1], e[2])


    with open(title, "wb") as output_file:
        MyMIDI.writeFile(output_file)
