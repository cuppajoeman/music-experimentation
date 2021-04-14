#include "../../csg/drawing_service.h"

int main(void) 
{
  cairo_surface_t *surface;
  cairo_t *cr;

  int width = 4096, height = 4096;

  surface = cairo_pdf_surface_create("pdffile.pdf", width, height);
  cr = cairo_create(surface);

  draw_title(cr, width, height, "Estate");
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

  int radius_so_far = 100;

  draw_layer(cr, width, height, radius_so_far, 50, base_layer, true);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_1[12];

  strcpy(layer_1[11].symbol, "0"); layer_1[11].highlighted = true;
  strcpy(layer_1[0].symbol, "1"); layer_1[0].highlighted = true;
  strcpy(layer_1[1].symbol, "2"); layer_1[1].highlighted = true;
  strcpy(layer_1[2].symbol, "3"); layer_1[2].highlighted = true;
  strcpy(layer_1[3].symbol, "4"); layer_1[3].highlighted = true;
  strcpy(layer_1[4].symbol, "5"); layer_1[4].highlighted = true;
  strcpy(layer_1[5].symbol, "6"); layer_1[5].highlighted = true;
  strcpy(layer_1[6].symbol, "7"); layer_1[6].highlighted = true;
  strcpy(layer_1[7].symbol, "8"); layer_1[7].highlighted = true;
  strcpy(layer_1[8].symbol, "9"); layer_1[8].highlighted = true;
  strcpy(layer_1[9].symbol, "10"); layer_1[9].highlighted = true;
  strcpy(layer_1[10].symbol, "11"); layer_1[10].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_1, false);

  radius_so_far += 50;


  // ------ NEW LAYER ------
  struct sector layer_2[12];

  strcpy(layer_2[4].symbol, "0"); layer_2[4].highlighted = true;
  strcpy(layer_2[5].symbol, ""); layer_2[5].highlighted = true;
  strcpy(layer_2[6].symbol, ""); layer_2[6].highlighted = true;
  strcpy(layer_2[7].symbol, "3"); layer_2[7].highlighted = true;
  strcpy(layer_2[8].symbol, ""); layer_2[8].highlighted = true;
  strcpy(layer_2[9].symbol, ""); layer_2[9].highlighted = true;
  strcpy(layer_2[10].symbol, ""); layer_2[10].highlighted = true;
  strcpy(layer_2[11].symbol, "7"); layer_2[11].highlighted = true;
  strcpy(layer_2[0].symbol, ""); layer_2[0].highlighted = true;
  strcpy(layer_2[1].symbol, ""); layer_2[1].highlighted = true;
  strcpy(layer_2[2].symbol, "10"); layer_2[2].highlighted = true;
  strcpy(layer_2[3].symbol, ""); layer_2[3].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_2, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_3[12];

  strcpy(layer_3[6].symbol, "0"); layer_3[6].highlighted = true;
  strcpy(layer_3[7].symbol, "1"); layer_3[7].highlighted = true;
  strcpy(layer_3[8].symbol, ""); layer_3[8].highlighted = true;
  strcpy(layer_3[9].symbol, ""); layer_3[9].highlighted = true;
  strcpy(layer_3[10].symbol, "4"); layer_3[10].highlighted = true;
  strcpy(layer_3[11].symbol, ""); layer_3[11].highlighted = true;
  strcpy(layer_3[0].symbol, ""); layer_3[0].highlighted = true;
  strcpy(layer_3[1].symbol, "7"); layer_3[1].highlighted = true;
  strcpy(layer_3[2].symbol, ""); layer_3[2].highlighted = true;
  strcpy(layer_3[3].symbol, ""); layer_3[3].highlighted = true;
  strcpy(layer_3[4].symbol, "10"); layer_3[4].highlighted = true;
  strcpy(layer_3[5].symbol, ""); layer_3[5].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_3, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_4[12];

  strcpy(layer_4[11].symbol, "0"); layer_4[11].highlighted = true;
  strcpy(layer_4[0].symbol, ""); layer_4[0].highlighted = true;
  strcpy(layer_4[1].symbol, ""); layer_4[1].highlighted = true;
  strcpy(layer_4[2].symbol, "3"); layer_4[2].highlighted = true;
  strcpy(layer_4[3].symbol, ""); layer_4[3].highlighted = true;
  strcpy(layer_4[4].symbol, ""); layer_4[4].highlighted = true;
  strcpy(layer_4[5].symbol, ""); layer_4[5].highlighted = true;
  strcpy(layer_4[6].symbol, "7"); layer_4[6].highlighted = true;
  strcpy(layer_4[7].symbol, ""); layer_4[7].highlighted = true;
  strcpy(layer_4[8].symbol, ""); layer_4[8].highlighted = true;
  strcpy(layer_4[9].symbol, "10"); layer_4[9].highlighted = true;
  strcpy(layer_4[10].symbol, ""); layer_4[10].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_4, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_5[12];

  strcpy(layer_5[4].symbol, "0"); layer_5[4].highlighted = true;
  strcpy(layer_5[5].symbol, ""); layer_5[5].highlighted = true;
  strcpy(layer_5[6].symbol, ""); layer_5[6].highlighted = true;
  strcpy(layer_5[7].symbol, "3"); layer_5[7].highlighted = true;
  strcpy(layer_5[8].symbol, ""); layer_5[8].highlighted = true;
  strcpy(layer_5[9].symbol, ""); layer_5[9].highlighted = true;
  strcpy(layer_5[10].symbol, ""); layer_5[10].highlighted = true;
  strcpy(layer_5[11].symbol, "7"); layer_5[11].highlighted = true;
  strcpy(layer_5[0].symbol, ""); layer_5[0].highlighted = true;
  strcpy(layer_5[1].symbol, ""); layer_5[1].highlighted = true;
  strcpy(layer_5[2].symbol, "10"); layer_5[2].highlighted = true;
  strcpy(layer_5[3].symbol, ""); layer_5[3].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_5, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_6[12];

  strcpy(layer_6[9].symbol, "0"); layer_6[9].highlighted = true;
  strcpy(layer_6[10].symbol, ""); layer_6[10].highlighted = true;
  strcpy(layer_6[11].symbol, ""); layer_6[11].highlighted = true;
  strcpy(layer_6[0].symbol, ""); layer_6[0].highlighted = true;
  strcpy(layer_6[1].symbol, "4"); layer_6[1].highlighted = true;
  strcpy(layer_6[2].symbol, ""); layer_6[2].highlighted = true;
  strcpy(layer_6[3].symbol, ""); layer_6[3].highlighted = true;
  strcpy(layer_6[4].symbol, "7"); layer_6[4].highlighted = true;
  strcpy(layer_6[5].symbol, ""); layer_6[5].highlighted = true;
  strcpy(layer_6[6].symbol, ""); layer_6[6].highlighted = true;
  strcpy(layer_6[7].symbol, "10"); layer_6[7].highlighted = true;
  strcpy(layer_6[8].symbol, ""); layer_6[8].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_6, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_7[12];

  strcpy(layer_7[2].symbol, "0"); layer_7[2].highlighted = true;
  strcpy(layer_7[3].symbol, ""); layer_7[3].highlighted = true;
  strcpy(layer_7[4].symbol, ""); layer_7[4].highlighted = true;
  strcpy(layer_7[5].symbol, ""); layer_7[5].highlighted = true;
  strcpy(layer_7[6].symbol, ""); layer_7[6].highlighted = true;
  strcpy(layer_7[7].symbol, "5"); layer_7[7].highlighted = true;
  strcpy(layer_7[8].symbol, ""); layer_7[8].highlighted = true;
  strcpy(layer_7[9].symbol, "7"); layer_7[9].highlighted = true;
  strcpy(layer_7[10].symbol, ""); layer_7[10].highlighted = true;
  strcpy(layer_7[11].symbol, ""); layer_7[11].highlighted = true;
  strcpy(layer_7[0].symbol, "10"); layer_7[0].highlighted = true;
  strcpy(layer_7[1].symbol, ""); layer_7[1].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_7, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_8[12];

  strcpy(layer_8[2].symbol, "0"); layer_8[2].highlighted = true;
  strcpy(layer_8[3].symbol, ""); layer_8[3].highlighted = true;
  strcpy(layer_8[4].symbol, ""); layer_8[4].highlighted = true;
  strcpy(layer_8[5].symbol, "3"); layer_8[5].highlighted = true;
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

  strcpy(layer_9[7].symbol, "0"); layer_9[7].highlighted = true;
  strcpy(layer_9[8].symbol, ""); layer_9[8].highlighted = true;
  strcpy(layer_9[9].symbol, ""); layer_9[9].highlighted = true;
  strcpy(layer_9[10].symbol, ""); layer_9[10].highlighted = true;
  strcpy(layer_9[11].symbol, "4"); layer_9[11].highlighted = true;
  strcpy(layer_9[0].symbol, ""); layer_9[0].highlighted = true;
  strcpy(layer_9[1].symbol, ""); layer_9[1].highlighted = true;
  strcpy(layer_9[2].symbol, "7"); layer_9[2].highlighted = true;
  strcpy(layer_9[3].symbol, ""); layer_9[3].highlighted = true;
  strcpy(layer_9[4].symbol, ""); layer_9[4].highlighted = true;
  strcpy(layer_9[5].symbol, ""); layer_9[5].highlighted = true;
  strcpy(layer_9[6].symbol, "11"); layer_9[6].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_9, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_10[12];

  strcpy(layer_10[6].symbol, "0"); layer_10[6].highlighted = true;
  strcpy(layer_10[7].symbol, ""); layer_10[7].highlighted = true;
  strcpy(layer_10[8].symbol, ""); layer_10[8].highlighted = true;
  strcpy(layer_10[9].symbol, ""); layer_10[9].highlighted = true;
  strcpy(layer_10[10].symbol, "4"); layer_10[10].highlighted = true;
  strcpy(layer_10[11].symbol, ""); layer_10[11].highlighted = true;
  strcpy(layer_10[0].symbol, ""); layer_10[0].highlighted = true;
  strcpy(layer_10[1].symbol, "7"); layer_10[1].highlighted = true;
  strcpy(layer_10[2].symbol, ""); layer_10[2].highlighted = true;
  strcpy(layer_10[3].symbol, ""); layer_10[3].highlighted = true;
  strcpy(layer_10[4].symbol, "10"); layer_10[4].highlighted = true;
  strcpy(layer_10[5].symbol, ""); layer_10[5].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_10, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_11[12];

  strcpy(layer_11[6].symbol, "0"); layer_11[6].highlighted = true;
  strcpy(layer_11[7].symbol, ""); layer_11[7].highlighted = true;
  strcpy(layer_11[8].symbol, ""); layer_11[8].highlighted = true;
  strcpy(layer_11[9].symbol, ""); layer_11[9].highlighted = true;
  strcpy(layer_11[10].symbol, "4"); layer_11[10].highlighted = true;
  strcpy(layer_11[11].symbol, ""); layer_11[11].highlighted = true;
  strcpy(layer_11[0].symbol, ""); layer_11[0].highlighted = true;
  strcpy(layer_11[1].symbol, ""); layer_11[1].highlighted = true;
  strcpy(layer_11[2].symbol, "8"); layer_11[2].highlighted = true;
  strcpy(layer_11[3].symbol, ""); layer_11[3].highlighted = true;
  strcpy(layer_11[4].symbol, "10"); layer_11[4].highlighted = true;
  strcpy(layer_11[5].symbol, ""); layer_11[5].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_11, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_12[12];

  strcpy(layer_12[11].symbol, "0"); layer_12[11].highlighted = true;
  strcpy(layer_12[0].symbol, ""); layer_12[0].highlighted = true;
  strcpy(layer_12[1].symbol, ""); layer_12[1].highlighted = true;
  strcpy(layer_12[2].symbol, ""); layer_12[2].highlighted = true;
  strcpy(layer_12[3].symbol, "4"); layer_12[3].highlighted = true;
  strcpy(layer_12[4].symbol, ""); layer_12[4].highlighted = true;
  strcpy(layer_12[5].symbol, ""); layer_12[5].highlighted = true;
  strcpy(layer_12[6].symbol, "7"); layer_12[6].highlighted = true;
  strcpy(layer_12[7].symbol, ""); layer_12[7].highlighted = true;
  strcpy(layer_12[8].symbol, ""); layer_12[8].highlighted = true;
  strcpy(layer_12[9].symbol, ""); layer_12[9].highlighted = true;
  strcpy(layer_12[10].symbol, "11"); layer_12[10].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_12, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_13[12];

  strcpy(layer_13[5].symbol, "0"); layer_13[5].highlighted = true;
  strcpy(layer_13[6].symbol, ""); layer_13[6].highlighted = true;
  strcpy(layer_13[7].symbol, ""); layer_13[7].highlighted = true;
  strcpy(layer_13[8].symbol, "3"); layer_13[8].highlighted = true;
  strcpy(layer_13[9].symbol, ""); layer_13[9].highlighted = true;
  strcpy(layer_13[10].symbol, ""); layer_13[10].highlighted = true;
  strcpy(layer_13[11].symbol, "6"); layer_13[11].highlighted = true;
  strcpy(layer_13[0].symbol, ""); layer_13[0].highlighted = true;
  strcpy(layer_13[1].symbol, ""); layer_13[1].highlighted = true;
  strcpy(layer_13[2].symbol, ""); layer_13[2].highlighted = true;
  strcpy(layer_13[3].symbol, "10"); layer_13[3].highlighted = true;
  strcpy(layer_13[4].symbol, ""); layer_13[4].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_13, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_14[12];

  strcpy(layer_14[10].symbol, "0"); layer_14[10].highlighted = true;
  strcpy(layer_14[11].symbol, "1"); layer_14[11].highlighted = true;
  strcpy(layer_14[0].symbol, ""); layer_14[0].highlighted = true;
  strcpy(layer_14[1].symbol, ""); layer_14[1].highlighted = true;
  strcpy(layer_14[2].symbol, "4"); layer_14[2].highlighted = true;
  strcpy(layer_14[3].symbol, ""); layer_14[3].highlighted = true;
  strcpy(layer_14[4].symbol, ""); layer_14[4].highlighted = true;
  strcpy(layer_14[5].symbol, "7"); layer_14[5].highlighted = true;
  strcpy(layer_14[6].symbol, ""); layer_14[6].highlighted = true;
  strcpy(layer_14[7].symbol, ""); layer_14[7].highlighted = true;
  strcpy(layer_14[8].symbol, "10"); layer_14[8].highlighted = true;
  strcpy(layer_14[9].symbol, ""); layer_14[9].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_14, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_15[12];

  strcpy(layer_15[3].symbol, "0"); layer_15[3].highlighted = true;
  strcpy(layer_15[4].symbol, ""); layer_15[4].highlighted = true;
  strcpy(layer_15[5].symbol, ""); layer_15[5].highlighted = true;
  strcpy(layer_15[6].symbol, "3"); layer_15[6].highlighted = true;
  strcpy(layer_15[7].symbol, ""); layer_15[7].highlighted = true;
  strcpy(layer_15[8].symbol, ""); layer_15[8].highlighted = true;
  strcpy(layer_15[9].symbol, ""); layer_15[9].highlighted = true;
  strcpy(layer_15[10].symbol, "7"); layer_15[10].highlighted = true;
  strcpy(layer_15[11].symbol, ""); layer_15[11].highlighted = true;
  strcpy(layer_15[0].symbol, ""); layer_15[0].highlighted = true;
  strcpy(layer_15[1].symbol, "10"); layer_15[1].highlighted = true;
  strcpy(layer_15[2].symbol, ""); layer_15[2].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_15, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_16[12];

  strcpy(layer_16[8].symbol, "0"); layer_16[8].highlighted = true;
  strcpy(layer_16[9].symbol, "1"); layer_16[9].highlighted = true;
  strcpy(layer_16[10].symbol, ""); layer_16[10].highlighted = true;
  strcpy(layer_16[11].symbol, ""); layer_16[11].highlighted = true;
  strcpy(layer_16[0].symbol, "4"); layer_16[0].highlighted = true;
  strcpy(layer_16[1].symbol, ""); layer_16[1].highlighted = true;
  strcpy(layer_16[2].symbol, ""); layer_16[2].highlighted = true;
  strcpy(layer_16[3].symbol, "7"); layer_16[3].highlighted = true;
  strcpy(layer_16[4].symbol, ""); layer_16[4].highlighted = true;
  strcpy(layer_16[5].symbol, ""); layer_16[5].highlighted = true;
  strcpy(layer_16[6].symbol, "10"); layer_16[6].highlighted = true;
  strcpy(layer_16[7].symbol, ""); layer_16[7].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_16, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_17[12];

  strcpy(layer_17[4].symbol, "0"); layer_17[4].highlighted = true;
  strcpy(layer_17[5].symbol, "1"); layer_17[5].highlighted = true;
  strcpy(layer_17[6].symbol, ""); layer_17[6].highlighted = true;
  strcpy(layer_17[7].symbol, ""); layer_17[7].highlighted = true;
  strcpy(layer_17[8].symbol, "4"); layer_17[8].highlighted = true;
  strcpy(layer_17[9].symbol, ""); layer_17[9].highlighted = true;
  strcpy(layer_17[10].symbol, ""); layer_17[10].highlighted = true;
  strcpy(layer_17[11].symbol, "7"); layer_17[11].highlighted = true;
  strcpy(layer_17[0].symbol, ""); layer_17[0].highlighted = true;
  strcpy(layer_17[1].symbol, ""); layer_17[1].highlighted = true;
  strcpy(layer_17[2].symbol, "10"); layer_17[2].highlighted = true;
  strcpy(layer_17[3].symbol, ""); layer_17[3].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_17, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_18[12];

  strcpy(layer_18[9].symbol, "0"); layer_18[9].highlighted = true;
  strcpy(layer_18[10].symbol, ""); layer_18[10].highlighted = true;
  strcpy(layer_18[11].symbol, ""); layer_18[11].highlighted = true;
  strcpy(layer_18[0].symbol, ""); layer_18[0].highlighted = true;
  strcpy(layer_18[1].symbol, "4"); layer_18[1].highlighted = true;
  strcpy(layer_18[2].symbol, ""); layer_18[2].highlighted = true;
  strcpy(layer_18[3].symbol, ""); layer_18[3].highlighted = true;
  strcpy(layer_18[4].symbol, "7"); layer_18[4].highlighted = true;
  strcpy(layer_18[5].symbol, ""); layer_18[5].highlighted = true;
  strcpy(layer_18[6].symbol, ""); layer_18[6].highlighted = true;
  strcpy(layer_18[7].symbol, "10"); layer_18[7].highlighted = true;
  strcpy(layer_18[8].symbol, ""); layer_18[8].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_18, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_19[12];

  strcpy(layer_19[2].symbol, "0"); layer_19[2].highlighted = true;
  strcpy(layer_19[3].symbol, ""); layer_19[3].highlighted = true;
  strcpy(layer_19[4].symbol, ""); layer_19[4].highlighted = true;
  strcpy(layer_19[5].symbol, ""); layer_19[5].highlighted = true;
  strcpy(layer_19[6].symbol, ""); layer_19[6].highlighted = true;
  strcpy(layer_19[7].symbol, "5"); layer_19[7].highlighted = true;
  strcpy(layer_19[8].symbol, ""); layer_19[8].highlighted = true;
  strcpy(layer_19[9].symbol, "7"); layer_19[9].highlighted = true;
  strcpy(layer_19[10].symbol, ""); layer_19[10].highlighted = true;
  strcpy(layer_19[11].symbol, ""); layer_19[11].highlighted = true;
  strcpy(layer_19[0].symbol, "10"); layer_19[0].highlighted = true;
  strcpy(layer_19[1].symbol, ""); layer_19[1].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_19, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_20[12];

  strcpy(layer_20[2].symbol, "0"); layer_20[2].highlighted = true;
  strcpy(layer_20[3].symbol, ""); layer_20[3].highlighted = true;
  strcpy(layer_20[4].symbol, ""); layer_20[4].highlighted = true;
  strcpy(layer_20[5].symbol, "3"); layer_20[5].highlighted = true;
  strcpy(layer_20[6].symbol, ""); layer_20[6].highlighted = true;
  strcpy(layer_20[7].symbol, ""); layer_20[7].highlighted = true;
  strcpy(layer_20[8].symbol, ""); layer_20[8].highlighted = true;
  strcpy(layer_20[9].symbol, "7"); layer_20[9].highlighted = true;
  strcpy(layer_20[10].symbol, ""); layer_20[10].highlighted = true;
  strcpy(layer_20[11].symbol, ""); layer_20[11].highlighted = true;
  strcpy(layer_20[0].symbol, "10"); layer_20[0].highlighted = true;
  strcpy(layer_20[1].symbol, ""); layer_20[1].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_20, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_21[12];

  strcpy(layer_21[7].symbol, "0"); layer_21[7].highlighted = true;
  strcpy(layer_21[8].symbol, ""); layer_21[8].highlighted = true;
  strcpy(layer_21[9].symbol, ""); layer_21[9].highlighted = true;
  strcpy(layer_21[10].symbol, ""); layer_21[10].highlighted = true;
  strcpy(layer_21[11].symbol, "4"); layer_21[11].highlighted = true;
  strcpy(layer_21[0].symbol, ""); layer_21[0].highlighted = true;
  strcpy(layer_21[1].symbol, ""); layer_21[1].highlighted = true;
  strcpy(layer_21[2].symbol, "7"); layer_21[2].highlighted = true;
  strcpy(layer_21[3].symbol, ""); layer_21[3].highlighted = true;
  strcpy(layer_21[4].symbol, ""); layer_21[4].highlighted = true;
  strcpy(layer_21[5].symbol, ""); layer_21[5].highlighted = true;
  strcpy(layer_21[6].symbol, "11"); layer_21[6].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_21, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_22[12];

  strcpy(layer_22[6].symbol, "0"); layer_22[6].highlighted = true;
  strcpy(layer_22[7].symbol, ""); layer_22[7].highlighted = true;
  strcpy(layer_22[8].symbol, ""); layer_22[8].highlighted = true;
  strcpy(layer_22[9].symbol, ""); layer_22[9].highlighted = true;
  strcpy(layer_22[10].symbol, "4"); layer_22[10].highlighted = true;
  strcpy(layer_22[11].symbol, ""); layer_22[11].highlighted = true;
  strcpy(layer_22[0].symbol, ""); layer_22[0].highlighted = true;
  strcpy(layer_22[1].symbol, "7"); layer_22[1].highlighted = true;
  strcpy(layer_22[2].symbol, ""); layer_22[2].highlighted = true;
  strcpy(layer_22[3].symbol, ""); layer_22[3].highlighted = true;
  strcpy(layer_22[4].symbol, "10"); layer_22[4].highlighted = true;
  strcpy(layer_22[5].symbol, ""); layer_22[5].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_22, false);

  radius_so_far += 50;

  // ------ NEW LAYER ------
  struct sector layer_23[12];

  strcpy(layer_23[6].symbol, "0"); layer_23[6].highlighted = true;
  strcpy(layer_23[7].symbol, ""); layer_23[7].highlighted = true;
  strcpy(layer_23[8].symbol, ""); layer_23[8].highlighted = true;
  strcpy(layer_23[9].symbol, ""); layer_23[9].highlighted = true;
  strcpy(layer_23[10].symbol, "4"); layer_23[10].highlighted = true;
  strcpy(layer_23[11].symbol, ""); layer_23[11].highlighted = true;
  strcpy(layer_23[0].symbol, ""); layer_23[0].highlighted = true;
  strcpy(layer_23[1].symbol, ""); layer_23[1].highlighted = true;
  strcpy(layer_23[2].symbol, "8"); layer_23[2].highlighted = true;
  strcpy(layer_23[3].symbol, ""); layer_23[3].highlighted = true;
  strcpy(layer_23[4].symbol, "10"); layer_23[4].highlighted = true;
  strcpy(layer_23[5].symbol, ""); layer_23[5].highlighted = true;

  draw_layer(cr, width, height, radius_so_far, 50, layer_23, false);

  radius_so_far += 50;




  // cleanup
  cairo_show_page(cr);

  cairo_surface_destroy(surface);
  cairo_destroy(cr);

  return 0;
}

