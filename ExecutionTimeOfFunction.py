def addition(a, b):
    return a + b


def cal_exe_time(a, b):
    from time import time
    start = time()

    addition(a, b)

    end = time()

    return end - start


print(cal_exe_time(54667769743, 268758544769743))
