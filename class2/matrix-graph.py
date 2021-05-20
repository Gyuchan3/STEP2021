import numpy, sys, time
import matplotlib.pyplot as plt

x = [] #[0,1,...,N]
y = [] #execution time for each n

if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

N = int(sys.argv[1])
for n in range(N + 1):
    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C

    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    begin = time.time()

    ######################################################
    # Write code to calculate C = A * B                  #
    # (without using numpy librarlies e.g., numpy.dot()) #
    for i in range(n): #Aのi行目
        for j in range(n): #Aのj列目、Bのj行目
            for k in range(n): #Bのk列目
                c[i, k] += a[i, j] * b[j, k]
    ######################################################

    end = time.time()
#     print(f"n: {n}") 
#     print("time: %.6f sec" % (end - begin))

    #グラフの準備
    x.append(n)
    y.append(end - begin)

#Nと実行時間の関係をグラフにする
plt.scatter(x, y)
plt.xlabel('n')
plt.ylabel('execution time')
plt.grid()
plt.show()