#include "drawing_service.h"

int min(int x, int y) {
  return (x < y) ? x : y;
}

  
void trace_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12]) {
  // This function also marks them with color
  
  cairo_set_source_rgb(cr, 0, 0, 0);
  cairo_select_font_face (cr, "Sans", CAIRO_FONT_SLANT_NORMAL,
  CAIRO_FONT_WEIGHT_NORMAL);
  cairo_set_font_size (cr, layer_width/2);

  // Center at middle

  cairo_translate(cr, width/2, height/2);

  // -- Draw two concentric circles --
  double line_width = 5.0;
  cairo_set_line_width (cr, line_width);
  cairo_new_sub_path(cr);
  cairo_arc (cr, 0, 0, start_radius, 0 , (2 * M_PI) );
  cairo_arc (cr, 0, 0, start_radius + layer_width, 0, (2 * M_PI));
  cairo_stroke (cr);

  double wedge_angle = (2.0 * M_PI)/12.0;

  for (double i = 0; i < 12; i ++) {
    int idx = (int) i;
    double ang = wedge_angle * i;

    cairo_save(cr);

      // -- Rotation -- 
      cairo_rotate(cr, ang);

      // -- Line -- 
      cairo_move_to(cr, start_radius, 0);
      cairo_line_to (cr, start_radius + layer_width, 0);

      cairo_stroke (cr);

      // -- Text setup --
      cairo_text_extents_t te;

      char *symbol = sectors[idx].symbol;

      cairo_save(cr);

        cairo_move_to(cr, 0, 0);

        // Move to middle of sector (angle wise)
        cairo_rotate(cr, wedge_angle/2);

        // Move to middle of sector (vertically)
        cairo_move_to(cr, start_radius + layer_width/2 , 0);

        // Fix rotation of text in the sector (tangent line)
        cairo_rotate(cr, M_PI/2);

        // Center the text 
        cairo_text_extents (cr, symbol, &te);

        cairo_rel_move_to(cr, -te.width/2, +te.height/2);

        // invert color for readability

        cairo_set_source_rgb(cr, 1 - sectors[idx].red, 1 - sectors[idx].green, 1 - sectors[idx].blue);

        cairo_show_text(cr, symbol);

      cairo_restore(cr);

    cairo_restore(cr);

  }

  cairo_translate(cr, -width/2, -height/2);

  cairo_stroke (cr);
}

void setup_base_layer_colors(struct sector sectors[12], int root_tone, int *sequence, int seq_len) {
  // Assumption is that the sequence must bring you back to where you start
  // eg 2212221 the sum is 12.
  for (int i = 0; i < 12; i++) {
    // Make everything grey
    sectors[i].red = .5; sectors[i].green = .5; sectors[i].blue = .5;
  }
  int position = root_tone;
  for (int j = 0; j < seq_len; j++) {
    if (position == root_tone) {
      // Special color for root tone
      sectors[position].red = 1; sectors[position].green = 1; sectors[position].blue = 1;
    } else {
      sectors[position].red = 0; sectors[position].green = 0; sectors[position].blue = 0;
    }
    position += sequence[j];
    position %= 12;
  }
}

void setup_layer_colors(struct sector sectors[12]) {
  for (double i = 0; i < 12; i ++) {
    int idx = (int) i;

    long relative_position;
    if (sectors[idx].symbol[0] != '\0') {
      relative_position = strtol(sectors[idx].symbol, NULL, 10);
    } else {
      relative_position = -1;
    }

    switch(relative_position) {

      case 0:
        sectors[idx].red = 0/255.0; sectors[idx].green = 0/255.0; sectors[idx].blue = 255/255.0;
      break; 

      case 1:
        sectors[idx].red = 128/255.0; sectors[idx].green = 128/255.0; sectors[idx].blue = 51/255.0;
      break; 

      case 2:
        sectors[idx].red = 127/255.0; sectors[idx].green = 255/255.0; sectors[idx].blue = 212/255.0;
      break; 

      case 3:
        sectors[idx].red = 255/255.0; sectors[idx].green = 165/255.0; sectors[idx].blue = 0/255.0;
      break; 

      case 4:
        sectors[idx].red = 139/255.0; sectors[idx].green = 0/255.0; sectors[idx].blue = 0/255.0;
      break; 

      case 5:
        sectors[idx].red = 46/255.0; sectors[idx].green = 139/255.0; sectors[idx].blue = 87/255.0;
      break; 

      case 6:
        sectors[idx].red = 127/255.0; sectors[idx].green = 255/255.0; sectors[idx].blue = 0/255.0;
      break; 

      case 7:
        sectors[idx].red = 0/255.0; sectors[idx].green = 255/255.0; sectors[idx].blue = 0/255.0;
      break; 

      case 8:
        sectors[idx].red = 255/255.0; sectors[idx].green = 248/255.0; sectors[idx].blue = 220/255.0;
      break; 

      case 9:
        sectors[idx].red = 238/255.0; sectors[idx].green = 173/255.0; sectors[idx].blue = 14/255.0;
      break; 

      case 10:
        sectors[idx].red = 139/255.0; sectors[idx].green = 71/255.0; sectors[idx].blue = 137/255.0;
      break; 

      case 11:
        sectors[idx].red = 255/255.0; sectors[idx].green = 20/255.0; sectors[idx].blue = 147/255.0;
      break; 

      default:
        sectors[idx].red = .5; sectors[idx].green = .5; sectors[idx].blue = .5;
      break;


    }
  }
}

void highlight_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12]) {

  cairo_translate(cr, width/2, height/2);

  cairo_move_to(cr, 0, 0);

  double wedge_angle = (2.0 * M_PI)/12.0;

  for (double i = 0; i < 12; i ++) {
    int idx = (int) i;
    double ang = wedge_angle * i;

    cairo_save(cr);

      // -- Rotation -- 
      cairo_rotate(cr, ang);

      // Draw a wedge
      cairo_arc(cr, 0, 0, start_radius , 0, wedge_angle);
      cairo_arc_negative(cr, 0, 0, start_radius + layer_width , wedge_angle, 0);

      if (sectors[idx].highlighted) {
        cairo_set_source_rgb(cr, sectors[idx].red, sectors[idx].green, sectors[idx].blue);
      } else {
        cairo_set_source_rgb(cr, .5 , .5, .5);
      }

      cairo_fill(cr);

    cairo_restore(cr);

  }

  cairo_translate(cr, -width/2, -height/2);
}

void draw_title(cairo_t *cr, int width, int height, char *title) {

  cairo_set_source_rgb(cr, 0, 0, 0);
  cairo_select_font_face (cr, "Sans", CAIRO_FONT_SLANT_NORMAL,
  CAIRO_FONT_WEIGHT_NORMAL);
  cairo_set_font_size (cr, width/50);

  cairo_save(cr);

    cairo_move_to(cr, width*1/2, width/20);

    cairo_text_extents_t te;

    //// Center the text 
    cairo_text_extents (cr, title, &te);

    cairo_rel_move_to(cr, -te.width/2, +te.height/2);

    cairo_show_text(cr, title);

  cairo_restore(cr);

}

void sign_name(cairo_t *cr, int width, int height) {

  cairo_set_source_rgb(cr, 0, 0, 0);
  cairo_select_font_face (cr, "Sans", CAIRO_FONT_SLANT_NORMAL,
  CAIRO_FONT_WEIGHT_NORMAL);
  cairo_set_font_size (cr, width/50);

  cairo_save(cr);

    cairo_move_to(cr, width*5/6, height - width/20);

    cairo_text_extents_t te;

    char *name = "cuppajoeman";

    // Center the text 
    cairo_text_extents (cr, name, &te);

    cairo_rel_move_to(cr, -te.width/2, +te.height/2);

    cairo_show_text(cr, name);

  cairo_restore(cr);

}

void draw_base_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12], int root_tone, int *sequence, int seq_len) {
  setup_base_layer_colors(sectors, root_tone, sequence, seq_len);
  // Highlight first so we can cover seams with the trace
  highlight_layer(cr, width, height, start_radius, layer_width, sectors);
  trace_layer(cr, width, height, start_radius, layer_width, sectors);
}

void draw_chord_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12], struct chord chord) {
  construct_sectors_from_chord(sectors, chord);
  setup_layer_colors(sectors);
  // Highlight first so we can cover seams with the trace
  highlight_layer(cr, width, height, start_radius, layer_width, sectors);
  trace_layer(cr, width, height, start_radius, layer_width, sectors);
  // Just was propoating title through to the main program.
}

void construct_sectors_from_chord(struct sector sectors[12], struct chord chord) {
  // Sets up the data, symbols and highlighted data
  // Initialize everything to be the empty string
  for (int i = 0; i < 12; i++) {
   strcpy(sectors[i].symbol,""); 
  }

  for (int j = 0; j < chord.num_intervals; j++) {
    int interval = chord.intervals[j];
    char i_str[3];
    sprintf(i_str, "%d", interval);
    strcpy(sectors[(chord.root_tone + interval) % 12].symbol, i_str);
    sectors[(chord.root_tone + interval) % 12].highlighted = true;
  }
}

void construct_sectors_all_notes(struct sector sectors[12]) {
  // Initializes the sector array
  for (int i = 0; i < 12; i++) {
    char i_str[3];
    sprintf(i_str, "%d", i);
    strcpy(sectors[i].symbol, i_str); 
    sectors[i].highlighted = true;
  }
}

