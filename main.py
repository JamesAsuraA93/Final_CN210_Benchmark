from tkinter import *
import cpu_testing, memory_testing, disk_testing

root = Tk()
root.title("Tyschu Benchmark")

# text
ex = Label(text="CN210 Tyschu Benchmark", font="Helvetica 18 bold")
ex.grid(row=0, column=0, pady=15, columnspan=5)


def storage_all(one, two, three):
    return


# Disk Test
def disk_ex():
    disk_out.delete(0, END)
    val = disk_testing.run()
    disk_out.insert(0, f"second = {val['sec']}, score = {(val['score']):,}")
    return val


# Mem Test
def mem_ex():
    mem_out.delete(0, END)
    val = memory_testing.run()
    mem_out.insert(0, f"second = {val['sec']}, score = {(val['score']):,}")
    return val


# CPU Test
def cpu_ex():
    cpu_out.delete(0, END)
    val = cpu_testing.run()
    cpu_out.insert(0, f"second = {val['sec']}, score = {(val['score']):,}")
    return val


# All Test
def all_ex():
    disk_out.delete(0, END)
    mem_out.delete(0, END)
    cpu_out.delete(0, END)
    all_out.delete(0, END)
    one = disk_ex()
    two = mem_ex()
    three = cpu_ex()
    result = f"second = {(one['sec'] + two['sec'] + three['sec']):.2f}, score = {(one['score'] + two['score'] + three['score']):,}"
    all_out.insert(0, result)


# Clear all result
def clear_result():
    disk_out.delete(0, END)
    mem_out.delete(0, END)
    cpu_out.delete(0, END)
    all_out.delete(0, END)


# output of disk
text_disk = Label(text="Disk Benchmark:", font="Helvetica 10")
text_disk.grid(row=1, column=0, padx=15)
disk_button = Button(text="Disk", command=disk_ex, foreground="red", bd=3, font="12", width=7)
disk_button.grid(row=2, column=0, pady=15)
disk_out = Entry(font="Helvetica 12", width=35)
disk_out.grid(row=2, column=2, pady=15)

# output of memory
text_mem = Label(text="Memory Benchmark:", font="Helvetica 10")
text_mem.grid(row=3, column=0, padx=15)
mem_button = Button(text="Memory", command=mem_ex, foreground="blue", bd=3, font="12", width=7)
mem_button.grid(row=4, column=0, pady=15)
mem_out = Entry(font="Helvetica 12", width=35)
mem_out.grid(row=4, column=2, pady=15)

# output of cpu
text_cpu = Label(text="CPU Benchmark:", font="Helvetica 10")
text_cpu.grid(row=5, column=0, padx=15)
cpu_button = Button(text="CPU", command=cpu_ex, foreground="green", bd=3, font="12 ", width=7)
cpu_button.grid(row=6, column=0, pady=15)
cpu_out = Entry(font="Helvetica 12", width=35)
cpu_out.grid(row=6, column=2, pady=15)

# output of all
text_all = Label(text="Benchmark All:", font="Helvetica 10")
text_all.grid(row=7, column=0, padx=15)
all_button = Button(text="Start All", command=all_ex, foreground="orange", bd=3, font="12 ", width=7)
all_button.grid(row=8, column=0, pady=15)
all_out = Entry(font="Helvetica 12", width=35)
all_out.grid(row=8, column=2, pady=15)

# clear all result
clear_button = Button(text="CLEAR", command=clear_result, bg="red", bd=3, font="Helvetica 12 bold")
clear_button.grid(row=9, column=2, pady=15)

# size
root.geometry("500x500")
root.mainloop()
