import os
import typing

class Node:
    def __init__(self, left : "Node", right : "Node", v : int, name : bytes):
        self.left = left
        self.right = right
        self.v = v
        self.name = name

    def __str__(self):
        return "name = " + str(self.name) + "\n" \
                                            "v = " + str(self.v) + "\n" \
                                                                   "left= " + str(self.left) + "\n" \
                                                                                               "right " + str(self.right)
    def __repr__(self):
        return str(self)

huffman_codes = {}
counter = 0

with open("input.txt", "rb") as f:
    while True:
        read_byte = f.read(1)
        if not read_byte:
            break

        counter += 1
        if read_byte in huffman_codes:
            huffman_codes[read_byte] += 1
        else:
            huffman_codes[read_byte] = 1

for e in huffman_codes.keys():
    huffman_codes[e] = huffman_codes[e] / counter

huffman_nodes = {}
for i in huffman_codes.items():
    huffman_nodes[i[0]] = Node(None, None, i[1], i[0])

sorted_dict = dict(sorted(huffman_nodes.items(), key=lambda item: item[1].v))

while len(sorted_dict) != 1:
    it = iter(sorted_dict.items())
    first = next(it)
    second = next(it)
    sorted_dict.pop(first[0])
    sorted_dict.pop(second[0])
    sorted_dict[first[0] + second[0]] = Node(first[1], second[1], first[1].v + second[1].v, first[0] + second[0])
    sorted_dict = dict(sorted(sorted_dict.items(), key=lambda item: item[1].v))

for i in sorted_dict.values():
    print(i.left)