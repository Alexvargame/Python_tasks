
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(matrix)
summ=[]
def magic(matrix):

    for i in range(n):
        sum_=0
        for j in range(n):
            sum_=sum_+matrix[i][j]
        summ.append(sum_)
    for j in range(n):
        sum_=0
        for i in range(n):
            sum_=sum_+matrix[i][j]
        summ.append(sum_)
    sum_=0
    for i in range(n):
        sum_=sum_+matrix[i][i]
    summ.append(sum_)
    sum_=0
    for i in range(n):
        sum_=sum_+matrix[i][n-1-i]
    summ.append(sum_)
    print(summ)
    return summ
def check(summ):
    for i in range(len(summ)-1):
        if summ[i]==summ[i+1]:
            pass
        else: return False
    return True
magic(matrix)
print(check(summ))
