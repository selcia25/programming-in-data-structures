def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i]<S2[j]):
            S[i+j] = S1[i]
            i = i + 1
        else:
            S[i+j] = S2[j]
            j = j + 1

def merge_sort(S):
    n = len(S)
    if n < 2 :
        return
    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)
    return S

S = [1,17,51,14,3,42,8]
print(merge_sort(S))