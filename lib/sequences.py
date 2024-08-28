#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print('[]')
        return
    if length == 1:
        print('[0]')
        return
    if length == 2:
        print('[0, 1]')
        return
    list = [0, 1]
    for i in range(2, length):
        list.append(list[i-1] + list[i-2])
    print(list)