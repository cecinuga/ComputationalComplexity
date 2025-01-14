def max_crossing_sub_array(A:list[int], low:int, mid:int, high:int) -> tuple[int, int, int]:

    sum = 0
    max_left = mid
    left_sum = float('-inf')
    for i in range(mid-1, low-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    max_right = mid
    right_sum = float('-inf')
    for j in range(mid, high-1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    
    return ( max_left, max_right, left_sum + right_sum )

def max_sub_array(A:list[int], low:int=0, high:int=-1) -> tuple[int, int, int]:
    if high == low: return ( low, high, A[low-1] )
    if high == -1: high = len(A)

    mid = ( low+high )//2

    left_low, left_high, left_sum = max_sub_array(A, low, mid)
    right_low, right_high, right_sum = max_sub_array(A, mid+1, high)
    cross_low, cross_high, cross_sum = max_crossing_sub_array(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum: return ( left_low, left_high, left_sum )
    if right_sum >= left_sum and right_sum >= cross_sum: return ( right_low, right_high, right_sum )
    return ( cross_low, cross_high, cross_sum )
