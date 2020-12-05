def merge(A, B):
    C = []
    j, k = 0, 0
    for i in range(len(A + B)):
        if j >= len(A) or k >= len(B):
            break
        if A[j] > B[k]:
            C.append(B[k])
            k += 1
        else:
            C.append(A[j])
            j += 1
    if len(A)-1 >= j:
        C += A[j:]
    if len(B)-1 >= k:
        C += B[k:]
    return C


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
