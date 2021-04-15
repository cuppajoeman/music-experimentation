#include "drawing_service.h"

int main(void) 
{
  cairo_surface_t *surface;
  cairo_t *cr;

  int width = 1024, height = 1024;

  surface = cairo_pdf_surface_create("pdffile.pdf", width, height);
  cr = cairo_create(surface);

  draw_title(cr, width, height, "A 2 5 1 or (2 7 0) chord progression moving radially outward.");
  sign_name(cr, width, height);



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
  double radius_so_far = 150;

  struct sector base_layer[12];

  int sequence[] = {2,2,1,2,2,2,1};

  construct_sectors_all_notes(base_layer);

  draw_base_layer(cr, width, height, radius_so_far, 50, base_layer, 0, sequence, 7);

  radius_so_far += 60;

  struct sector layer_1[12];

  struct chord Dm7 = {2, (int[]){0, 3, 7, 10}, 4};

  draw_chord_layer(cr, width, height, radius_so_far, 50, layer_1, Dm7);

  radius_so_far += 60;

  //struct sector layer_2[12];

  //int intervals_2[] = {0, 3, 7, 10};

  //construct_sectors_from_chord(layer_2, 2, intervals_2, 4);

  //draw_chord_layer(cr, width, height, radius_so_far, 50, layer_2);

  //radius_so_far += 60;

  cairo_show_page(cr);

  cairo_surface_destroy(surface);
  cairo_destroy(cr);

  return 0;
}

