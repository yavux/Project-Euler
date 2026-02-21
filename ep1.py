# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
import time
begin = time.time()

from utils import gauss_sum_multiples 
def sum_mult(x,y):
    return gauss_sum_multiples(x-1, y)

total = sum_mult(1000, 3) + sum_mult(1000, 5) - sum_mult(1000, 15)
print(total)

end = time.time()
print(f"Finished in {end - begin} seconds.")
