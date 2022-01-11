#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct Item {
    char *code;
    char *description;
    bool valid;
} Item;

typedef struct Payload {
    Item *items[];
    char *service;
    char *requestId;
} Payload;
