n, k = map(int, input().split())
array = list(map(int, input().split()))

cnt = 0
tap = [0] * n
tap_i = [0] * n

for j, a in enumerate(array):
    
    conn = False
    
    for i in range(len(tap)):
        if tap[i] == 0 or tap[i] == a:
            tap[i] = a
            conn = True
            break
            
        else:
            try:
                tap_i[i] = array[j+1:].index(tap[i])
            except:
                tap_i[i] = len(array) + 1
                
            continue
            
    if conn:
        pass
    else:
        max_idx = tap_i.index(max(tap_i))
        tap[max_idx] = a
        cnt += 1

print(cnt)
