
#include "drawing_service.h"

int min(int x, int y) {
  return (x < y) ? x : y;
}

  
void trace_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12]) {
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

      char *symbol = sectors[(int)i].symbol;

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

        cairo_show_text(cr, symbol);

      cairo_restore(cr);

    cairo_restore(cr);

  }

  cairo_translate(cr, -width/2, -height/2);

  cairo_stroke (cr);


}

void highlight_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12]) {

  cairo_set_source_rgba(cr, 255, 0, 0, 0.5);

  cairo_translate(cr, width/2, height/2);

  cairo_move_to(cr, 0, 0);

  double wedge_angle = (2.0 * M_PI)/12.0;

  for (double i = 0; i < 12; i ++) {
    double ang = wedge_angle * i;

    cairo_save(cr);

      // -- Rotation -- 
      cairo_rotate(cr, ang);

      if (sectors[(int)i].highlighted) {

        cairo_arc(cr, 0, 0, start_radius , 0, wedge_angle);

        cairo_arc_negative(cr, 0, 0, start_radius + layer_width , wedge_angle, 0);

        cairo_fill(cr);
        
      }

    cairo_restore(cr);

  }

  cairo_translate(cr, -width/2, -height/2);
}

void draw_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12]) {
  // Highlight first so we can cover seams with the trace
  highlight_layer(cr, width, height, start_radius, layer_width, sectors);
  trace_layer(cr, width, height, start_radius, layer_width, sectors);
}

