# https://app.codility.com/demo/results/training7M9S9K-6NS/

def solution(A, K):
    if not A:
        return A

    K =  K % len(A)
    if not K:
        return A
    else:
        shifted_A = A[-K:] + A[:-K]
        return shifted_A
