import pygame as pg

import os,sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from theory_utils import *

class VirtualChordInstrument:
    def __init__(self, sound_generator, human_interface):
        self.sound_generator = sound_generator
        self.notes_pressed = set()
        self.human_interface = human_interface

    def parse_input_to_sound(self):
        keys = pg.key.get_pressed()

        notes = self.human_interface.parse_input_to_notes()

        if keys[pg.K_RETURN]:
            for note in notes:
                if note not in self.notes_pressed:
                    self.notes_pressed.add(note)
                    self.sound_generator.play_note(note)
                else:
                    # We don't repeat the note
                    pass
        else:
            for note in notes:
                if note in self.notes_pressed:
                    self.notes_pressed.remove(note)
                    self.sound_generator.stop_playing_note(note)
                else:
                    # We've already removed the note
                    pass

class ChordInputBox(pg.sprite.Sprite):
    # This class gives input to the Virtual Chord Instrument
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = (255, 255, 255)
        self.backcolor = None
        self.pos = (x, y) 
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()

    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pg.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pg.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pg.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.pos)

    def parse_input_to_notes(self):
        # Put this in a try except block
        data = self.text.split()
        print(data)
        try:
            root_tone, intervals = data[0], data[1:]

            root_tone = int(root_tone)
            intervals = [int(x) for x in intervals]

            notes = root_and_intervals_to_int_basic(root_tone, intervals, 2)
        except: 
            notes = []

        return notes


    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pg.KEYDOWN and self.active:
                if event.key == pg.K_ESCAPE:
                    self.active = False
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pg.K_RETURN:
                    pass
                else:
                    self.text += event.unicode
                self.render_text()

