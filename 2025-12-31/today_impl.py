# affine -> relu -> softmax skeleton
import numpy as np

def affine(x,W,b):
  return x @ W + b

def relu(x):
  return np.maximum(0,x)

def softmax(x):
  exp_x = np.exp(x - np.max(x))
  return exp_x / np.sum(exp_x)

