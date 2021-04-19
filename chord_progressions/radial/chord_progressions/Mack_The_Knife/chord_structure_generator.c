#include "../../csg/drawing_service.h"
#include "../../csg/dynamic_array.h"

int main(void) 
{
  cairo_surface_t *surface;
  cairo_t *cr;

  int scale = 2;

  int width = scale * 1024, height = scale * 1024;

  surface = cairo_pdf_surface_create("Enter File Name.pdf", width, height);
  cr = cairo_create(surface);

  draw_title(cr, width, height, "Enter Title");
  sign_name(cr, width, height);

  // Start drawing

  double start_radius = 100;
  double layer_width = 50;
  double layer_gap_size = 10;
  double radius_so_far = start_radius;

  // Setup Base Layer

  struct sector base_layer[12];

  int sequence[] = {2,2,1,2,2,2,1};

  construct_sectors_all_notes(base_layer);

  draw_base_layer(cr, width, height, radius_so_far, layer_width, base_layer, 10, sequence, 7);

  radius_so_far += layer_width + layer_gap_size;
  
  // Chord Changes
  
  // Useful regex
  // '<,'>s/s.\{-}rd \(.\{-}\) .*/insert_darray(\&changes, \&\1);

  DynamicArray changes;

  init_darray(&changes, 1, sizeof(struct chord*));

  insert_darray(&changes, &((struct chord){10, (int[]){0, 4, 6, 9}, 4}));
  insert_darray(&changes, &((struct chord){0, (int[]){0, 3, 7, 10}, 4}));
  insert_darray(&changes, &((struct chord){5, (int[]){0, 4, 7, 10}, 4}));

  insert_darray(&changes, &((struct chord){10, (int[]){0, 4, 6, 9}, 4}));
  insert_darray(&changes, &((struct chord){7, (int[]){0, 3, 7, 10}, 4}));
  insert_darray(&changes, &((struct chord){0, (int[]){0, 3, 7, 10}, 4}));

  insert_darray(&changes, &((struct chord){5, (int[]){0, 4, 7, 10}, 4}));
  insert_darray(&changes, &((struct chord){10, (int[]){0, 4, 6, 9}, 4}));

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

