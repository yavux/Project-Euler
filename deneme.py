import time
begin = time.time()

from utils import gauss_sum_multiples 
def sum_mult(x,y):
    return gauss_sum_multiples(x-1, y)

total = sum_mult(1000, 3) + sum_mult(1000, 5) - sum_mult(1000, 15)
print(total)

end = time.time()
print(f"Finished in {end - begin} seconds.")
