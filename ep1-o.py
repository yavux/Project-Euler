# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Problem statement: If we list all the natural numbers below                                                           
# 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The                                                           
# sum of these multiples is 23. Find the sum of all the                                                                 
# multiples of 3 or 5 below 1000.                                                                                       
#                                                                                                                       
# As listed at https://projecteuler.net/problem=1           
                                                            
import time
begin = time.time()                                                                                                                       
n = 1000                        # Sum all multiples of the factors below                                                
                                # this number.                                                                          
factors = [3, 5]                # Use all multiples of these                                                            
factors.sort()                  # Sort in ascending order                                                               
summ = 0                        # Cumulative sum initialized to zero.                                                   
                                                                                                                        
for i in range(len(factors)):   # Need to deal with each factor, so loop over them.                                     
    for j in range(factors[i], n, factors[i]): # Count up to n by steps of factors[i].                                  
        if i == 0 or any(j % factors[k] for k in range(i)): # If we have a multiple, add it.                            
            summ += j                                                                                                   
                                                                                                                        
print("Sum = ", summ)

end = time.time()
print(f"Finished in {end - begin} seconds.")


