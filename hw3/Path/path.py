import numpy as np
from ast import literal_eval as to_tuple
import heapq


def get_graph(file):
    source = []
    info = []
    count = 0
    with open(file) as f:  # read text file
        data = f.readlines()
    for i in range(len(data)):
        temp = data[i].strip().split("\n")
        if count % 2 == 0:     # save odd line to be source
            source.append(temp[0])
        else:       # save even line to be recepient node
            info.append(temp[0])
        count += 1
    graph = dict([(float(elem), []) for elem in source])
    next = [[] for i in range(len(source))]
    for i in range(len(source)):
        start = 0
        if info[i] != "":
            for j in range(len(info[i])-1):  # to separate each recepient node
                if info[i][j] == ")" and info[i][j + 1] == ",":
                    next[i].append(to_tuple(info[i][start: j + 1]))  # make them tuple
                    start = j + 2
            next[i].append(to_tuple(info[i][start: len(info[i])]))
        else:   # if empty, append ""
            next[i].append("")
    for i in range(len(source)):
        for j in range(len(next[i])):
            if info[i] != "":   # change str to float
                temp = (float(next[i][j][0]), float(next[i][j][1]))
                graph[float(source[i])].append(temp)
    return(graph)


def find_shortest_path(file, source, destination):
    graph = get_graph(file)
    s = []
    F = []
    F_n = []
    s_n = []
    dist = dict()
    dist[source] = 0.0
    path = dict([(float(elem), []) for elem in graph.keys()])
    for i in path.keys():
        path[i].append(float(source))
    heapq.heappush(F, (dist[source], source))
    F_n.append(F[-1][1])
    while F != []:
        f = heapq.heappop(F)
        s.append(f)
        s_n.append(s[-1][1])
        for node in graph[f[1]]:
            if node[0] not in F_n and node[0] not in s_n:
                dist[node[0]] = dist[f[1]] + node[1]
                path[node[0]] = (path[f[1]][:])
                path[node[0]].append(node[0])
                heapq.heappush(F, (dist[node[0]], node[0]))
                F_n.append(node[0])
            elif dist[f[1]] + node[1] < dist[node[0]]:
                dist[node[0]] = dist[f[1]] + node[1]
                path[node[0]] = (path[f[1]][:])
                path[node[0]].append(node[0])
                if node[0] not in s_n:
                    for i in range(len(F)):
                        if F[i][1] == node[0]:
                            del F[i]
                            heapq.heappush(F, (dist[node[0]], node[0]))
                            s_n.append(node[0])
                            break
                    tempF = []
                    for i in range(len(F)):
                        temp = heapq.heappop(F)
                        heapq.heappush(tempF, temp)
                    F = tempF
                    F_n.append(node[0])
    if len(path[destination]) == 1 and source != destination:
        return float("inf"), []
    else:
        return dist[destination], path[destination]


def func(graph, step, source, destination):
    temp = []
    path = []
    cache = []
    if step == 0:
        if destination == source:
            return 0, [source]
        else:
            return float("inf"), []
    else:
        if graph[source] == []:
            if destination == source:
                return 0, [source]
            else:
                return float("inf"), []
        else:
            count = 0
            for child in graph[source]:
                cache.append(func(graph, step - 1, child[0], destination))
                temp.append(cache[count][0] + child[1])
                path.append(cache[count][1])
                count += 1
            former = func(graph, step - 1, source, destination)
            if cache == []:
                return former
            else:
                latter = (temp[np.argmin(temp)], path[np.argmin(temp)])
                final = np.argmin([former[0], latter[0]])
                if final == 0:
                    return former
                else:
                    latter[1].insert(0, source)
                    return latter[0], latter[1]


def find_negative_cycles(file):
    graph = get_graph(file)
    if len(graph) == 0:
        return None
    width = len(graph)
    flag = False
    for i in graph.keys():
        for j in graph.keys():
            if func(graph, width, i, j) < func(graph, width-1, i, j):
                flag = True
                bad_i = i
                bad_j = j
                break
    if flag:
        path = func(graph, width, bad_i, bad_j)[1]
        for i in range(len(path)):
            for j in range(len(path)):
                if path[j] == path[i] and i != j:
                    return path[i:j + 1]
    else:
        return None
