import pygame as pg
from math import floor
import time
import os,sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from theory_utils import *


# Helper functions
def invert_color(rgb_color):
    return (255 - rgb_color[0], 255 - rgb_color[1], 255 - rgb_color[2])

def pos_mod(x,m):
    return (x%m + m)%m;

def draw_text_in_block(screen, x,y, x_block_size, y_block_size, text,block_color, y_offset = 0):

    block = pg.Rect((x_block_size * x, y_block_size * y + y_offset), (x_block_size, y_block_size + y_offset))
    pg.draw.rect(screen, block_color, block)

    center_of_block = (x_block_size * x + x_block_size/2, y_block_size * y + y_offset + y_block_size/2)

    fitted_size = floor(min(x_block_size, y_block_size))

    font = pg.font.Font(None, fitted_size)
    text = font.render(text, True, invert_color(block_color))
    text_rect = text.get_rect(center=center_of_block)
    screen.blit(text, text_rect)


# 0 to 35 is for 3 octaves
# extra row for duration
# extra row for input box
NUM_ROWS = 36 + 2

class VirtualChordInstrument:
    def __init__(self, sound_generator, font, screen, w, h):
        self.sound_generator = sound_generator
        self.notes_pressed = set()
        self.song = []
        self.tab_already_pressed = False
        self.screen = screen
        self.w = w
        self.h = h
        self.font = font
        self.colors = {
            0: pg.color.THECOLORS['blue'],
            1: pg.color.THECOLORS['orangered4'],
            2: pg.color.THECOLORS['aquamarine'],
            3: pg.color.THECOLORS['orange'],
            4: pg.color.THECOLORS['red4'],
            5: pg.color.THECOLORS['seagreen'],
            6: pg.color.THECOLORS['chartreuse'],
            7: pg.color.THECOLORS['green'],
            8: pg.color.THECOLORS['cornsilk'],
            9: pg.color.THECOLORS['darkgoldenrod2'],
            10: pg.color.THECOLORS['orchid4'],
            11: pg.color.THECOLORS['red']
        }
        dist_so_far = 0
        self.human_interface = ChordInputBox(0,0,0.25 * self.w,font)
        dist_so_far += 0.25 * self.w

        button_dimensions = self.human_interface.rect.h 
        self.PBB = PlayBackButton(dist_so_far, 0, button_dimensions, button_dimensions , pg.color.THECOLORS['green'], self)
        dist_so_far += button_dimensions

        self.DB = DeleteButton(dist_so_far, 0, button_dimensions, button_dimensions , pg.color.THECOLORS['red'], self)
        dist_so_far += button_dimensions

        self.slice_player_input = PlaybackInputBox(dist_so_far,0,0.25 * self.w ,font, "Slice Player")
        dist_so_far += 0.25 * self.w

        self.SB = PlayBackButton(dist_so_far, 0, button_dimensions, button_dimensions , pg.color.THECOLORS['yellow'], self, self.slice_player_input )
        

    def playback_song(self, start=-1, end =-1):
        if start != -1 and end != -1:
            section = self.song[start:end]
        else:
            section = self.song

        for data in section:
            oct_band, root_tone, intervals, duration = data[0][0], data[0][1], data[1], data[2] 
            notes = root_and_intervals_to_int_no_obj(oct_band, root_tone, intervals)
            # play the chord
            for note in notes:
                self.sound_generator.play_note(note, True)

            time.sleep(duration)

            # silence the notes
            for note in notes:
                self.sound_generator.stop_playing_note(note, True)


    def record_chord(self):
        keys = pg.key.get_pressed()

        chord_data = self.human_interface.parse_input_to_oct_root_and_intervals()

        if keys[pg.K_TAB]:
            if not self.tab_already_pressed:
                self.tab_already_pressed = True
                self.song.append(chord_data)
            else:
                pass
        else:
            self.tab_already_pressed = False

        if len(self.song) > 0:
            self.draw_song(self.screen)

    def remove_chord(self):
        self.song = self.song[:-1]

    def parse_input_to_sound(self):
        keys = pg.key.get_pressed()

        notes = self.human_interface.parse_input_to_notes()

        if keys[pg.K_RETURN]:
            for note in notes:
                if note not in self.notes_pressed:
                    self.notes_pressed.add(note)
                    self.sound_generator.play_note(note, True)
                else:
                    # We don't repeat the note
                    pass
        else:
            for note in notes:
                if note in self.notes_pressed:
                    self.notes_pressed.remove(note)
                    self.sound_generator.stop_playing_note(note, True)
                else:
                    # We've already removed the note
                    pass

    def draw_song(self, screen):
        y_offset = self.human_interface.rect.h
        x_block_size = self.w/len(self.song)
        y_block_size = (self.h - y_offset)/NUM_ROWS

        for i,chord in enumerate(self.song): 
            if isinstance(chord[0], list):
                oct_band = chord[0][0]
                root_tone = chord[0][1]
            else:
                root_tone = chord[0]
            #root_tone = pos_mod(root_tone,12)
            #root_tone += key
            intervals = chord[1]
            duration = chord[2]

            draw_text_in_block(screen, i,0, x_block_size, y_block_size, "D: "+str(duration), pg.color.THECOLORS['white'], y_offset)

            generated_notes = root_and_intervals_to_int_no_obj(oct_band, root_tone, intervals)
            # j represents a note in integer notation
            # minus one for the duration band
            for j in range(0, NUM_ROWS-1):

                # we will work on octave range 3, 4, 5
                current_octave = j // 12 + 3

                note_data = str(j % 12)


                if (current_octave,j%12) in generated_notes:
                    semitones_from_root = j - root_tone 
                    
                    color = self.colors[pos_mod(semitones_from_root, 12)]

                    note_data += ", " + str(semitones_from_root)
                    #note_data = str(semitones_from_root)
                else:
                    # Draw normally
                    #if j % 12 == key:
                    #    color = pg.color.THECOLORS['white']
                    #else:
                    #    color = pg.color.THECOLORS['black']
                    color = pg.color.THECOLORS['black']

                draw_text_in_block(screen, i,j+1, x_block_size, y_block_size, note_data, color, y_offset)

        pg.display.update()


class ChordInputBox(pg.sprite.Sprite):
    # This class gives input to the Virtual Chord Instrument
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = pg.color.THECOLORS['grey']
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

    def parse_input_to_oct_root_and_intervals(self):
        data = self.text.split()
        try:
            oct_band, root_tone, intervals = data[0], data[1], data[2:]

            oct_band = int(oct_band)
            root_tone = int(root_tone)
            intervals = [int(x) for x in intervals]

            # Hardcoding the duration for now
            chord_data = [ [oct_band, root_tone], intervals, 1]

        except: 
            chord_data = []
            
        return chord_data

    def parse_input_to_notes(self):
        # Put this in a try except block
        data = self.text.split()
        try:
            octave_band, root_tone, intervals = data[0], data[1],  data[2:]

            octave_band = int(octave_band)
            root_tone = int(root_tone)
            intervals = [int(x) for x in intervals]

            notes = root_and_intervals_to_int_no_obj(octave_band, root_tone, intervals)
        except: 
            notes = []

        return notes


    def update(self, event_list):
        for event in event_list:
            #if event.type == pg.MOUSEBUTTONDOWN and not self.active:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.active = self.rect.collidepoint(event.pos)
                self.color = pg.color.THECOLORS['green'] if self.active else pg.color.THECOLORS['grey']
            if event.type == pg.KEYDOWN and self.active:
                if event.key == pg.K_ESCAPE:
                    self.text = self.text[1]
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pg.K_RETURN:
                    # Don't do anything, VCI plays sound
                    pass
                elif event.key == pg.K_TAB:
                    pass
                else:
                    self.text += event.unicode
            self.render_text()

class PlaybackInputBox(pg.sprite.Sprite):
    # This class gives input to the Virtual Chord Instrument
    def __init__(self, x, y, w, font, type = "Standard"):
        super().__init__()
        self.color = pg.color.THECOLORS['grey']
        self.backcolor = None
        self.pos = (x, y) 
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()
        self.type = type

    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pg.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pg.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pg.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.pos)


    def update(self, event_list):
        for event in event_list:
            #if event.type == pg.MOUSEBUTTONDOWN and not self.active:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.active = self.rect.collidepoint(event.pos)
                self.color = pg.color.THECOLORS['green'] if self.active else pg.color.THECOLORS['grey']
            if event.type == pg.KEYDOWN and self.active:
                if event.key == pg.K_ESCAPE:
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pg.K_RETURN:
                    # Don't do anything, VCI plays sound
                    pass
                elif event.key == pg.K_TAB:
                    pass
                else:
                    self.text += event.unicode
            self.render_text()


class PlayBackButton(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, color, device, text_box_input = None):
        super().__init__()
        self.color = color
        self.backcolor = None
        self.pos = (x, y) 
        self.width = w
        self.height = h
        # What device it belongs to, in this case an instrument
        self.device = device
        self.text_box_input = text_box_input

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pg.Surface([self.width, self.height])
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.move_ip(self.pos)

    def update(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if self.rect.collidepoint(event.pos):
                        # logic here - 
                        if self.text_box_input:
                            if self.text_box_input.type == "Slice Player":
                                try:
                                    start, end = [int(x) for x in self.text_box_input.text.split()]
                                    self.device.playback_song(start,end)
                                except:
                                    pass
                        else:
                            self.device.playback_song()

    

class DeleteButton(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, color, device):
        super().__init__()
        self.color = color
        self.backcolor = None
        self.pos = (x, y) 
        self.width = w
        self.height = h
        # What device it belongs to, in this case an instrument
        self.device = device

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pg.Surface([self.width, self.height])
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.move_ip(self.pos)

    def update(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if self.rect.collidepoint(event.pos):
                        # logic here - 
                        self.device.remove_chord()

