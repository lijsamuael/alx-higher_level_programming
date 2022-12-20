#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if (self.__head is None):
            self.__head = Node(value)
            return

        if (value < self.__head.data):
            self.__head = Node(value, self.__head)
            return

        tmp = self.__head
        while (tmp is not None):
            if tmp.next_node is None:
                tmp.next_node = Node(value)
                return

            if (value < tmp.next_node.data):
                tmp.next_node = Node(value, tmp.next_node)
                return

            tmp = tmp.next_node

    def __str__(self):
        out = ""
        tmp = self.__head
        while (tmp is not None):
            out += str(tmp.data) + ("\n" if tmp.next_node is not None else "")
            tmp = tmp.next_node
        return out
