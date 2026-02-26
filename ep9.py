#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def pisagor(n):
    for a in range(1, n):
        for b in range(a, n):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and a + b + c == n:
                return int(a * b * c)
    return None

print(pisagor(1000))


#i'm bored 