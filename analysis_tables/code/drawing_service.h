#include <cairo.h>
#include <math.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>     /* strtol */
#include <string.h>
#include <cairo-pdf.h>

#ifndef SECTOR_H
#define SECTOR_H

struct chord {
  int root_tone;
  int *intervals;
  int num_intervals;
};

struct sector {
  char symbol[3];
  bool highlighted;
  double red;
  double green;
  double blue;
};

#endif 


int min(int x, int y);

void trace_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12]);

void highlight_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12]);

void draw_base_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12], int root_tone, int *sequence, int seq_len);

void draw_chord_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12], struct chord chord);

void draw_title(cairo_t *cr, int width, int height, char *title);

void sign_name(cairo_t *cr, int width, int height);

void setup_layer_colors(struct sector sectors[12]);

void construct_sectors_from_chord(struct sector sectors[12], struct chord chord);

void setup_base_layer_colors(struct sector sectors[12], int root_tone, int *sequence, int seq_len);

void construct_sectors_all_notes(struct sector sectors[12]);
