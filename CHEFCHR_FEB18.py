# Done

from itertools import permutations
permutation = permutations("chef", 4)
p = list(permutation)

def calc(s):
    count = 0
    for per in p:
        count += s.count("".join(list(per)))
    return count
t = int(input())
while(t):
    s = input()
    result = calc(s)
    if(result):
        print("lovely", result)
    else:
        print("normal")
    t = t-1
