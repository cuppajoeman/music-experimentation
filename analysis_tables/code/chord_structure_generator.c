#include "drawing_service.h"
#include "dynamic_array.h"

int main(void) 
{
  cairo_surface_t *surface;
  cairo_t *cr;

  int width = 1024, height = 1024;

  surface = cairo_pdf_surface_create("pdffile.pdf", width, height);
  cr = cairo_create(surface);

  draw_title(cr, width, height, "A 2 5 1 or (2 7 0) chord progression moving radially outward.");
  sign_name(cr, width, height);

  double start_radius = 100;
  double layer_width = 50;
  double layer_gap_size = 10;
  double radius_so_far = start_radius;

  DynamicArray changes;

  init_darray(&changes, 1, sizeof(struct chord*));

  struct chord Dm7 = {2, (int[]){0, 3, 7, 10}, 4};
  struct chord G7 = {7, (int[]){0, 4, 7, 10}, 4};
  struct chord CM7 = {0, (int[]){0, 4, 7, 11}, 4};
  struct chord BLANK = {0, (int[]){}, 0};
  struct chord single = {3, (int[]){0}, 1};

  insert_darray(&changes, &Dm7);
  insert_darray(&changes, &G7);
  insert_darray(&changes, &CM7);
  insert_darray(&changes, &BLANK);
  
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

