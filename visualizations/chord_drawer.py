import pygame
from math import floor
import os,sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from midiutil import MIDIFile
from theory_utils import *
from sound_utils import *

WIDTH = 1920
HEIGHT = 1080

NUM_ROWS = 37


colors = {
    0: pygame.color.THECOLORS['blue'],
    1: pygame.color.THECOLORS['orangered4'],
    2: pygame.color.THECOLORS['aquamarine'],
    3: pygame.color.THECOLORS['orange'],
    4: pygame.color.THECOLORS['red4'],
    5: pygame.color.THECOLORS['seagreen'],
    6: pygame.color.THECOLORS['chartreuse'],
    7: pygame.color.THECOLORS['green'],
    8: pygame.color.THECOLORS['cornsilk'],
    9: pygame.color.THECOLORS['darkgoldenrod2'],
    10: pygame.color.THECOLORS['orchid4'],
    11: pygame.color.THECOLORS['red']
}


def invert_color(rgb_color):
    return (255 - rgb_color[0], 255 - rgb_color[1], 255 - rgb_color[2])

def pos_mod(x,m):
    return (x%m + m)%m;

def draw_text_in_block(screen, x,y, x_block_size, y_block_size, text,block_color):

    block = pygame.Rect((x_block_size * x, y_block_size * y), (x_block_size, y_block_size))
    pygame.draw.rect(screen, block_color, block)

    center_of_block = (x_block_size * x + x_block_size/2, y_block_size * y + y_block_size/2)

    fitted_size = floor(min(x_block_size, y_block_size))

    font = pygame.font.Font(None, fitted_size)
    text = font.render(text, True, invert_color(block_color))
    text_rect = text.get_rect(center=center_of_block)
    screen.blit(text, text_rect)

def visualize_chords(chords,key, name):

    ## initialize pygame and create window
    pygame.init()
    pygame.mixer.init()  ## For sound
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Name")
    clock = pygame.time.Clock()     ## For syncing the FPS

    x_block_size = WIDTH/len(chords)
    y_block_size = HEIGHT/NUM_ROWS


    for i,chord in enumerate(chords): 
        if isinstance(chord[0], list):
            root_tone = chord[0][1]
        else:
            root_tone = chord[0]
        #root_tone = pos_mod(root_tone,12)
        root_tone += key
        intervals = chord[1]
        duration = chord[2]

        draw_text_in_block(screen, i,0, x_block_size, y_block_size, "D: "+str(duration), pygame.color.THECOLORS['white'])

        generated_notes = root_and_intervals_to_int_basic(root_tone, intervals, 3)
        print(generated_notes )
        # j represents a note in integer notation
        # minus one for the duration band
        for j in range(0, NUM_ROWS-1):

            note_data = str(j % 12)

            if j in generated_notes:
                semitones_from_root = j - root_tone 
                
                color = colors[semitones_from_root]

                note_data += ", " + str(semitones_from_root)
                #note_data = str(semitones_from_root)
            else:
                # Draw normally
                if j % 12 == key:
                    color = pygame.color.THECOLORS['white']
                else:
                    color = pygame.color.THECOLORS['black']

            draw_text_in_block(screen, i,j+1, x_block_size, y_block_size, note_data, color)

    pygame.display.update()

    rect = pygame.Rect(0,0, WIDTH, HEIGHT)
    screenshot = pygame.Surface((WIDTH, HEIGHT))
    screenshot.blit(screen, rect)
    pygame.image.save(screenshot, name+".jpg")
    pygame.QUIT


    #running = True
    #while running:

    #    #1 Process input/events
    #    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    #    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
    #        ## listening for the the X button at the top
    #        if event.type == pygame.QUIT:
    #            running = False


