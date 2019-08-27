def solution(l):
    
    count = 0

    # Brute Force - too slow
#    for i in range(len(l)-2):
#        for j in range(i+1,len(l)-1):
#            if l[j]%l[i]==0:
#                for k in range(j+1,len(l)):
#                     if l[k]%l[j]==0:
#                        #print (l[i],l[j],l[k])
#                        count += 1

    # Dynamic Programming

    div = [0]*len(l)
    
    for k in range(1,len(l)):       # For every number k
        for j in range(0,k):            # Loop through every number j before it
            if l[k]%l[j] == 0:          # If j is a divisor of k
                div[k] += 1                 # Increment number of divisors of k
                count += div[j]             # If j has divisors, then we have triplets : (k,j,divisors of j)

    return count

#print (solution([1,2,3,4,5,6]))
