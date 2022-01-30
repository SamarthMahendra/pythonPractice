w=[1,2,4,2,5]
v=[5,3,5,3,2]

def knapsack(n,c,memo={}):
    if (n,c) in memo:
        return memo[(n,c)]
    if n==0 or c==0:
        return 0
    if w[n-1]>c:

        return knapsack(n-1,c)
    else:
        temp1= knapsack(n-1,c)
        temp2=v[n-1]+knapsack(n-1,c-w[n-1])
        result=max(temp2,temp1)
    memo[(n,c)]=result
    return result
print(knapsack(5,10))