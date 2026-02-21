
def gauss_sum_multiples(x,y):
    k = x // y
    return y * k * (k + 1) // 2

def sum_mult(x,y):
    return gauss_sum_multiples(x-1, y)

total = sum_mult(1000, 3) + sum_mult(1000, 5) - sum_mult(1000, 15)
print(total)

