import time
begin = time.time()
p = [0] * 1001
q = [0] * 1001
a = [0] * 1001
p[0], p[1] = 1, 3
q[0], q[1] = 1, 2
a[0], a[1], a[2], a[3], a[4], a[5] = 1, 2, 2, 2, 2, 2
p = [1, 3, 0, 0, 0, 0]
q = [1, 2, 0, 0, 0, 0]
a = [1, 2, 2, 2, 2, 2]
for n in range(2, 1000):
    p[n] = a[n]*p[n-1] + p[n-2]
    q[n] = a[n]*q[n-1] + q[n-2]
print(p)
print(q)

end = time.time()
print(f"Finished in {end - begin} seconds.")