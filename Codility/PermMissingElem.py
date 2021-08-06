# Solution1 (dict, 10min)
# https://app.codility.com/demo/results/trainingCMKBYB-286/
def solution(A):
    dic = dict()
    for i in range(1, len(A)+2):
        dic[i] = 0

    for a in A:
        dic[a] += 1

    rev_dic = dict(map(reversed, dic.items()))

    return rev_dic[0]

# Solution2 (list, 4min)
# https://app.codility.com/demo/results/trainingUTERSA-TVP/
def solution(A):
    ls = [0] * (len(A)+2)
    ls[0] = 1

    for a in A:
        ls[a] = 1

    return ls.index(0)
