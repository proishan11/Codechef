# Done

t = int(input())
while(t):
    n = int(input())
    time = [int(x) for x in input().split()]
    c, d, s = input().split()
    c = int(c)
    d = int(d)
    s = int(s)
    print('{0:.9f}'.format((c-1)*max(time)))
    t = t-1
