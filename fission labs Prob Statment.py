def smallest_prime_factor(n):
    if n == 0 or n == 1:                        #because if 0 or 1 then number itself should be returned
        return n
    if n % 2 == 0:                              #checking for 2,3,5. by this we have reduced our total number of numbers to be checked to 3/10th of original size
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5

    for i in range(7,int(n**(1/2.0))+1,30):     #increment by 30 because lcm(2,3,5) = 30 & we have checked for those earlier so this will produce the same pattern of divisibility by those numbers at the same offsets.
        if n%i == 0:                            #now we first write numbers from 0-29 and then eliminate the numbers which we have covered earlier (2k+1,2+3k,3+5k) and remaining nos. will be 0,4,6,10,12,16,22,24. 
            return i
        if n%(i + 4) == 0:
            return i+4
        if n%(i + 6) == 0:
            return i+6
        if n%(i + 10) == 0:
            return i+10
        if n%(i + 12) == 0:
            return i+12
        if n%(i + 16) == 0:
            return i+16
        if n%(i + 22) == 0:
            return i+22
        if n%(i + 24) == 0:
            return i+24

    return n                                    #if none of above works then n itself if prime

tc = int(input())                               #taking tc = number of contests as integer input

for i in range(tc):
    n = int(input())                            #taking n = number of problems in contest as integer input
    x = smallest_prime_factor(n)
    print(n - x,x)