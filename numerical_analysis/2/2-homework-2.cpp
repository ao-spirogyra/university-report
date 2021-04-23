#include <stdio.h>
#include <math.h>
int main (void) {
  double x = pow(10,-7);
  double f = (1-cos(x))/pow(x,2);
  double f2 = (2*pow(sin(x/2),2)+1/pow(x,2));
  printf("(1-cos(x))/x^2= %.16e\n", f);
  printf("2*sin^2(x/2)+1/x^2= %.16e\n", f2);
  return 0;
}