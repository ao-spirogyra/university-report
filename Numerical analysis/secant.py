import math
from decimal import *
# あとでDecoratorを使っていい感じにする
class Secant():
  getcontext().prec = 12
  def __init__(self,residual,format):
    self.residual = residual
    self.format = format
  def approximate(self,initial_x,second_x,max_n):
    x = [initial_x,second_x]
    for i in range(max_n-1):
      x.append(x[i+1]-self.f_x(x[i+1])*((x[i+1]-x[i])/self.f_x(x[i+1])-self.f_x(x[i])))
      if self.checkResidual(x[i+2]):
        print(x[i+2])
        break
  def changeFormat(self,value):
    if (self.format == '.12e'):
      return '{.12e}'.format(value)
  def f_x(self,xnum):
    return (math.e)**(xnum)-(5)*(xnum)
  def checkResidual(self,function_x):
    if (function_x < self.residual):
      return True
    else:
      return False
    
if __name__ == '__main__':
  secant = Secant(1*(10^(-12)),'.12e')
  secant.approximate(-2,-1,50)