def add_all(*args):
    """Adds all the values entered"""

    # Initilalize sum
    sum_all = 0

    # Accumulate sum
    for num in args:
        sum_all += num
    return sum_all

add_all(1) # 1
add_all(1, 2) # 3
add_all(5, 10, 15, 20) # 50     
