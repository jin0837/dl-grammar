#乗算レイヤの実装
class MulLayer:
   def __init__(self):
       self.x = None
       self.y = None

   def forward(f,x,y):
       self.x = x
       self.y = y
       out = x * y

       return out

   def backward(self,dout):
       dx = dout * y
       dy = dout * x

       return dx,dy
   
       
