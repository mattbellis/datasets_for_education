import sys
import numpy as np

data = np.loadtxt(sys.argv[1],skiprows=3,dtype=str,unpack=True,delimiter=',')

cases = data[1].astype(int)
deaths = data[2].astype(int)

newcases = []
newdeaths = []

for i,(case,death) in enumerate(zip(cases,deaths)):

    if i==0:
        newcases.append(case)
        newdeaths.append(death)
    else:
        x = case - cases[i-1]
        newcases.append(x)
        x = death - deaths[i-1]
        newdeaths.append(x)

for a,b,c in zip(data[0],newcases,newdeaths):
    print(f'{a},{b},{c}')
