import os
import time


def run():
    try:
        disk_test = open("disk_test.txt", "w")
    except ValueError:
        disk_test = open("disk_test.txt", "x")

    size = 1073741824 * 1
    startTimeMBCounter = time.time()
    for i in range(int(size)):
        disk_test.write('A')

    disk_test.close()

    os.remove("disk_test.txt")

    endTimeMBCounter = time.time()
    sec_use = endTimeMBCounter - startTimeMBCounter

    score = (size / sec_use) / 1000
    return dict(sec=format(sec_use, ".2f"), score=int(score))