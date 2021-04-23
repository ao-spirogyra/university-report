#include <stdio.h>
int main (void) {
  double a = 1.1;
  double b = 1.2;
  double c = 1.3;
  printf("左辺=%.16e\n", (a+b)+c);
  printf("右辺=%.16e\n", a+(b+c));
  return 0;
}