import cairo
import math
from fretboard_position_generator import *

WIDTH = 1
HEIGHT = 4
PIXEL_SCALE = 200
PADDING_X = WIDTH/10.0
PADDING_Y = HEIGHT/10.0

TRUE_WIDTH = PIXEL_SCALE*(WIDTH + 2 * PADDING_X)
TRUE_HEIGHT = PIXEL_SCALE*(HEIGHT + 2 * PADDING_Y)

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

def create_fret_representation(filename, chords):

    num_chords = len(chords)

    surface = cairo.SVGSurface("generated_assets/" + filename + ".svg", TRUE_WIDTH * num_chords , TRUE_HEIGHT)
    
    ctx = cairo.Context(surface)
    ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)


    for j in range(num_chords):
        # Move over to do the next drawing

        # PADDING
        ctx.rectangle(0, 0, WIDTH + 2 * PADDING_X , HEIGHT + 2 * PADDING_Y)
        ctx.set_source_rgb(.5, .5, .5)
        ctx.fill()

        # LABEL DIAGRAM
        root_note, chord_type = chords[j]
        label = root_note + " " + chord_type

        ctx.set_font_size(PADDING_Y/2)
        (tx, ty, width, height, dx, dy) = ctx.text_extents(label)
        ctx.set_source_rgb(0, 0, 0)
        ctx.move_to( (WIDTH + 2 * PADDING_X)/2 - width/2 ,PADDING_Y/2 + height/2)
        ctx.show_text(label)


        # Recenter because of padding
        ctx.translate(PADDING_X,PADDING_Y)

        # BACKGROUND    
        ctx.rectangle(0, 0, WIDTH , HEIGHT)
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
            ctx.line_to(WIDTH , y_pos)
        ctx.stroke()

        for i in range(STRINGS):
            # We use -1, because we only want 5 gaps, which gives 6 strings
            x_pos = WIDTH/(STRINGS - 1) * i  
            ctx.move_to(x_pos, 0)
            #ctx.arc(x_pos,0 ,15, 0, 2*math.pi)
            ctx.line_to(x_pos, HEIGHT)

        ctx.stroke()

        # Prepare for note generation

        root_note, chord_type = chords[j]
        intervals = chord_to_interval[chord_type]
        start_fret = E_STRING_FRET_MAPPING[root_note]
        print( root_note, chord_type, intervals,  start_fret )


        positions = chord_constructor(start_fret, intervals, False)

        show_mult_pos_on_fb(positions, ctx)

        # Undo padding translation
        ctx.translate(-PADDING_X,-PADDING_Y)
        ctx.translate(WIDTH + 2 * PADDING_X,0)

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

    # Make text fit in middle of circle
    ctx.set_font_size(rad)
    (tx, ty, width, height, dx, dy) = ctx.text_extents(interval)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(x_pos - width/2,shifted_y + height/2)
    ctx.show_text(interval)

def show_mult_pos_on_fb(list_of_positions, ctx):
    for pos in list_of_positions:
        # String representation is backwards
        x = STRINGS - 1 - pos[0]
        y = pos[1]
        interval = pos[2]
        show_pos_on_fretboard(x, y,interval, ctx)

if __name__ == '__main__':
    #blues = ["G#7", "A7", "B7"]
    blues = [("A", "dom7"), ("D", "dom7"), ("E", "dom7")]
    #for c in blues:
    #    note = c[:-1]
    #    create_fret_representation(c, E_STRING_FRET_MAPPING[note], [0, 4, 7, 10])
    create_fret_representation("blues",blues )

    #for s, c in PATTERNS:
    #    r_pos = random.randint(0, 12)
    #    create_fret_representation(s, r_pos, c)
        

