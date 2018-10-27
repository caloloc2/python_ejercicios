# Ejercicio 1
import tkinter

root = tkinter.Tk()
root.geometry("400x200")

def callback(num):
    print("click!")

b1 = tkinter.Button(root, width=2, height=1, bg = "black", command = callback(0))
b1.grid(row=30, column=1)

b2 = tkinter.Button(root, width=2, height=1, bg = "white", command = callback(1))
b2.grid(row=60, column=1)

# MyButton1= tkinter.Button(root, width=2, height=1, bg = "white", command = color_change)
# MyButton1.grid(row=60, column=1)

# MyButton1 = tkinter.Button(root, width=2, height=1, bg = "white", command = color_change)
# MyButton1.grid(row=30, column=2)

# MyButton1= tkinter.Button(root, width=2, height=1, bg = "white", command = color_change)
# MyButton1.grid(row=60, column=2)

root.mainloop()







# from random import shuffle
# import numpy as np
# import matplotlib.pyplot as plt

# prob = [2/16]
# pb = 1
# for n in range(0,14):
#     pb *= (14-n)/(16-n)
#     pn = 2/(16-(n+1))
#     prob += [pb * pn]

# x = np.array([i+1 for i in range(15)])
# print(x)
# px = np.array(prob)
# print(px)
# mx = np.sum(x*px)
# print(mx)
# vx = np.sum((x**2)*px) - mx**2
# sx = np.sqrt(vx)

# # plt.bar(x, px) 
# # plt.show()

# # print("Probs", px, "\nSum(px)=", np.sum(px))
# # print("mean = ", mx, "std = ", sx)