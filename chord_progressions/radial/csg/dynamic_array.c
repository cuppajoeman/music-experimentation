#include "dynamic_array.h"
#include <stdlib.h>
#include <string.h>

void init_darray(DynamicArray *a, size_t initial_length, size_t elem_size) {
  a->elem_size = elem_size;
  a->static_array = malloc(initial_length * elem_size);
  a->used = 0;
  a->length = initial_length;
}

void insert_darray(DynamicArray *a, void *element) {
    // a->used is the number of used entries, because a->static_array[a->used++] updates a->used only *after* the array has been accessed.
    // Therefore a->used can go up to a->size 
    if (a->used == a->length) {
        a->length *= 2;
        a->static_array = realloc(a->static_array, a->length * a->elem_size);
    }
    a->static_array[a->used++] = element;
}
    
void free_darray(DynamicArray *a) {
  free(a->static_array);
  a->static_array = NULL;
  a->used = a->length = 0;
}

void at(DynamicArray *a, void *elem, size_t i) {
  // this lets you memcpy the indexed element back to
  memcpy(elem, a->static_array + a->elem_size * i, a->elem_size);
}
