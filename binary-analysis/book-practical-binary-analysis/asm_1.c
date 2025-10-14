#include <stdio.h>

typedef struct ValidDTO {
  int value_one;
  int value_two;
} ValidDTO;

int main(int argc, char *argv[])
{
    ValidDTO some_struct = {.value_one = 123, .value_two = 321};
    printf("Hello, world!\n");
    printf("%d", some_struct);
    return 0;
}

