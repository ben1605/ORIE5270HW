import re
import sys
from pyspark import SparkConf, SparkContext
import numpy as np
from numpy.linalg import norm

def find_c(l, c1):
        norms = []
        for i in range(len(c1)):
            norms.append(norm(l - c1[i]))
        return (np.argmin(norms), (l, 1))

def final(ans):
        file = open("res1.txt","w")
        for i in ans:
            temp = "" 
            for elem in i:
                temp += str(elem) + " "
            file.write(temp + "\n")
        file.close()

def pyspark_kmeans(dFile, cFile, max_iter = 20):
    conf = SparkConf()
    sc = SparkContext(conf=conf)

    # Load the data
    data = sc.textFile(dFile).map(lambda line: np.array([float(x) for x in line.split(' ')])).cache()
    # Load the initial centroids
    c1 = sc.textFile(cFile).map(lambda line: np.array([float(x) for x in line.split(' ')])).collect()
    
    data1 = data.map(lambda l: find_c(l, c1))
    for i in range(max_iter):
        data1 = data1.reduceByKey(lambda n1, n2: (n1[0] + n2[0], n1[1] + n2[1])).sortByKey(ascending=True)
        c1 = data1.map(lambda l: l[1][0] / l[1][1]).collect()
        data1 = data.map(lambda l: find_c(l, c1))
    final(c1)
    sc.stop()

if __name__ == '__main__':
    pyspark_kmeans(sys.argv[1], sys.argv[2], 20)