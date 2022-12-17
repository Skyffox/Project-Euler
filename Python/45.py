# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle	 	Tn=n(n+1)/2	 	
# Pentagonal	Pn=n(3n−1)/2	
# Hexagonal	 	Hn=n(2n−1)	 	
# It can be verified that T285 = P165 = H143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.
# Execution time: 209.046s

def triangle(n):
    return n * (n + 1) / 2

def pentagonal(n):
    return n * (3*n - 1) /2
    
def hexagonal(n):
    return n * (2*n - 1)
    
    
tri_nums = []
penta_nums = []
hex_nums = []
for n in range(1, 56000):
    tri_nums.append(triangle(n))
    penta_nums.append(pentagonal(n))
    hex_nums.append(hexagonal(n))

found_tri_num = 0
for i, tnum in enumerate(tri_nums):
    for j, hnum in enumerate(hex_nums[:i+1]):
        if hnum > tnum:
            break
        if hnum == tnum:
            for k, pnum in enumerate(penta_nums[j:i+1]):
                if pnum == hnum and pnum == tnum:
                    found_tri_num = pnum
                    print (found_tri_num)
                    print (i,k+j,j)
        
