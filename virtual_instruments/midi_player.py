import pygame.midi as midi
import time

class MidiPlayer:
    def __init__(self):
        midi.init()
        # Used to find the one for timidity
        print(midi.get_device_info(0))
        print(midi.get_device_info(1))
        print(midi.get_device_info(2))
        port = midi.get_default_output_id()
        port = 2
        self.out = midi.Output(port, 0)
        self.instrument = 0
        self.out.set_instrument(self.instrument)

    def convert_note_to_midi(self, note, oct_band = 0):
        if oct_band != 0:
            return 12 * oct_band + note
        else:
            return note + 48


    def play_note(self,note,oct_band=False):
        # Convert notes into midi format, Using full velocity
        print(note)
        if oct_band:
            self.out.note_on(self.convert_note_to_midi(note[1], note[0]), 127)
        else:
            self.out.note_on(self.convert_note_to_midi(note), 127)

    def stop_playing_note(self,note, oct_band=False):
        print(note)
        if oct_band:
            self.out.note_off(self.convert_note_to_midi(note[1], note[0]), 0)
        else:
            self.out.note_off(self.convert_note_to_midi(note), 0)


    def play_notes(self,notes):
        # Convert notes into midi format
        for note in notes:
            # Using full velocity
            self.out.note_on(self.convert_note_to_midi(note), 127)
