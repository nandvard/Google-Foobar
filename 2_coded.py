from itertools import permutations

def solution(l):
    max_num = 0
    
    for n in range(1, len(l)+1):                # Generate power set
        for perm in permutations(l, n):         # Permute digits in each set
            num, sum = 0, 0
            for i,d in enumerate(perm):
                num += d*pow(10,i)              # Generate decimal number from digits
                sum += d                        # Get sum of digits
            #print (num,sum)
            if sum%3 == 0:                      # Check divisibility by 3
                    max_num = max(num, max_num) # Check max number so far

    return max_num

print (solution([1,1,6]))

