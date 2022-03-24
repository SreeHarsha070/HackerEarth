#https://www.hackerearth.com/problem/algorithm/prime-count-1/
# Using Prefix_sum and Seive of Aratosthenes
n=10000001
seive=[1]*n
prefix=[0]*n


def seive_gen():
    i=2
    while(i*i<=n):
        if seive[i]==1:
            for j in range(i*i,n,i):
                seive[j]=0
        i+=1
    seive[0]=0
    seive[1]=0
    for i in range(2,n):
        if seive[i]==1:
            prefix[i]=prefix[i-1]+1
        else:
            prefix[i]=prefix[i-1]


seive_gen()
t=int(input())
for k in range(t):
    x=int(input())
    print(prefix[x])
