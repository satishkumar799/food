import random
import pandas as pd
[w1,w2,w3,w4] = [0.001,0.0019,0.0020,0.0019]
vals = []
for i in range(1000):
    x1 = random.randint(1, 10)
    x2 = random.randint(1, 5)
    x3 = random.randint(0, 100)
    x4 = random.randint(0, 70)
    eq = w1*x1+w2*x2+w3*x3+w4*x4
    vals.append([x1,x2,x3,x4,eq])
df = pd.DataFrame(vals,columns=['time','budget','availability','need'])
df.to_csv('productivity.csv',index=False)