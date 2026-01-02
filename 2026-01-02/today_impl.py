# 2026-01-02
# 今日の確認：relu の動作を手で確かめる

import numpy as np

x = np.array([-1.0,0.0,2.0])
y = np.maximum(0,x)

print("input:",x)
print("relu :", y)
