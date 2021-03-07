from virtual_instrument_chords import *
from midi_player import *
import pygame
import pygame as pg

WIDTH = 800
HEIGHT = 800
FPS = 60


## initialize pygame and create window
pygame.init()
#pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Name")
clock = pygame.time.Clock()     ## For syncing the FPS


## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()

font = pg.font.SysFont(None, 50)

MP = MidiPlayer()
VCI = VirtualChordInstrument(MP, font, screen, WIDTH, HEIGHT)

all_sprites.add(VCI.human_interface)
all_sprites.add(VCI.PBB)
all_sprites.add(VCI.DB)
all_sprites.add(VCI.slice_player_input)
all_sprites.add(VCI.SB)

## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    events = pygame.event.get()
    for event in events:        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            midi.quit()
            running = False

    screen.fill(pygame.color.THECOLORS['black'])

    #2 Update
    all_sprites.update(events)
    #VI.parse_input_to_sound(events)
    VCI.parse_input_to_sound()
    VCI.record_chord()


    #3 Draw/render

    all_sprites.draw(screen)
    ########################

    ### Put code here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()
