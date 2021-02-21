import os,sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from midiutil import MIDIFile
from theory_utils import *
from sound_utils import *

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

def create_midi_song(title, BPM, song):
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

    # add beat
    MyMIDI.addProgramChange(track, 10, 0, 10)
    for i in range(current_beat):
        MyMIDI.addNote(track, 9, 51, i, 1, volume)
        if i % 2 == 0:
            MyMIDI.addNote(track, 9, 35, i, 1, volume)
        else:
            MyMIDI.addNote(track, 9, 38, i, 1, volume)



    with open(title, "wb") as output_file:
        MyMIDI.writeFile(output_file)
