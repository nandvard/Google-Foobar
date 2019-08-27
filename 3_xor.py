# XOR of all values upto a number follows a cyclical pattern of period 4
def xor_upto(a):
    val = [a,1,a+1,0]
    return val[a%4]

# XOR of all values in range (a,b) is similar to sum of all values in the range: sum_upto(b)-sum_upto(a)
def xor_range(a,b):
    return xor_upto(b) ^ xor_upto(a-1)
# Note: this happens to work even when a=0, so we can avoid an additional IF condition check (when a-1 equals -1)

def solution(start,length):
    val = 0

    # Brute Force - Takes too long
#    for line in range(length):
#        for i in range(length-line):
#            val = val ^ (start + line*length + i)

    # Using XOR cyclical shortcut
    for i,a in enumerate(range(start, start+length*(length-1) +1, length)):
        val = val ^ xor_range(a, a + length-i-1)
    
    return val

#print(solution(17,4))
