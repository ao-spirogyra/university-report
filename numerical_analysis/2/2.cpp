#include <stdio.h>
#include <math.h>
int main (void) {
  double x = pow(10,20);
  double a = sqrt(x+1)-sqrt(x);
  double b = 1/(sqrt(x+1)+sqrt(x));
  printf("%.1e\n",a);
  printf("%.1e\n",b);
  return 0;
}