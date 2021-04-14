#include <cairo.h>
#include <math.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>     /* strtol */
#include <string.h>
#include <cairo-pdf.h>

#ifndef SECTOR_H
#define SECTOR_H

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

void highlight_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12], bool single_color);

void draw_layer(cairo_t *cr, int width, int height, double start_radius, double layer_width, struct sector sectors[12], bool single_color);

void draw_title(cairo_t *cr, int width, int height, char *title);

void sign_name(cairo_t *cr, int width, int height);

void setup_layer_colors(struct sector sectors[12]);
