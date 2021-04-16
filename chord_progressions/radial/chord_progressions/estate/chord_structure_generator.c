#include "drawing_service.h"
#include "dynamic_array.h"

int main(void) 
{
  cairo_surface_t *surface;
  cairo_t *cr;

  int width = 4096, height = 4096;

  surface = cairo_pdf_surface_create("pdffile.pdf", width, height);
  cr = cairo_create(surface);

  draw_title(cr, width, height, "Estate");
  sign_name(cr, width, height);

  double start_radius = 100;
  double layer_width = 50;
  double layer_gap_size = 10;
  double radius_so_far = start_radius;

  DynamicArray changes;

  init_darray(&changes, 1, sizeof(struct chord*));

  // Useful regex
  // '<,'>s/s.\{-}rd \(.\{-}\) .*/insert_darray(\&changes, \&\1);

  struct chord Bm7 = {11, (int[]){0, 3, 7, 10}, 4};
  struct chord Em7 = {4, (int[]){0, 3, 7, 10}, 4};
  struct chord Fs7b9 = {6, (int[]){0, 1, 4, 7, 10}, 5};
  struct chord A7 = {9, (int[]){0, 4, 7, 10}, 4};
  struct chord D7sus = {2, (int[]){0, 5, 7, 10}, 4};
  struct chord Dm7 = {2, (int[]){0, 3, 7, 10}, 4};
  struct chord GM7 = {7, (int[]){0, 4, 7, 11}, 4};
  struct chord Fs7 = {6, (int[]){0,  4, 7, 10}, 4};
  struct chord Fs7s5 = {6, (int[]){0,  4, 8, 10}, 4};
  struct chord BM7 = {11, (int[]){0, 4, 7, 11}, 4};
  struct chord Fhd7 = {5, (int[]){0, 3, 6, 10}, 4};
  struct chord Bb7b9 = {10, (int[]){0, 1, 4, 7, 10}, 5};
  struct chord Ebm7 = {3, (int[]){0, 3, 7, 10}, 4};
  struct chord Ab7b9 = {8, (int[]){0, 1, 4, 7, 10}, 5};

  insert_darray(&changes, &Bm7);
  insert_darray(&changes, &Em7);
  insert_darray(&changes, &Fs7b9);

  insert_darray(&changes, &Bm7);
  insert_darray(&changes, &Em7);
  insert_darray(&changes, &A7);

  insert_darray(&changes, &D7sus);
  insert_darray(&changes, &Dm7);
  insert_darray(&changes, &GM7);

  insert_darray(&changes, &Fs7);
  insert_darray(&changes, &Fs7s5);

  insert_darray(&changes, &BM7);
  insert_darray(&changes, &Fhd7);
  insert_darray(&changes, &Bb7b9);

  insert_darray(&changes, &Ebm7);
  insert_darray(&changes, &Ab7b9);
  insert_darray(&changes, &Em7);
  insert_darray(&changes, &A7);

  insert_darray(&changes, &D7sus);
  insert_darray(&changes, &Dm7);
  insert_darray(&changes, &GM7);

  insert_darray(&changes, &Fs7);
  insert_darray(&changes, &Fs7s5);


  
  // Setup Base Layer

  struct sector base_layer[12];

  int sequence[] = {2,2,1,2,2,2,1};

  construct_sectors_all_notes(base_layer);

  draw_base_layer(cr, width, height, radius_so_far, layer_width, base_layer, 0, sequence, 7);

  radius_so_far += layer_width + layer_gap_size;

  // Add in chord changes
  
  for (int i  = 0; i < changes.used; i++) {
    struct chord *curr_chord_ptr;
    struct sector chord_layer[12];
    at(&changes, &curr_chord_ptr, i);
    struct chord curr_chord = * ((struct chord *) curr_chord_ptr);
    draw_chord_layer(cr, width, height, radius_so_far, layer_width, chord_layer, curr_chord);
    radius_so_far += layer_width + layer_gap_size;
  }

  free_darray(&changes);

  cairo_show_page(cr);

  cairo_surface_destroy(surface);
  cairo_destroy(cr);

  return 0;
}

