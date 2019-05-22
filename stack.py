#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StackOverflowError(RuntimeError):
    pass


class StackIsEmptyError(RuntimeError):
    pass


class Stack:
    def __init__(self, size):
        self.storage = [0] * size
        self.size = size
        self.head = -1


    def push(self, n):
        if(self.head + 1 < self.size):
            self.head += 1
            self.storage[self.head] = n            
        else: 
            raise StackOverflowError()            


    def pop(self):
        if(self.head > -1):
            popping = self.storage[self.head]
            self.storage[self.head] = 0
            self.head -= 1
            return(popping)
        else: raise StackIsEmptyError()        


    def __len__(self):
        return(self.head+1)
