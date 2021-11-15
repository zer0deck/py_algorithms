#libs initialization
import numpy as np
import timeit
import matplotlib.pyplot as plt
from numpy.random.mtrand import standard_t
from tkinter import *


a = 2000
b = 200
#speed counter fuction (linear functions)
def speedy_line(function, r, N):
    logs = []
    for n in range(1, N + 1, 1):
        t = 0
        for j in range(r): 
            numb = list(np.random.random((n)))
            start = timeit.default_timer()
            function(numb)
            end = timeit.default_timer()
            #print(start, end)
            t += (end - start)
        logs.append(t / r)
    return logs
#speed counter function (matrix functions)
def speedy_matrix(k, n):
    logs = []
    for y in range(1, n + 1):
        t = 0
        for x in range(k):
            matrix1 = np.random.random((y, y))
            matrix2 = np.random.random((y, y))
            start = timeit.default_timer()
            matrix1 @ matrix2
            end = timeit.default_timer()
            t += (end - start)
        logs.append(t / k)
    return logs


#math alghorithms itself
#first one. Constant value
def constant_ex_1(numb):
    numb = 1
    return numb
#second one. Counting sum by n
def summorizing_ex_2(numb):
    rez = 0
    for i in range(len(numb)):
        rez += numb[i]    
    return rez
#third one. Counting product by n
def product_ex_3(numb):
    rez = 1
    for i in range(len(numb)):
        rez *= numb[i]  
    return rez
#forth one
#naiv polynominal
def polynominal_ex_4_1(numb):
    rez = 0
    for i in range(len(numb)):
        rez += numb[i] * 1.5 ** i
    return rez
#gorner polynominal
def polynominal_gorner_ex_4_2(numb, argument = 1.5): 
    rez = 0
    for i in range(len(numb), 0, -1):
        rez = numb[i - 1] + argument * rez 
    return rez
#fith one. Bubble sorting
def bubble_ex_5(numb):
    n = len(numb)
    for a in range(n):
        for b in range(n - 1):
            if numb[b] > numb[b + 1]:
                numb[b], numb[b + 1] = numb[b + 1], numb[b]
    return numb
#sixth one. Quick sort
def quicksort_ex_6(numb):
    return np.sort(numb, kind='quicksort')
#seventh one. Timesort
def timsort_ex_7(numb):
    return np.sort(numb, kind='stable')



#MATPLOTLIB figures lines initialization
ex_1 = speedy_line(constant_ex_1, 5, a)
ex_2 = speedy_line(summorizing_ex_2, 5, a)
ex_3 = speedy_line(product_ex_3, 5, a)
ex_4_1 = speedy_line(polynominal_ex_4_1, 5, b)
ex_4_2 = speedy_line(polynominal_gorner_ex_4_2, 5, b)
ex_5 = speedy_line(bubble_ex_5, 5, b)
ex_6 = speedy_line(quicksort_ex_6, 5, b)
ex_7 = speedy_line(timsort_ex_7, 5, b)
ex_8 = speedy_matrix(5, b)

#display functions
def b_ex_1():
    plt.figure(figsize=(10,5))
    plt.plot(ex_1)
    plt.ylabel('Time (seconds)', fontsize=10)
    plt.xlabel('Vector length $v$', fontsize=10)
    plt.legend(fontsize=10)
    plt.show()
def b_ex_2():
    plt.figure(figsize=(10,5))
    plt.plot(ex_2)
    #plt.plot([i for i in range(0, a, 1)], linewidth=3, label='$O(n)$')
    plt.ylabel('Time (seconds)', fontsize=10)
    plt.xlabel('Vector length $v$', fontsize=10)
    plt.legend(fontsize=10)
    plt.show()
def b_ex_3():
    plt.figure(figsize=(10,5))
    plt.plot(ex_3)
    #plt.plot([i ** math.log(3, 2) for i in range(0, a, 1)], linewidth=3, label='$O(n^log3base2)$')
    plt.ylabel('Time (seconds)', fontsize=10)
    plt.xlabel('Vector length $v$', fontsize=10)
    plt.legend(fontsize=10)
    plt.show()
def b_ex_4():
    plt.figure(figsize=(10,5))
    plt.plot(ex_4_1)
    plt.plot(ex_4_2)
    #plt.plot([i for i in range(0, b, 1)], linewidth=3, label='$O(n)$')
    plt.ylabel('Time (seconds)', fontsize=10)
    plt.xlabel('Vector length $v$', fontsize=10)
    plt.legend(fontsize=10)
    plt.show()
def b_ex_5():
    plt.figure(figsize=(10,5))
    plt.plot(ex_5)
    #plt.plot([i * i for i in range(0, b, 1)], linewidth=3, label='$O(n^2)$')
    plt.ylabel('Time (seconds)', fontsize=10)
    plt.xlabel('Vector length $v$', fontsize=10)
    plt.legend(fontsize=10)
    plt.show()
def b_ex_6():
    plt.figure(figsize=(10,5))
    plt.plot(ex_6)
    #plt.plot([i * math.log(i) for i in range(0, b, 1)], linewidth=3, label='$O(n*log(n))$')
    plt.ylabel('Time (seconds)', fontsize=10)
    plt.xlabel('Vector length $v$', fontsize=10)
    plt.legend(fontsize=10)
    plt.show()
def b_ex_7():
    plt.figure(figsize=(10,5))
    plt.plot(ex_7)
    #plt.plot([i * math.log(i) for i in range(0, b, 1)], linewidth=3, label='$O(n*log(n))$')
    plt.ylabel('Time (seconds)', fontsize=10)
    plt.xlabel('Vector length $v$', fontsize=10)
    plt.legend(fontsize=10)
    plt.show()

def b_ex_8():
    plt.figure(figsize=(10,5))
    plt.plot(ex_8)
    plt.ylabel('Time (seconds)', fontsize=10)
    plt.xlabel('Vector length $v$', fontsize=10)
    plt.legend(fontsize=10)
    plt.show()


#GUI
root = Tk()
root.title("Choose a plot")
root.geometry("300x350")


#buttons
btn1 = Button(text="Constant", background="#555", foreground="#ccc",
            padx="20", pady="8", font="16", command=b_ex_1)
btn1.place(relx=.2, rely=.1, anchor="c", height=30, width=130, bordermode=OUTSIDE)
btn1.pack(fill=BOTH)
btn2 = Button(text="Sum", background="#555", foreground="#ccc",
            padx="20", pady="8", font="16", command=b_ex_2)
btn2.place(relx=.2, rely=.2, anchor="c", height=30, width=130, bordermode=OUTSIDE)
btn2.pack(fill=BOTH)
btn3 = Button(text="Product", background="#555", foreground="#ccc",
            padx="20", pady="8", font="16", command=b_ex_3)
btn3.place(relx=.2, rely=.3, anchor="c", height=30, width=130, bordermode=OUTSIDE)
btn3.pack(fill=BOTH)
btn4 = Button(text="Polynominal", background="#555", foreground="#ccc",
            padx="20", pady="8", font="16", command=b_ex_4)
btn4.place(relx=.2, rely=.4, anchor="c", height=30, width=130, bordermode=OUTSIDE)
btn4.pack(fill=BOTH)
btn5 = Button(text="Bubble sorting", background="#555", foreground="#ccc",
            padx="20", pady="8", font="16", command=b_ex_5)
btn5.place(relx=.2, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
btn5.pack(fill=BOTH)
btn6 = Button(text="Quicksorting", background="#555", foreground="#ccc",
            padx="20", pady="8", font="16", command=b_ex_6)
btn6.place(relx=.2, rely=.6, anchor="c", height=30, width=130, bordermode=OUTSIDE)
btn6.pack(fill=BOTH)
btn7 = Button(text="Timsorting", background="#555", foreground="#ccc",
            padx="20", pady="8", font="16", command=b_ex_7)
btn7.place(relx=.2, rely=.7, anchor="c", height=30, width=130, bordermode=OUTSIDE)
btn7.pack(fill=BOTH)
btn8 = Button(text="Matrix", background="#555", foreground="#ccc",
            padx="20", pady="8", font="16", command=b_ex_8)
btn8.place(relx=.2, rely=.8, anchor="c", height=30, width=130, bordermode=OUTSIDE)
btn8.pack(fill=BOTH)
root.mainloop()

print()