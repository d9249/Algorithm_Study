# 2.1_(b)
# “정렬후 회전된 배열”이란 (5, 8, 9, 2, 3, 4)와 같은 배열을 말한다.
# 즉, 정렬이 된 후에 회전 연산이 0회 이상 적용된 배열이다.
# 회전 연산이란 배열의 마지막 원소가 처음으로 이동하고 나머지 원소들이 오른쪽으로 한 칸씩 이동하는 것을 말한다.
# 예를들어, (2, 3, 4, 5, 8, 9)는 정렬된 배열이고 여기에 회전 연산을 1회 적용하면 (9, 2, 3, 4, 5, 8)이 되고
# 여기에 회전 연산을 추가로 2회 적용하면 (5, 8, 9, 2, 3, 4)가 된다.
# 따라서 (5, 8, 9, 2, 3, 4)는 정렬후 회전된 배열이다.
# (b) 정렬후 회전된 배열A [0..n-1]가 회전연산을 몇번 적용한 것인지 알아내는 알고리즘을 설계하고 분석하시오.

A= [5, 8, 9, 81, 99, -99, -98, 2, 3, 4]
i = 0

def NumRotAccount(A, i):
    if len(A) == i+1:
        return len(A)+1
    if A[i] < A[i+1]:
        return NumRotAccount(A, i+1)
    else:
        return i+1
    
print(NumRotAccount(A, i))