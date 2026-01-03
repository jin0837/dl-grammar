# 2026-01-03
# 今日の確認：softmax の性質を確認する

import numpy as numpy

x = np.array([1.0, 2.0, 3.0])

exp_x = np.exp(x - np.max(x)) #オーバーフロー防止
softmax = exp_x / np.sum(exp_x)

print("input   :", x)
print("softmax :", softmax)
print("sum     :", np.sum(softmax))
