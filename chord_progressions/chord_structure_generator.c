#include <cairo.h>
#include <math.h>
#include <stdio.h>
#include <cairo-pdf.h>



int min(int x, int y) {
  return (x < y) ? x : y;
}

  
void draw_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, char symbols[12][3]) {
  cairo_set_source_rgb(cr, 0, 0, 0);
  cairo_select_font_face (cr, "Sans", CAIRO_FONT_SLANT_NORMAL,
  CAIRO_FONT_WEIGHT_NORMAL);
  cairo_set_font_size (cr, 40.0);

  // Center at middle

  cairo_translate(cr, width/2, height/2);

  // -- Draw two concentric circles --
  cairo_set_line_width (cr, 5.0);
  cairo_arc (cr, 0, 0, start_radius, 0, (2 * M_PI));
  cairo_arc (cr, 0, 0, start_radius + layer_width, 0, (2 * M_PI));
  cairo_stroke (cr);

  for (double i = 0; i < 12; i ++) {
    double ang = (2.0 * M_PI)/12.0 * i;

    cairo_save(cr);

      // -- Rotation -- 
      cairo_rotate(cr, ang);

      // -- Line -- 
      cairo_move_to(cr, start_radius, 0);
      cairo_line_to (cr, start_radius + layer_width, 0);

      // -- Text setup --
      cairo_text_extents_t te;

      char *symbol = symbols[(int)i];

      cairo_save(cr);

        cairo_move_to(cr, 0, 0);

        // Move to middle of sector (angle wise)
        cairo_rotate(cr, (2.0 * M_PI)/24.0);

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


int main(void) 
{
  cairo_surface_t *surface;
  cairo_t *cr;

  int width = 1024, height = 1024;

  surface = cairo_pdf_surface_create("pdffile.pdf", width, height);
  cr = cairo_create(surface);

  cairo_set_source_rgb(cr, 0, 0, 0);
  cairo_select_font_face (cr, "Sans", CAIRO_FONT_SLANT_NORMAL,
  CAIRO_FONT_WEIGHT_NORMAL);
  cairo_set_font_size (cr, 40.0);

  double xc = width/2;
  double yc = height/2;
  double radius = min(xc, yc) - 8;
  double gap_width = radius/8.0;

  char symbols [12][3] = {
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11"
  };

  draw_layer(cr, width, height, 100, 100, symbols);

  cairo_show_page(cr);

  cairo_surface_destroy(surface);
  cairo_destroy(cr);

  return 0;
}

//int main(void) 
//{
//  cairo_surface_t *surface;
//  cairo_t *cr;
//
//  surface = cairo_pdf_surface_create("pdffile.pdf", width, height);
//  cr = cairo_create(surface);
//
//  cairo_set_source_rgb(cr, 0, 0, 0);
//  cairo_select_font_face (cr, "Sans", CAIRO_FONT_SLANT_NORMAL,
//  CAIRO_FONT_WEIGHT_NORMAL);
//  cairo_set_font_size (cr, 40.0);
//
//  int width = 1024, height = 1024;
//  double xc = width/2;
//  double yc = height/2;
//  double radius = min(xc, yc) - 8;
//  double gap_width = radius/8.0;
//
//  cairo_set_line_width (cr, 5.0);
//  cairo_arc (cr, xc, yc, radius, 0, (2 * M_PI));
//  cairo_arc (cr, xc, yc, radius - gap_width, 0, (2 * M_PI));
//  cairo_stroke (cr);
//
//  /* draw helping lines */
//  cairo_set_source_rgba (cr, 1, 0.2, 0.2, 0.6);
//  cairo_set_line_width (cr, 6.0);
//
//  cairo_fill (cr);
//
//
//  cairo_translate(cr, width/2, height/2);
//
//  for (double i = 0; i < 12; i ++) {
//    double ang = (2.0 * M_PI)/12.0 * i;
//
//    cairo_save(cr);
//
//      // -- Rotation -- 
//      cairo_rotate(cr, ang);
//      // -- Line -- 
//      cairo_move_to(cr, 0, 0);
//      cairo_line_to (cr, radius, 0);
//
//      // -- Text setup --
//      cairo_text_extents_t te;
//      int num = (int) i; 
//      char output[50];
//
//      snprintf(output, 50, "%d", num);
//
//      cairo_save(cr);
//
//        cairo_move_to(cr, 0, 0);
//
//        // Move to middle of sector (angle wise)
//
//        cairo_rotate(cr, (2.0 * M_PI)/24.0);
//
//        // Move to middle of sector (vertically)
//
//        cairo_move_to(cr, radius - gap_width, 0);
//
//        // Fix rotation of text in the sector (tangent line)
//
//        cairo_rotate(cr, M_PI/2);
//
//        // Center the text 
//        
//        cairo_text_extents (cr, output, &te);
//
//        cairo_rel_move_to(cr, -te.width/2, -te.height/2);
//
//        cairo_show_text(cr, output);
//
//      cairo_restore(cr);
//
//    cairo_restore(cr);
//
//    printf("iteration: %.6f ,angle:  %.6f \n", i, ang);
//    // cairo_arc (cr, xc, yc, radius, ang, ang);
//    // cairo_line_to (cr, xc, yc);
//  }
//
//  cairo_translate(cr, -width/2, -height/2);
//
//  cairo_stroke (cr);
//
//   // --- 
//  cairo_move_to(cr, 10.0, 50.0);
//  cairo_show_text(cr, "Disziplin ist Macht.");
//
//
//  cairo_show_page(cr);
//
//  cairo_surface_destroy(surface);
//  cairo_destroy(cr);
//
//  return 0;
//}
