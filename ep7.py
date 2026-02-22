#By listing the first six prime numbers:
#2, 3, 5, 7, 11 and 13,
#we can see that the 6th prime is 13.
#What is the 10 001st prime number? 

import time 
start = time.time()
def prime_checker(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def thprime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if prime_checker(num):
            count += 1
    return num

print(thprime(10001))
end = time.time()
print("Çalışma süresi: ", end - start, "saniye")    