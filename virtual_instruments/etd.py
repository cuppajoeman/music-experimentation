from virtual_instrument import *
from midi_player import *
import pygame
import pygame as pg

WIDTH = 800
HEIGHT = 800
FPS = 60


## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Name")
clock = pygame.time.Clock()     ## For syncing the FPS


## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()

vertical_snake_mapping = {
pg.K_z: 0, pg.K_a: 1,pg.K_q: 2,pg.K_1: 3,pg.K_2: 4,pg.K_w: 5,pg.K_s: 6,pg.K_x: 7,pg.K_c: 8,pg.K_d: 9,pg.K_e: 10,pg.K_3: 11,
pg.K_v: 12,pg.K_f: 13,pg.K_r: 14,pg.K_4: 15,pg.K_5: 16,pg.K_t: 17,pg.K_g: 18,pg.K_b: 19,pg.K_n: 20,pg.K_h: 21,pg.K_y: 22,pg.K_6: 23,
pg.K_m: 24,pg.K_j: 25,pg.K_u: 26,pg.K_7: 27,pg.K_8: 28,pg.K_i: 29,pg.K_k: 30,pg.K_COMMA: 31,pg.K_PERIOD: 32,pg.K_l: 33,pg.K_o: 34,pg.K_9: 35
}

MP = MidiPlayer()
VI = VirtualInstrument(vertical_snake_mapping, MP)

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


    #2 Update
    all_sprites.update()
    #VI.parse_input_to_sound(events)
    VI.parse_input_to_sound_get_pressed()


    #3 Draw/render
    screen.fill(pygame.color.THECOLORS['black'])

    all_sprites.draw(screen)
    ########################

    ### Put code here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()
