#include <stdio.h>
int main (void) {
  double epsilon = 1.0;
  while (1+ epsilon != 1) {
    epsilon = epsilon/2.0;
  }
  epsilon = epsilon*2;
  double a = 1+(1*epsilon)/2;
  double b = 1+(1*epsilon)/3;
  double c = 2-(1*epsilon)/2;
  printf("%.16e\n", epsilon);
  printf("%.16e\n",a);
  printf("%.16e\n",b);
  printf("%.16e\n",c);

  return 0;
}