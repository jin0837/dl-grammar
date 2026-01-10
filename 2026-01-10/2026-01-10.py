#RELU実装

class ReLu:
    def __init__(self):
        self.mask = None
    
    def forward(self,x):
        self.mask = (x <= 0) #ReLUによって潰されたところをTrueとして記録
        out = x.copy()
        out[self.mask] = 0   #mask が True の部分だけを 0 にする
    
        return out
    
    def backward(self,dout):
        dout[self.mask] = 0
        dx = dout
    
        return dx
