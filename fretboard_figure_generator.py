import cairo
import math
from chord_generation import *

WIDTH = 1
HEIGHT = 4
PIXEL_SCALE = 200

TRUE_WIDTH = WIDTH*PIXEL_SCALE
TRUE_HEIGHT = HEIGHT*PIXEL_SCALE

FRETS = 24
STRINGS = 6

X_UNIT = WIDTH/(STRINGS-1)
Y_UNIT = HEIGHT/(FRETS-1)

E_STRING_FRET_MAPPING = {
'E':0,
'F':1,
'F#':2,
'Gb':2,
'G':3,
'G#':4,
'Ab':4,
'A':5,
'A#':6,
'Bb':6,
'B':7,
'C':8 ,
'C#':9,
'Db':9,
'D':10,
'D#':11,
'Eb':11,
}

def create_fret_representation(filename, start_fret, chord):

    surface = cairo.SVGSurface(filename + ".svg", TRUE_WIDTH , TRUE_HEIGHT)

    ctx = cairo.Context(surface)
    ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    # BACKGROUND    
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    # PREPARE BRUSH
    ctx.set_source_rgb(1,1,1)
    ctx.set_line_width(0.01)

    # DRAW NUT
    ctx.rectangle(0, 2 * Y_UNIT/3, WIDTH, Y_UNIT/3)

    # DRAW GRID

    for i in range(FRETS):
        # TODO fix the scale
        scale = .5 *  (FRETS + 9)/(i+1)
        y_pos = HEIGHT/(FRETS - 1) * i
        scaled_y_pos = y_pos * scale
        ctx.move_to(0, y_pos)
        ctx.line_to(WIDTH, y_pos)
    ctx.stroke()

    for i in range(STRINGS):
        # We use -1, because we only want 5 gaps, which gives 6 strings
        x_pos = WIDTH/(STRINGS - 1) * i
        ctx.move_to(x_pos, 0)
        #ctx.arc(x_pos,0 ,15, 0, 2*math.pi)
        ctx.line_to(x_pos, HEIGHT)

    ctx.stroke()


    def show_pos_on_fretboard(x, y, interval, ctx):
        ctx.set_source_rgb(1, 1, 1)
        x_pos = x * X_UNIT 
        # We have to do this because the first fret isn't visible
        y_pos = (y+1) * Y_UNIT
        # DRAW CIRCLE
        rad = min(X_UNIT, Y_UNIT)/4
        shifted_y = y_pos - Y_UNIT/4
        ctx.arc(x_pos,shifted_y ,rad , 0, 2*math.pi)
        ctx.fill()


        ctx.set_font_size(rad)
        (tx, ty, width, height, dx, dy) = ctx.text_extents(interval)
        ctx.set_source_rgb(0, 0, 0)
        ctx.move_to(x_pos - width/2,shifted_y + height/2)
        ctx.show_text(interval)

    def show_mult_pos_on_fb(list_of_positions, ctx):
        for pos in list_of_positions:
            # String representation is backwards
            print(pos)
            x = STRINGS - 1 - pos[0]
            y = pos[1]
            interval = pos[2]
            show_pos_on_fretboard(x, y,interval, ctx)

    positions = chord_constructor(start_fret, chord, False)

    show_mult_pos_on_fb(positions, ctx)

if __name__ == '__main__':
    blues = ["G#7", "A7", "B7"]
    for c in blues:
        note = c[:-1]
        create_fret_representation(c, E_STRING_FRET_MAPPING[note], [0, 4, 7, 10])
        

