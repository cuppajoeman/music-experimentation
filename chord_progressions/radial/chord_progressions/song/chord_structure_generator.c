#include "../../csg/drawing_service.h"

int main(void) 
{
  cairo_surface_t *surface;
  cairo_t *cr;

  int width = 2048, height = 2048;

  surface = cairo_pdf_surface_create("pdffile.pdf", width, height);
  cr = cairo_create(surface);

  draw_title(cr, width, height, "Song");
  sign_name(cr, width, height);

  // Drawing data
  // Useful vim regexs for creating data
  /*
   
  double mod and addition make sure it's positive
  '<,'>s/\[\(\d\+\)\]/\='[' .((submatch(1)-2)%12+12)%12. ']'/g
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

  draw_layer(cr, width, height, radius_so_far, 50, layer_N);

  radius_so_far += 50;
   
 */

  // ------ NEW LAYER ------
  struct sector layer_1[12];

  strcpy(layer_1[0].symbol, "0"); layer_1[0].highlighted = true;
  strcpy(layer_1[1].symbol, "1"); layer_1[1].highlighted = false;
  strcpy(layer_1[2].symbol, "2"); layer_1[2].highlighted = true;
  strcpy(layer_1[3].symbol, "3"); layer_1[3].highlighted = true;
  strcpy(layer_1[4].symbol, "4"); layer_1[4].highlighted = false;
  strcpy(layer_1[5].symbol, "5"); layer_1[5].highlighted = true;
  strcpy(layer_1[6].symbol, "6"); layer_1[6].highlighted = false;
  strcpy(layer_1[7].symbol, "7"); layer_1[7].highlighted = true;
  strcpy(layer_1[8].symbol, "8"); layer_1[8].highlighted = true;
  strcpy(layer_1[9].symbol, "9"); layer_1[9].highlighted = false;
  strcpy(layer_1[10].symbol, "10"); layer_1[10].highlighted = true;
  strcpy(layer_1[11].symbol, "11"); layer_1[11].highlighted = false;

  int radius_so_far = 100;

  draw_layer(cr, width, height, radius_so_far, 50, layer_1, true);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_2[12];

  strcpy(layer_2[3].symbol, "0"); layer_2[3].highlighted = true;
  strcpy(layer_2[4].symbol, ""); layer_2[4].highlighted = true;
  strcpy(layer_2[5].symbol, "2"); layer_2[5].highlighted = true;
  strcpy(layer_2[6].symbol, ""); layer_2[6].highlighted = true;
  strcpy(layer_2[7].symbol, ""); layer_2[7].highlighted = true;
  strcpy(layer_2[8].symbol, ""); layer_2[8].highlighted = true;
  strcpy(layer_2[9].symbol, ""); layer_2[9].highlighted = true;
  strcpy(layer_2[10].symbol, "7"); layer_2[10].highlighted = true;
  strcpy(layer_2[11].symbol, ""); layer_2[11].highlighted = true;
  strcpy(layer_2[0].symbol, ""); layer_2[0].highlighted = true;
  strcpy(layer_2[1].symbol, "10"); layer_2[1].highlighted = true;
  strcpy(layer_2[2].symbol, ""); layer_2[2].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_2, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_3[12];

  strcpy(layer_3[5].symbol, "0"); layer_3[5].highlighted = true;
  strcpy(layer_3[6].symbol, ""); layer_3[6].highlighted = true;
  strcpy(layer_3[7].symbol, "2"); layer_3[7].highlighted = true;
  strcpy(layer_3[8].symbol, "3"); layer_3[8].highlighted = true;
  strcpy(layer_3[9].symbol, ""); layer_3[9].highlighted = true;
  strcpy(layer_3[10].symbol, ""); layer_3[10].highlighted = true;
  strcpy(layer_3[11].symbol, ""); layer_3[11].highlighted = true;
  strcpy(layer_3[0].symbol, ""); layer_3[0].highlighted = true;
  strcpy(layer_3[1].symbol, ""); layer_3[1].highlighted = true;
  strcpy(layer_3[2].symbol, ""); layer_3[2].highlighted = true;
  strcpy(layer_3[3].symbol, "10"); layer_3[3].highlighted = true;
  strcpy(layer_3[4].symbol, ""); layer_3[4].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_3, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_4[12];

  strcpy(layer_4[8].symbol, "0"); layer_4[8].highlighted = true;
  strcpy(layer_4[9].symbol, ""); layer_4[9].highlighted = true;
  strcpy(layer_4[10].symbol, ""); layer_4[10].highlighted = true;
  strcpy(layer_4[11].symbol, ""); layer_4[11].highlighted = true;
  strcpy(layer_4[0].symbol, "4"); layer_4[0].highlighted = true;
  strcpy(layer_4[1].symbol, "5"); layer_4[1].highlighted = true;
  strcpy(layer_4[2].symbol, ""); layer_4[2].highlighted = true;
  strcpy(layer_4[3].symbol, ""); layer_4[3].highlighted = true;
  strcpy(layer_4[4].symbol, ""); layer_4[4].highlighted = true;
  strcpy(layer_4[5].symbol, "9"); layer_4[5].highlighted = true;
  strcpy(layer_4[6].symbol, ""); layer_4[6].highlighted = true;
  strcpy(layer_4[7].symbol, ""); layer_4[7].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_4, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_5[12];

  strcpy(layer_5[0].symbol, "0"); layer_5[0].highlighted = true;
  strcpy(layer_5[1].symbol, ""); layer_5[1].highlighted = true;
  strcpy(layer_5[2].symbol, "2"); layer_5[2].highlighted = true;
  strcpy(layer_5[3].symbol, ""); layer_5[3].highlighted = true;
  strcpy(layer_5[4].symbol, ""); layer_5[4].highlighted = true;
  strcpy(layer_5[5].symbol, "5"); layer_5[5].highlighted = true;
  strcpy(layer_5[6].symbol, ""); layer_5[6].highlighted = true;
  strcpy(layer_5[7].symbol, ""); layer_5[7].highlighted = true;
  strcpy(layer_5[8].symbol, "8"); layer_5[8].highlighted = true;
  strcpy(layer_5[9].symbol, ""); layer_5[9].highlighted = true;
  strcpy(layer_5[10].symbol, ""); layer_5[10].highlighted = true;
  strcpy(layer_5[11].symbol, ""); layer_5[11].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_5, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_6[12];

  strcpy(layer_6[3].symbol, "0"); layer_6[3].highlighted = true;
  strcpy(layer_6[4].symbol, ""); layer_6[4].highlighted = true;
  strcpy(layer_6[5].symbol, "2"); layer_6[5].highlighted = true;
  strcpy(layer_6[6].symbol, ""); layer_6[6].highlighted = true;
  strcpy(layer_6[7].symbol, ""); layer_6[7].highlighted = true;
  strcpy(layer_6[8].symbol, "5"); layer_6[8].highlighted = true;
  strcpy(layer_6[9].symbol, ""); layer_6[9].highlighted = true;
  strcpy(layer_6[10].symbol, ""); layer_6[10].highlighted = true;
  strcpy(layer_6[11].symbol, "8"); layer_6[11].highlighted = true;
  strcpy(layer_6[0].symbol, ""); layer_6[0].highlighted = true;
  strcpy(layer_6[1].symbol, ""); layer_6[1].highlighted = true;
  strcpy(layer_6[2].symbol, ""); layer_6[2].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_6, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_7[12];

  strcpy(layer_7[2].symbol, "0"); layer_7[2].highlighted = true;
  strcpy(layer_7[3].symbol, ""); layer_7[3].highlighted = true;
  strcpy(layer_7[4].symbol, ""); layer_7[4].highlighted = true;
  strcpy(layer_7[5].symbol, "3"); layer_7[5].highlighted = true;
  strcpy(layer_7[6].symbol, ""); layer_7[6].highlighted = true;
  strcpy(layer_7[7].symbol, ""); layer_7[7].highlighted = true;
  strcpy(layer_7[8].symbol, ""); layer_7[8].highlighted = true;
  strcpy(layer_7[9].symbol, "7"); layer_7[9].highlighted = true;
  strcpy(layer_7[10].symbol, "8"); layer_7[10].highlighted = true;
  strcpy(layer_7[11].symbol, ""); layer_7[11].highlighted = true;
  strcpy(layer_7[0].symbol, ""); layer_7[0].highlighted = true;
  strcpy(layer_7[1].symbol, ""); layer_7[1].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_7, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_8[12];

  strcpy(layer_8[2].symbol, "0"); layer_8[2].highlighted = true;
  strcpy(layer_8[3].symbol, ""); layer_8[3].highlighted = true;
  strcpy(layer_8[4].symbol, "2"); layer_8[4].highlighted = true;
  strcpy(layer_8[5].symbol, ""); layer_8[5].highlighted = true;
  strcpy(layer_8[6].symbol, ""); layer_8[6].highlighted = true;
  strcpy(layer_8[7].symbol, ""); layer_8[7].highlighted = true;
  strcpy(layer_8[8].symbol, ""); layer_8[8].highlighted = true;
  strcpy(layer_8[9].symbol, "7"); layer_8[9].highlighted = true;
  strcpy(layer_8[10].symbol, ""); layer_8[10].highlighted = true;
  strcpy(layer_8[11].symbol, ""); layer_8[11].highlighted = true;
  strcpy(layer_8[0].symbol, "10"); layer_8[0].highlighted = true;
  strcpy(layer_8[1].symbol, ""); layer_8[1].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_8, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_9[12];

  strcpy(layer_9[10].symbol, "0"); layer_9[10].highlighted = true;
  strcpy(layer_9[11].symbol, ""); layer_9[11].highlighted = true;
  strcpy(layer_9[0].symbol, "2"); layer_9[0].highlighted = true;
  strcpy(layer_9[1].symbol, ""); layer_9[1].highlighted = true;
  strcpy(layer_9[2].symbol, ""); layer_9[2].highlighted = true;
  strcpy(layer_9[3].symbol, "5"); layer_9[3].highlighted = true;
  strcpy(layer_9[4].symbol, ""); layer_9[4].highlighted = true;
  strcpy(layer_9[5].symbol, "7"); layer_9[5].highlighted = true;
  strcpy(layer_9[6].symbol, ""); layer_9[6].highlighted = true;
  strcpy(layer_9[7].symbol, "9"); layer_9[7].highlighted = true;
  strcpy(layer_9[8].symbol, ""); layer_9[8].highlighted = true;
  strcpy(layer_9[9].symbol, ""); layer_9[9].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_9, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_10[12];
  strcpy(layer_10[10].symbol, "0"); layer_10[10].highlighted = true;
  strcpy(layer_10[11].symbol, ""); layer_10[11].highlighted = true;
  strcpy(layer_10[0].symbol, "2"); layer_10[0].highlighted = true;
  strcpy(layer_10[1].symbol, ""); layer_10[1].highlighted = true;
  strcpy(layer_10[2].symbol, "4"); layer_10[2].highlighted = true;
  strcpy(layer_10[3].symbol, ""); layer_10[3].highlighted = true;
  strcpy(layer_10[4].symbol, ""); layer_10[4].highlighted = true;
  strcpy(layer_10[5].symbol, "8"); layer_10[5].highlighted = true;
  strcpy(layer_10[6].symbol, ""); layer_10[6].highlighted = true;
  strcpy(layer_10[7].symbol, ""); layer_10[7].highlighted = true;
  strcpy(layer_10[8].symbol, ""); layer_10[8].highlighted = true;
  strcpy(layer_10[9].symbol, ""); layer_10[9].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_10, false);

  radius_so_far += 50;

  // '<,'>s/\[\(\d\+\)\]/\='[' .((submatch(1)-2)%12+12)%12. ']'/g


  // cleanup
  cairo_show_page(cr);

  cairo_surface_destroy(surface);
  cairo_destroy(cr);

  return 0;
}

