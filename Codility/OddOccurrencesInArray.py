# https://app.codility.com/demo/results/training7P3HY6-KGH/

from collections import defaultdict

def solution(A):
    dic = defaultdict(int)

    for n in A:
        if not dic[n]:
            dic[n] += 1
        else:
            dic[n] -= 1

    rev_dic = dict(map(reversed, dic.items()))

    return rev_dic[1]
