#include "../../csg/drawing_service.h"

int main(void) 
{
  cairo_surface_t *surface;
  cairo_t *cr;

  int width = 1024, height = 1024;

  surface = cairo_pdf_surface_create("Enter File Name.pdf", width, height);
  cr = cairo_create(surface);

  draw_title(cr, width, height, "Enter Title");
  sign_name(cr, width, height);

  // Drawing data
  // Useful vim regexs for creating data
  /*
   
  double mod and addition make sure it's positive
  '<,'>s/\[\(\d\+\)\]/\='[' .((submatch(1)-2)%12+12)%12. ']'/g
  incrementer
  '<,'>s/_\(\d\+\)/\='_' .(submatch(1)+1)/g
  '<,'>s/true/false/g
  */

  // General form of data for copy pasting
  
  /*
   
  // ------ NEW LAYER ------
  struct sector layer_N[12];

  strcpy(layer_N[0].symbol, "0"); layer_N[0].highlighted = true;
  strcpy(layer_N[1].symbol, "1"); layer_N[1].highlighted = false;
  strcpy(layer_N[2].symbol, "2"); layer_N[2].highlighted = true;
  strcpy(layer_N[3].symbol, "3"); layer_N[3].highlighted = false;
  strcpy(layer_N[4].symbol, "4"); layer_N[4].highlighted = true;
  strcpy(layer_N[5].symbol, "5"); layer_N[5].highlighted = true;
  strcpy(layer_N[6].symbol, "6"); layer_N[6].highlighted = false;
  strcpy(layer_N[7].symbol, "7"); layer_N[7].highlighted = true;
  strcpy(layer_N[8].symbol, "8"); layer_N[8].highlighted = false;
  strcpy(layer_N[9].symbol, "9"); layer_N[9].highlighted = true;
  strcpy(layer_N[10].symbol, "10"); layer_N[10].highlighted = false;
  strcpy(layer_N[11].symbol, "11"); layer_N[11].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_N, false);

  radius_so_far += 50;
   
 */

  struct sector base_layer[12];

  strcpy(base_layer[0].symbol, "0"); base_layer[0].highlighted = true;
  strcpy(base_layer[1].symbol, "1"); base_layer[1].highlighted = false;
  strcpy(base_layer[2].symbol, "2"); base_layer[2].highlighted = true;
  strcpy(base_layer[3].symbol, "3"); base_layer[3].highlighted = false;
  strcpy(base_layer[4].symbol, "4"); base_layer[4].highlighted = true;
  strcpy(base_layer[5].symbol, "5"); base_layer[5].highlighted = true;
  strcpy(base_layer[6].symbol, "6"); base_layer[6].highlighted = false;
  strcpy(base_layer[7].symbol, "7"); base_layer[7].highlighted = true;
  strcpy(base_layer[8].symbol, "8"); base_layer[8].highlighted = false;
  strcpy(base_layer[9].symbol, "9"); base_layer[9].highlighted = true;
  strcpy(base_layer[10].symbol, "10"); base_layer[10].highlighted = false;
  strcpy(base_layer[11].symbol, "11"); base_layer[11].highlighted = true;

  radius_so_far = 100;

  draw_layer(cr, width, height, radius_so_far, 50, base_layer, true);

  radius_so_far += 50;


  // cleanup
  cairo_show_page(cr);

  cairo_surface_destroy(surface);
  cairo_destroy(cr);

  return 0;
}

