#include <stdio.h>
#include <math.h>
// a_(n+1) = a_n + 1/(n+1)
int main (void) {
  double a = 1;
  for (int n = 1; n<=30; n++) {
    a = a + 1.0/(n + 1.0);
    printf("a=%.14e\n", a);
  }
  return 0;
}