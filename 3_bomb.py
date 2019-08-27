def solution(x, y):
    M, F = int(x), int(y)
    
    gen = 0
    
    # Work backwards from final required bombs
    while M != F:       # Repeat until M equals F

        # Initial solution - Too slow
##        if F > M:           # If F > M, that means in previous gen, value of M was added to F
##            F = F-M         # so subtract M from F to get previous F value
##        else:               # Else, F was added to M
##            M = M-F         # so subtract F from M to get previous M value
##        gen += 1        

        # Speed up subtraction when difference between M & F is large 
        if F > M:
            g = max(1,(F-M)//M)     # e.g. if F = 100, M = 21, 100-21 = 79 // 21 = 3 , so g = max(1, 3) = 3
            F = F - g * M           # do F = 100 - 3*21 = 37
        else:
            g = max(1,(M-F)//F)     # e.g. if M = 100, F = 77, 100-77 = 23 // 77 = 0 , so g = max(1, 0) = 1
            M = M - g * F           # do M = 100 - 1*77 = 23

        gen += g
    
    if M == F == 1:         # If M and F both reach original state (1,1)
        return str(gen)     # we have solution
    else:                   # But if M & F are not equal to 1.. say 3,3, that state
        return 'impossible' # is impossible to reach from original state (1,1)

#print(solution(pow(10,40),pow(10,40)+1))
