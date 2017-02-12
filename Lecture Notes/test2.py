def sum_even(a, b):
    count = 0
    for i in range(0, 101, 1):
        if(i % 2 == 0):
            count += i
    return count
