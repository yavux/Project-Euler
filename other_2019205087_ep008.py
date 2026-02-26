#https://projecteuler.net/thread=8;page=8#450290

import time
begin = time.time()

num = "73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966489504452445231617318564030987111217223831136222989342338030813533627661428280644448664523874930358907296290491560440772390713810515859307960866701724271218839987979087922749219016997208880"
maxx = 0
longness = len(num)
i = 0
# I looked every page at the forum to find better soln. I found this one.
# The time is nearly half of my soln. The way of approach is %100 same as mine.
while i <= longness - 13:
    window = num[i:i+13]

    if '0' in window: #But at this step the user  is not createting temp string unlike me. Just checking the first digit at every window.
        zero = window.index('0') # If there is a zero, skipping the current and look at the next new "first" digit of new window.
        i += zero + 1
    else:                       # Probably cause of this, the time is nearly half of mine.
        product = 1
        for d in window:
            product *= int(d)
        if product > maxx:
            maxx = product
        i += 1

print("Maximum product of 13 adjacent digits is:", maxx)
end = time.time()
print(f"Finished in {end - begin} seconds.")

