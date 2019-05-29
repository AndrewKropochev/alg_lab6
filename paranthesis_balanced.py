#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stack import Stack

def is_paranthesis_balanced(s):
#    d = {'{':'{}', '}':'{}', '[':'[]', ']':'[]', '(':'()', ')':'()', '<':'<>', '>':'<>'}
    d = {'{':'}', '[':']', '(':')', '<':'>'}
    
    if(len(s) == 0): return(True)
#    if (s[0] == d[s[0]][1]): return(False)
    if (s[0] not in d): return(False)
    
    stack_in = Stack(len(s))
    
    for elem in s:

#        if(elem == d[elem][0]):
        if(elem in d):
            stack_in.push(elem)
        else:
            if(len(stack_in) > 0):
                head = stack_in.pop()
#                if(elem != d[head][1]):
                if(elem != d[head]):
                    return(False)
            else: return(False)
            
    if(len(stack_in) == 0): return(True)
    else: return(False)
            
    
    pass

