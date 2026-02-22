#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# Formula: (1 + 2 + ... + n)^2 - (1^2 + 2^2 + ... + n^2)
# Simplified: [n * (n + 1) * (n - 1) * (3n + 2)] / 12


import time 
start = time.time()

def sum_square_difference(n):
   return ((n*(n+1)*(n-1)*(3*n+2)) //12)
print(sum_square_difference(100))
end = time.time()
print("Çalışma süresi: ", end - start, "saniye")    