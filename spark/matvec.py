import re
import sys
from pyspark import SparkConf, SparkContext
import numpy as np

def pair(l):
    return [(l[i], i) for i in range(1,len(l))] # return element, and then its column index starting with 1
def row(l):
    return l[0]
def pair_v(l):
    return [(i + 1, l[i]) for i in range(len(l))]  # return vector with index
def expand(l):
    return [(l[0],l[1][i]) for i in range(len(l[1]))]
def order(l):
    return [(l[i][1][1], (l[0][0], l[i][1][0])) for i in range(len(l))]
def reduce_m(l):
    for i in range(len(l)):
        yield (l[i][0],(l[i][1][0],l[i][1][1]))
def reduce_v(l):
    for i in range(len(l)):
        yield (i+1, l[i][1])
def remove(l):
    # return [(l[i][1][0][0], l[i][1][0][1] * l[i][1][1]) for i in range(len(l))]
    return [(l[i]) for i in np.arange(1,len(l),2)]
def matrix_vector(matrix, vector):
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    lines = sc.textFile(matrix)
    vecs = sc.textFile(vector)
    mat = lines.map(lambda l: list(map(float, re.split(',', l))))  # separate matrix by ,
    mat = mat.map(lambda l: (row(l), (pair(l))))  # return (row index starting with 1, (element, column idx st w/ 1)
    vec = vecs.map(lambda l: list(map(float, re.split(',', l))))  # separate vec by ,
    vec = vec.map(lambda l: pair_v(l))
    mat = mat.map(lambda l: order(expand(l)))  # change order of row idx and col idx
    mat = mat.flatMap(reduce_m)
    vec = vec.flatMap(reduce_v)
    mat = mat.join(vec)  # join vector by key
    # [(1, ((1.0, 1.0), 1.0)), (1, ((2.0, 4.0), 1.0)), (1, ((3.0, 7.0), 1.0)),
    # (2, ((1.0, 2.0), 2.0)), (2, ((2.0, 5.0), 2.0)), (2, ((3.0, 8.0), 2.0)),
    # (3, ((1.0, 3.0), 3.0)), (3, ((2.0, 6.0), 3.0)), (3, ((3.0, 9.0), 3.0))]
    mat = mat.flatMap(remove)
    mat = mat.map(lambda l: (l[0][0], l[0][1] * l[1]))
    res = mat.reduceByKey(lambda n1, n2: n1 + n2)
    res = res.map(lambda l: l[1]).collect()
    print(res)
    # res.saveAsTextFile("test111")
    sc.stop()

if __name__ == '__main__':
    matrix_vector(sys.argv[1], sys.argv[2])
