
def printperm(freq, middle):
    t = []
    opposite = []

    # adds first half of palindrome
    for char in freq:
        opposite = [char]+opposite
        for i in range(1, freq[char][0]//2+1):
            t.extend([str(freq[char][i])])

    # adds middle element of palindrome
    if(middle):
        middle_index = freq[middle][0]//2+1
        t.extend([str(freq[middle][middle_index])])

    # adds final half of palindrome
    for char in opposite:
        if char != middle:
            for i in range(freq[char][0]//2+1, freq[char][0]+1):
                t.extend([str(freq[char][i])])
        else:
            for i in range(freq[char][0]//2+2, freq[char][0]+1):
                t.extend([str(freq[char][i])])
    return t

def perm(s):
    freq = {}
    for i in range(len(s)):
        if s[i] in freq:
            freq[s[i]][0] += 1
            freq[s[i]].extend([i+1])
        else:
            freq[s[i]] = [1, i+1]
    #print(freq)
    odd = 0
    middle = ''
    for i in freq:
        if(freq[i][0] % 2 != 0):
            middle = i
            odd += 1
        if(odd > 1):
            return []
    return printperm(freq, middle)

t = int(input())
while(t):
    s = input()
    t = t-1
    result = perm(s)
    if(result):
        for i in result:
            print(i,' ',end='')
        print('')
    else:
        print(-1)
