import math
from decimal import *
# あとでDecoratorを使っていい感じにする
class Secant():
  getcontext().prec = 12
  def __init__(self):
  
  def approximate(self,initial_x,second_x,*func,**max_n):
    def wrapper(*args):
      x = [initial_x,second_x]
      for i in range(max_n-1):
        x.append(x[i+1]-self.f_x(x[i+1])*((x[i+1]-x[i])/self.f_x(x[i+1])-self.f_x(x[i])))
        func(*args)
    return wrapper

  @approximate
  def checkResidual(residual):
    if (f_x(x[i+2]) < self.residual):
      # この書き方で動くのかは不明
      break
    
  def changeFormat(self,value):
    # ほかに特に使いたいformatが今のところないのでいい書き方が思いつかない
    if (self.format == '.12e'):
      return '{.12e}'.format(value)
  def f_x(self,xnum):
    # 任意の関数を受け取って計算できるようにしたい（evalとかでできそう？）
    return (math.e)**(xnum)-(5)*(xnum)
  
    
if __name__ == '__main__':
  secant = Secant(1*(10^(-12)),'.12e')
  secant.approximate(-2,-1,50)