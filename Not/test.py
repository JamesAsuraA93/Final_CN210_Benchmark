from tkinter import *
from Not import calTest

root = Tk()
root.title("Benchmark test")

ex = Label(text="CN210 Excecute", font="Helvetica 18 bold")
ex.grid(row=0, column=0, pady=15, columnspan=5)



def disk_execute():
    calTest.run()
    disk_out.insert(0, f"{calTest.display()}")


# output of disk
text_disk = Label(text="Disk Benchmark:", font="Helvetica 10")
text_disk.grid(row=1, column=0, padx=15)


disk_button = Button(text="Disk", command=disk_execute, foreground="red", bd=3, font="12", width=7)
disk_button.grid(row=2, column=0, pady=15)
disk_out = Entry(font="Helvetica 12", width=35)
disk_out.grid(row=2, column=2, pady=15)

root.geometry("500x500")
root.mainloop()

