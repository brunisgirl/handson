import math
import sys

path = []

class Node:
    path = []
    paths = []
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
        if self.data:
            if self.left is None:
                if data[1] is not None:
                    self.left = Node(data[1][0])
                    self.left.insert(data[1])
                else:
                    return

            if self.right is None:
                if data[2] is not None:
                    self.right = Node(data[2][0])
                    self.right.insert(data[2])
                else:
                    return
        else:
            return  # an empty tree

    def traverse(self, left, right):
        if self.data:
            Node.path.append(self.data)
            Node.paths.append(list(Node.path))
            if self.left is None and self.right is None:
                del Node.path[-1]
                return

            if self.left is not None:
                self.left.traverse(left.left, left.right)


            else:
                del Node.path[-1]

            if self.right is not None:
                self.right.traverse(right.left, right.right)
                del Node.path[-1]
            else:
                del Node.path[-1]

        else:
            del Node.path[-1]
            return  # an empty tree



def solution(T):
    tree = Node(T[0])
    tree.insert(T[1], T[2])

def main():
    T = (5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
    tree = Node(T[0])
    tree.insert(T)
    tree.traverse(tree.left, tree.right)
    count = 0
    for i in tree.paths:
        if sorted(i) == i:
            count +=1
    print(tree.paths)
    print(count)



if __name__ == '__main__':

    main()



