import pygame

class VirtualInstrument:
    def __init__(self, key_mapping, sound_generator):
        self.key_mapping =  key_mapping
        self.sound_generator = sound_generator
        self.notes_pressed = set()

    def parse_input_to_sound_get_pressed(self):
        keys = pygame.key.get_pressed()
        print(keys)
        for k, v in self.key_mapping.items():
            note = v
            if keys[k]:
                if note not in self.notes_pressed:
                    self.notes_pressed.add(note)
                    self.sound_generator.play_note(note)
            else:
                if note in self.notes_pressed:
                    self.notes_pressed.remove(note)
                    self.sound_generator.stop_playing_note(note)

    def parse_input_to_sound_single_event(self, e):
        if e.type == pygame.KEYDOWN:
            try:
                note = self.key_mapping[e.key]
            except KeyError:
                pass
            else:
                if note not in self.notes_pressed:
                    self.notes_pressed.add(note)
                    self.sound_generator.play_note(note)
        elif e.type == pygame.KEYUP:
            try:
                note = self.key_mapping[e.key]
            except KeyError:
                pass
            else:
                if note in self.notes_pressed:
                    self.notes_pressed.remove(note)
                    self.sound_generator.stop_playing_note(note)


    def parse_input_to_sound_multiple_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                try:
                    note = self.key_mapping[e.key]
                except KeyError:
                    pass
                else:
                    if note not in self.notes_pressed:
                        self.notes_pressed.add(note)
                        self.sound_generator.play_note(note)
            elif e.type == pygame.KEYUP:
                try:
                    note = self.key_mapping[e.key]
                except KeyError:
                    pass
                else:
                    if note in self.notes_pressed:
                        self.notes_pressed.remove(note)
                        self.sound_generator.stop_playing_note(note)

            






