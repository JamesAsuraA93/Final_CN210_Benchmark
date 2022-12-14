
process = 0

def run():
    for i in range(1000000000000000000000000000000000000000000000000000000000):
        update_pro(i)

def update_pro(number):
    global process
    process = number
    return

def display():
    return process


