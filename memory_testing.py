import time


def run():
    a = []
    startTimeMBCounter = time.time()
    size = 1073741824 * 2
    i = 1
    while a.__sizeof__() < size:
        a.append(i)
        if a.__sizeof__() > size:
            break
        else:
            i += 1
    a.clear()

    file = open("mocking_data.txt", "r")
    lines = file.readlines()
    while a.__sizeof__() < size:
        a.append(lines)
        if a.__sizeof__() > size:
            break
    file.close()
    del a

    endTimeMBCounter = time.time()
    score = ((size * 2) / (endTimeMBCounter - startTimeMBCounter)) / 1000
    sec_use = endTimeMBCounter - startTimeMBCounter

    return dict(sec=float(format(sec_use, ".2f")), score=int(score))
