import os, sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from theory import *

import cairo
import math

WIDTH = 7
HEIGHT = 1
PIXEL_SCALE = 200
PADDING_X = WIDTH/20
PADDING_Y = HEIGHT/5

TRUE_WIDTH = PIXEL_SCALE*(WIDTH + 2 * PADDING_X)
TRUE_HEIGHT = PIXEL_SCALE*(HEIGHT + 2 * PADDING_Y)

NUM_SEMITONES = 12
NUM_DEGREES = 7
PATTERN_LENGTH = 7

TABLE_COLS = 2 * 7 
TABLE_ROWS = NUM_DEGREES + 1

X_UNIT = WIDTH/(14)
Y_UNIT = HEIGHT/(8)

def create_table_for_patterns(filename, patterns, printable=False, cols_per_row=-1):

    num_patterns = len(patterns)
    rows = (num_patterns//cols_per_row)

    surface = cairo.SVGSurface("generated_assets/" + filename + ".svg", TRUE_WIDTH * cols_per_row , TRUE_HEIGHT * rows)
    
    ctx = cairo.Context(surface)
    ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)


    for j in range(num_patterns):
        # Move over to do the next drawing

        if cols_per_row != -1:
            # Don't linebreak on first iteration
            if j != 0 and j % cols_per_row == 0:
                slap_that_typerwriter_left = -1 * cols_per_row * (WIDTH + 2 * PADDING_X)
                ctx.translate(slap_that_typerwriter_left, HEIGHT + 2 * PADDING_Y)

        # PADDING
        ctx.rectangle(0, 0, WIDTH + 2 * PADDING_X , HEIGHT + 2 * PADDING_Y)
        if printable:
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_line_width(0.01)
            ctx.stroke()
        else:
            ctx.set_source_rgb(.5, .5, .5)
            ctx.fill()

        # LABEL DIAGRAM (not implemented)


        #ctx.set_font_size(PADDING_Y/4)
        #(tx, ty, width, height, dx, dy) = ctx.text_extents(title)
        #ctx.set_source_rgb(0, 0, 0)
        #ctx.move_to( (WIDTH + 2 * PADDING_X)/2 - width/2 ,PADDING_Y/2 + height/2)
        #ctx.show_text(title)


        # Recenter because of padding
        ctx.translate(PADDING_X,PADDING_Y)

        # BACKGROUND    
        ctx.rectangle(0, 0, WIDTH , HEIGHT)
        if printable:
            ctx.set_source_rgb(1, 1, 1)
            ctx.stroke()
        else:
            ctx.set_source_rgb(0, 0, 0)
            ctx.fill()

        # PREPARE BRUSH
        if printable:
            ctx.set_source_rgb(0,0,0)
        else:
            ctx.set_source_rgb(1,1,1)

        ctx.set_line_width(0.01)

        # DRAW GRID

        # Add one for the top row which displays the pattern
        for i in range(TABLE_ROWS + 1 ):
            y_pos = HEIGHT/(TABLE_ROWS) * i
            ctx.move_to(0, y_pos)
            ctx.line_to(WIDTH , y_pos)
        ctx.stroke()
        
        for i in range(TABLE_COLS+1):
            # We use -1, because we only want 5 gaps, which gives 6 strings
            x_pos = WIDTH/(TABLE_COLS) * i  
            ctx.move_to(x_pos, 0)
            #ctx.arc(x_pos,0 ,15, 0, 2*math.pi)
            ctx.line_to(x_pos, HEIGHT)

        ctx.stroke()

        # Prepare for note generation

        #print( root_note, chord_type, intervals,  start_fret )

        pattern = patterns[j]
        print(pattern)

        # The pattern is interwoven between the numbers
        # So we need an extra on the end thus (+1)
        top_row = [" "] * (len(pattern) * 2)

        for i in range(len(pattern)):
            top_row[2 * i + 1] = str(pattern[i])

        full_table = gen_table_from_pattern(pattern)
        full_table.insert(0, top_row)
        
        print(full_table)

        draw_table(full_table, ctx, printable)

        #positions = chord_constructor(start_fret, intervals, False)

        #show_mult_pos_on_fb(positions, ctx, printable)

        # Undo padding translation
        ctx.translate(-PADDING_X,-PADDING_Y)
        ctx.translate(WIDTH + 2 * PADDING_X,0)

def gen_table_from_pattern(pattern):
    table = []
    for i in range(len(pattern)):
        table.append(sum_pat(pattern, i))
    return table

def sum_pat(pattern, offset):
    # Offset is where you start in the pattern
    N = len(pattern)
    new_pat = [""] * (N * 2)
    s = 0
    for i in range(N):
      mark = "*" if i in (0, 2, 4, 6) else ""
      # This makes it so it will thread between pattern
      # p1 |    | p2 |    | p3 |    | 
      #    | s1 |    | s2 |    | s3 |
      curr_pat_ele = pattern[(i + offset) % N]
      pos =  2*(i + offset) % (N * 2)
      new_pat[pos] = str(s) + mark
      s += curr_pat_ele

    ## 7th chord analysis
    #idxs = []     
    #for c, itv in seventh_chord_to_interval.items():
    #    contained = set(itv).issubset(set([int(x) for x in new_pat if x != ""]))
    #    if contained:
    #        for i in range(len(new_pat)):
    #            if new_pat[i] != "" and int(new_pat[i]) in itv:
    #                idxs.append(i)
    #        break
    #for i in idxs:
    #    new_pat[i] += "*" 

    return new_pat

def draw_at_pos_in_table(x, y, text, ctx, printable=False):

    if printable:
        ctx.set_source_rgb(0, 0, 0)
    else:
        ctx.set_source_rgb(1, 1, 1)

    x_pos = x * X_UNIT + X_UNIT/2
    y_pos = y * Y_UNIT + Y_UNIT/2

    sz = min(X_UNIT, Y_UNIT)

    ctx.set_font_size(sz)
    (tx, ty, width, height, dx, dy) = ctx.text_extents(text)

    if printable:
        ctx.set_source_rgb(0, 0, 0)
    else:
        ctx.set_source_rgb(1, 1, 1)

    # Center in middle
    ctx.move_to(x_pos - width/2,y_pos + height/2)
    ctx.show_text(text)

def draw_table(table, ctx, printable=False):
    # Our table is a list of rows
    for y in range(len(table)):
        for x in range(len(table[y])):
            text = table[y][x]
            draw_at_pos_in_table(x, y,text, ctx, printable)

if __name__ == '__main__':
    #blues = ["G#7", "A7", "B7"]
    #blues = [("A", "dom7"), ("D", "dom7"), ("E", "dom7")]
    #for c in blues:
    #    note = c[:-1]
    #    create_fret_representation(c, E_STRING_FRET_MAPPING[note], [0, 4, 7, 10])
    create_table_for_patterns("all_scales", list(scales.values()), True, 2)
    #for i in range(7):
    #    print(sum_pat(scales['maj'], i))

    #for s, c in PATTERNS:
    #    r_pos = random.randint(0, 12)
    #    create_fret_representation(s, r_pos, c)
        

