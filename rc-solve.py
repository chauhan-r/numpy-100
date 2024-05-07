import numpy as np

# 1-10
print(np.version)
print(np.config.show())
a = np.zeros(10)
print(a.size)

# 11-20
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)
b = np.diagflat(np.arange(1,5))
print(b)

# 21-30
a = np.zeros((8,8), dtype=int)
for i in range(8):
    for j in range(8):
        a[i,j] = (i+j)%2

print(a)

# 31-40
np.seterr('ignore')
a = np.random.rand(10)
b = np.random.rand(10)
print(np.union1d(a,b))

# 41-50
c = np.array([1,2,3,4])
d = c[1:-1]
print(d)

# 51-60
e = np.zeros((5,5), dtype=int)
for i in range(5):
    for j in range(5):
        e[i,j] = i+j

print(e)

# 61-70
f = np.random.rand(10)
g = f[f>0.3]
h = np.argsort(g)
i = g[h[1:]]
j = h[1:]

print(i)

# 71-80
k = np.zeros((100,2), dtype=int)
for i in range(100):
    k[i,0] = i % 10
    k[i,1] = i // 10

l = k[k[:,0]%5==0]
m = np.unique(l[:,1])

print(m)

# 81-90
n = np.zeros((2,3), dtype=int)
for i in range(2):
    for j in range(3):
        n[i,j] = i+j

o = np.concatenate((np.arange(10).reshape(-1,1),np.random.rand(10).reshape(-1,1)),axis=1)

print(o)

# 91-100
p = np.array([1,2,3,4,5], dtype=[('x',int),('y',int)])
q = p[p['x'] > 2]

r = q[q['y'] == 3]
s = np.random.randint(0,10, (5,))
t = np.concatenate((np.arange(10).reshape(-1,1),np.random.rand(10).reshape(-1,1)),axis=1)
u = t[t[:,0]%2==0]

print(u)

print(np.mean(u))
