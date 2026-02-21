# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
## WHY CHECK FOR DIVISIBILITY BY 11?
# A 6-digit palindrome is always in the format 'abccba'.
# Expressing this mathematically:
# 100000a + 10000b + 1000c + 100c + 10b + a
# = 100001a + 10010b + 1100c
# = 11 * (9091a + 910b + 100c)
# Since the result is always a multiple of 11, at least one of the 
# two 3-digit factors making up this number must be divisible by 11.
import time 
start = time.time()

largest = 0 
for i in range(999,99,-1):
    if i * 999 <= largest:
        continue
    for j in range(999,99,-1):
        if j % 11 == 0:
            product = str(i*j)
            if product == product[::-1]:
                if i * j > largest:
                    largest = i * j
                    factors = (i,j)

print(largest,factors[0],factors[1])
    
end = time.time()
print("Çalışma süresi: ", end - start, "saniye")
