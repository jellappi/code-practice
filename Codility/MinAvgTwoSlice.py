# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

def mean(B):
    return sum(B) / len(B)

def solution(A):
    
    # window len = 2
    min_num_2 = 100000
    idx_2 = 10001
    for i in range(len(A)-1):
        if min_num_2 > mean(A[i:i+2]):
            min_num_2 = mean(A[i:i+2])
            idx_2 = i

    # window len = 3
    min_num_3 = 100000
    idx_3 = 10001
    for i in range(len(A)-2):
        if min_num_3 > mean(A[i:i+3]):
            min_num_3 = mean(A[i:i+3])
            idx_3 = i

    if min_num_2 > min_num_3:
        return idx_3
    else:
        return idx_2
