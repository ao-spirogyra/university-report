#include <stdio.h>
#include <math.h>
int main (void) {
  double a = pow(10,45) + 123.4 - pow(10,45) - pow(10,35) + 432.1 + pow(10,35);
  double b = 123.4 + 432.1 + pow(10,45) - pow(10,45) - pow(10,35) + pow(10,35);
  double c = pow(10,45) - pow(10,45) - pow(10,35) + pow(10,35) + 123.4 + 432.1;
  double d = pow(10,45) - pow(10,35) - pow(10,45) + pow(10,35) + 123.4 + 432.1;
  printf("%.1e\n",a);
  printf("%.1e\n",b);
  printf("%.1e\n",c);
  printf("%.1e\n",d);
  return 0;
}