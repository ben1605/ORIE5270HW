import numpy as np


class Tree(object):

    def __init__(self, root):
        self.root = root

    @staticmethod
    def get_value_root(self):
        if self.root is not None:
            return self.root.value
        else:
            return None

    def get_tree(self):
        delimiter = "|"
        plot = []
        if self is not None:
            if self.root.left is not None:
                le = Tree(self.root.left).get_tree()
            else:
                le = [["#"]]
            if self.root.right is not None:
                r = Tree(self.root.right).get_tree()
            else:
                r = [["#"]]
        if len(le) < len(r):
            c1 = 0
            ll = [[delimiter for i in range(len(r[0]))]for j in range(len(r))]
            ltemp = np.reshape(le, (len(le)*len(le[0])))
            ltemp1 = []
            for i in range(len(ltemp)):
                if ltemp[i] != delimiter:
                    ltemp1.append(ltemp[i])
            for i in range(len(le)):
                for j in range(len(r[0])):
                    if r[i][j] != delimiter:
                        ll[i][j] = ltemp1[c1]
                        c1 += 1
            le = ll
        elif len(le) > len(r):
            c2 = 0
            rr = [[delimiter for i in range(len(le[0]))]for j in range(len(le))]
            rtemp = np.reshape(r, (len(r)*len(r[0])))
            rtemp1 = []
            for i in range(len(rtemp)):
                if rtemp[i] != delimiter:
                    rtemp1.append(rtemp[i])
            for i in range(len(r)):
                for j in range(len(le[0])):
                    if le[i][j] != delimiter:
                        rr[i][j] = rtemp1[c2]
                        c2 += 1
            r = rr
        plot = le
        for i in range(len(le)):
            for j in range(len(r[0])):
                plot[i].append(r[i][j])
        temp = int(len(plot[0])/2)
        for i in range(len(le)):
            plot[i].insert(temp, delimiter)
        plot.insert(0, [])
        for i in range(len(plot[1])):
            plot[0].insert(0, delimiter)
        plot[0][temp] = self.get_value_root(self)
        return plot

    def print_tree(self):
        delimiter = "|"
        flag = True
        res = self.get_tree()
        for i in range(len(res[0])):
            if res[len(res) - 1][i] != delimiter and res[len(res) - 1][i] != "#":
                flag = False
        length = len(res[0])
        if flag:
            res = np.array(res)[0:len(res) - 1, 1:length - 1]
            res = res[:, np.arange(0, len(res[0]), 2)]
        for i in range(len(res)):
            for j in range(len(res[0])):
                if res[i][j] == "#":
                    res[i][j] = delimiter
        # for i in range(len(res)):
        #     print(*res[i])
        print(res)
        res = list(res)
        for i in range(len(res)):
            res[i] = list(res[i])
        return res


class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


if __name__ == '__main__':
    a = Node(2, None, None)
    e = Node(1, None, None)
    b = Node(3, e, None)
    c = Node(4, b, e)
    c = Tree(c)
    c.print_tree()
