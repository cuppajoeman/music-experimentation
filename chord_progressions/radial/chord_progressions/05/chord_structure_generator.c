#include "../../csg/drawing_service.h"

int main(void) 
{
  cairo_surface_t *surface;
  cairo_t *cr;

  int width = 1024, height = 1024;

  surface = cairo_pdf_surface_create("pdffile.pdf", width, height);
  cr = cairo_create(surface);

  //draw_title(cr, width, height, "");
  sign_name(cr, width, height);

  // Drawing data
  // Useful vim regexs for creating data
  /*
  '<,'>s/\[\(\d\+\)/\=(submatch(1)+K)%12/ | '<,'>s/_N/_N[
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


  struct sector layer_1[12];

  strcpy(layer_1[0].symbol, "0"); layer_1[0].highlighted = true;
  strcpy(layer_1[1].symbol, "1"); layer_1[1].highlighted = false;
  strcpy(layer_1[2].symbol, "2"); layer_1[2].highlighted = true;
  strcpy(layer_1[3].symbol, "3"); layer_1[3].highlighted = false;
  strcpy(layer_1[4].symbol, "4"); layer_1[4].highlighted = true;
  strcpy(layer_1[5].symbol, "5"); layer_1[5].highlighted = true;
  strcpy(layer_1[6].symbol, "6"); layer_1[6].highlighted = false;
  strcpy(layer_1[7].symbol, "7"); layer_1[7].highlighted = true;
  strcpy(layer_1[8].symbol, "8"); layer_1[8].highlighted = false;
  strcpy(layer_1[9].symbol, "9"); layer_1[9].highlighted = true;
  strcpy(layer_1[10].symbol, "10"); layer_1[10].highlighted = false;
  strcpy(layer_1[11].symbol, "11"); layer_1[11].highlighted = true;

  int radius_so_far = 150;

  draw_layer(cr, width, height, radius_so_far, 50, layer_1, true);

  radius_so_far += 50;
  
  // --

  struct sector layer_2[12];

  strcpy(layer_2[0].symbol, "0"); layer_2[0].highlighted = true;
  strcpy(layer_2[1].symbol, ""); layer_2[1].highlighted = true;
  strcpy(layer_2[2].symbol, ""); layer_2[2].highlighted = true;
  strcpy(layer_2[3].symbol, ""); layer_2[3].highlighted = true;
  strcpy(layer_2[4].symbol, "4"); layer_2[4].highlighted = true;
  strcpy(layer_2[5].symbol, ""); layer_2[5].highlighted = true;
  strcpy(layer_2[6].symbol, ""); layer_2[6].highlighted = true;
  strcpy(layer_2[7].symbol, "7"); layer_2[7].highlighted = true;
  strcpy(layer_2[8].symbol, ""); layer_2[8].highlighted = true;
  strcpy(layer_2[9].symbol, ""); layer_2[9].highlighted = true;
  strcpy(layer_2[10].symbol, ""); layer_2[10].highlighted = true;
  strcpy(layer_2[11].symbol, "11"); layer_2[11].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_2, false);

  radius_so_far += 50;

  // --

  struct sector layer_3[12];

  strcpy(layer_3[5].symbol, "0"); layer_3[5].highlighted = true;
  strcpy(layer_3[6].symbol, ""); layer_3[6].highlighted = true;
  strcpy(layer_3[7].symbol, ""); layer_3[7].highlighted = true;
  strcpy(layer_3[8].symbol, ""); layer_3[8].highlighted = true;
  strcpy(layer_3[9].symbol, "4"); layer_3[9].highlighted = true;
  strcpy(layer_3[10].symbol, ""); layer_3[10].highlighted = true;
  strcpy(layer_3[11].symbol, ""); layer_3[11].highlighted = true;
  strcpy(layer_3[0].symbol, "7"); layer_3[0].highlighted = true;
  strcpy(layer_3[1].symbol, ""); layer_3[1].highlighted = true;
  strcpy(layer_3[2].symbol, ""); layer_3[2].highlighted = true;
  strcpy(layer_3[3].symbol, ""); layer_3[3].highlighted = true;
  strcpy(layer_3[4].symbol, "11"); layer_3[4].highlighted = true;


  draw_layer(cr, width, height, radius_so_far, 50, layer_3, false);

  radius_so_far += 50;


  cairo_show_page(cr);

  cairo_surface_destroy(surface);
  cairo_destroy(cr);

  return 0;
}

