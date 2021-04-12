#include <cairo.h>
#include <math.h>
#include <stdio.h>
#include <cairo-pdf.h>

int min(int x, int y) {
  return (x < y) ? x : y;
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
  double angle1 = 0;
  double angle2 = (2 * M_PI);  

  cairo_set_line_width (cr, 5.0);
  cairo_arc (cr, xc, yc, radius, angle1, angle2);
  cairo_arc (cr, xc, yc, radius - gap_width, angle1, angle2);
  cairo_stroke (cr);

  /* draw helping lines */
  cairo_set_source_rgba (cr, 1, 0.2, 0.2, 0.6);
  cairo_set_line_width (cr, 6.0);

  cairo_fill (cr);


  cairo_translate(cr, width/2, height/2);

  for (double i = 0; i < 12; i ++) {
    double ang = (2.0 * M_PI)/12.0 * i;

    cairo_save(cr);

      // -- Rotation -- 
      cairo_rotate(cr, ang);
      // -- Line -- 
      cairo_move_to(cr, 0, 0);
      cairo_line_to (cr, radius, 0);
      // -- Text --
      int num = (int) i; 
      char output[50];

      snprintf(output, 50, "%d", num);

      cairo_save(cr);

        cairo_move_to(cr, 0, 0);

        cairo_rotate(cr, (2.0 * M_PI)/24.0);

        cairo_move_to(cr, radius - gap_width, 0);

        cairo_rotate(cr, M_PI/2);

        cairo_show_text(cr, output);

      cairo_restore(cr);

    cairo_restore(cr);

    printf("iteration: %.6f ,angle:  %.6f \n", i, ang);
    // cairo_arc (cr, xc, yc, radius, ang, ang);
    // cairo_line_to (cr, xc, yc);
  }

  cairo_translate(cr, -width/2, -height/2);

  cairo_stroke (cr);

   // --- 
  cairo_move_to(cr, 10.0, 50.0);
  cairo_show_text(cr, "Disziplin ist Macht.");


  cairo_show_page(cr);

  cairo_surface_destroy(surface);
  cairo_destroy(cr);

  return 0;
}
