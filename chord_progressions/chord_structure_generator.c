#include <cairo.h>
#include <math.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <cairo-pdf.h>

int min(int x, int y) {
  return (x < y) ? x : y;
}

struct sector {
  char symbol[3];
  bool highlighted;
  double red;
  double green;
  double blue;
};

  
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



int main(void) 
{
  cairo_surface_t *surface;
  cairo_t *cr;

  int width = 1024, height = 1024;

  surface = cairo_pdf_surface_create("pdffile.pdf", width, height);
  cr = cairo_create(surface);

  // Drawing data
  // Useful vim regexs for creating data
  /*
  '<,'>s/\[\(\d\+\)/\=(submatch(1)+5)%12/
  '<,'>s/_3/_3[
  '<,'>s/true/false/g
  */

  // General form of data for copy pasting
  /*
  struct sector layer_N[12];

  strcpy(layer_N[0].symbol, "0");
  layer_N[0].highlighted = true;
  strcpy(layer_N[1].symbol, "1");
  layer_N[1].highlighted = false;
  strcpy(layer_N[2].symbol, "2");
  layer_N[2].highlighted = true;
  strcpy(layer_N[3].symbol, "3");
  layer_N[3].highlighted = false;
  strcpy(layer_N[4].symbol, "4");
  layer_N[4].highlighted = true;
  strcpy(layer_N[5].symbol, "5");
  layer_N[5].highlighted = true;
  strcpy(layer_N[6].symbol, "6");
  layer_N[6].highlighted = false;
  strcpy(layer_N[7].symbol, "7");
  layer_N[7].highlighted = true;
  strcpy(layer_N[8].symbol, "8");
  layer_N[8].highlighted = false;
  strcpy(layer_N[9].symbol, "9");
  layer_N[9].highlighted = true;
  strcpy(layer_N[10].symbol, "10");
  layer_N[10].highlighted = false;
  strcpy(layer_N[11].symbol, "11");
  layer_N[11].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_N);

  radius_so_far += 50;
   
 */
  
  double radius_so_far = 0;

  struct sector layer_1[12];

  strcpy(layer_1[0].symbol, "0");
  layer_1[0].highlighted = true;
  strcpy(layer_1[1].symbol, "1");
  layer_1[1].highlighted = false;
  strcpy(layer_1[2].symbol, "2");
  layer_1[2].highlighted = true;
  strcpy(layer_1[3].symbol, "3");
  layer_1[3].highlighted = false;
  strcpy(layer_1[4].symbol, "4");
  layer_1[4].highlighted = true;
  strcpy(layer_1[5].symbol, "5");
  layer_1[5].highlighted = true;
  strcpy(layer_1[6].symbol, "6");
  layer_1[6].highlighted = false;
  strcpy(layer_1[7].symbol, "7");
  layer_1[7].highlighted = true;
  strcpy(layer_1[8].symbol, "8");
  layer_1[8].highlighted = false;
  strcpy(layer_1[9].symbol, "9");
  layer_1[9].highlighted = true;
  strcpy(layer_1[10].symbol, "10");
  layer_1[10].highlighted = false;
  strcpy(layer_1[11].symbol, "11");
  layer_1[11].highlighted = true;

  draw_layer(cr, width, height, 100, 50, layer_1);

  radius_so_far = 150;

  struct sector layer_2[12];

  strcpy(layer_2[2].symbol, "0");
  layer_2[2].highlighted = false;
  strcpy(layer_2[3].symbol, "");
  layer_2[3].highlighted = false;
  strcpy(layer_2[4].symbol, "");
  layer_2[4].highlighted = false;
  strcpy(layer_2[5].symbol, "3");
  layer_2[5].highlighted = false;
  strcpy(layer_2[6].symbol, "");
  layer_2[6].highlighted = false;
  strcpy(layer_2[7].symbol, "");
  layer_2[7].highlighted = false;
  strcpy(layer_2[8].symbol, "");
  layer_2[8].highlighted = false;
  strcpy(layer_2[9].symbol, "7");
  layer_2[9].highlighted = false;
  strcpy(layer_2[10].symbol, "");
  layer_2[10].highlighted = false;
  strcpy(layer_2[11].symbol, "");
  layer_2[11].highlighted = false;
  strcpy(layer_2[0].symbol, "10");
  layer_2[0].highlighted = false;
  strcpy(layer_2[1].symbol, "");
  layer_2[1].highlighted = false;

  draw_layer(cr, width, height, radius_so_far, 50, layer_2);

  radius_so_far += 50;

  struct sector layer_3[12];

  strcpy(layer_3[7].symbol, "0");
  layer_3[7].highlighted = false;
  strcpy(layer_3[8].symbol, "");
  layer_3[8].highlighted = false;
  strcpy(layer_3[9].symbol, "");
  layer_3[9].highlighted = false;
  strcpy(layer_3[10].symbol, "");
  layer_3[10].highlighted = false;
  strcpy(layer_3[11].symbol, "4");
  layer_3[11].highlighted = false;
  strcpy(layer_3[0].symbol, "");
  layer_3[0].highlighted = false;
  strcpy(layer_3[1].symbol, "");
  layer_3[1].highlighted = false;
  strcpy(layer_3[2].symbol, "7");
  layer_3[2].highlighted = false;
  strcpy(layer_3[3].symbol, "");
  layer_3[3].highlighted = false;
  strcpy(layer_3[4].symbol, "");
  layer_3[4].highlighted = false;
  strcpy(layer_3[5].symbol, "10");
  layer_3[5].highlighted = false;
  strcpy(layer_3[6].symbol, "");
  layer_3[6].highlighted = false;

  draw_layer(cr, width, height, radius_so_far, 50, layer_3);

  radius_so_far += 50;

  struct sector layer_4[12];

  strcpy(layer_4[0].symbol, "0");
  layer_4[0].highlighted = false;
  strcpy(layer_4[1].symbol, "");
  layer_4[1].highlighted = false;
  strcpy(layer_4[2].symbol, "");
  layer_4[2].highlighted = false;
  strcpy(layer_4[3].symbol, "");
  layer_4[3].highlighted = false;
  strcpy(layer_4[4].symbol, "4");
  layer_4[4].highlighted = false;
  strcpy(layer_4[5].symbol, "");
  layer_4[5].highlighted = false;
  strcpy(layer_4[6].symbol, "");
  layer_4[6].highlighted = false;
  strcpy(layer_4[7].symbol, "7");
  layer_4[7].highlighted = false;
  strcpy(layer_4[8].symbol, "");
  layer_4[8].highlighted = false;
  strcpy(layer_4[9].symbol, "");
  layer_4[9].highlighted = false;
  strcpy(layer_4[10].symbol, "");
  layer_4[10].highlighted = false;
  strcpy(layer_4[11].symbol, "11");
  layer_4[11].highlighted = false;

  draw_layer(cr, width, height, radius_so_far, 50, layer_4);

  radius_so_far += 50;


  cairo_show_page(cr);

  cairo_surface_destroy(surface);
  cairo_destroy(cr);

  return 0;
}

