#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testmemoizing.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 13:20:44 2019
# Description: 
#************************************************************************#


import time
import hashlib
import pickle
from itertools import chain
cache = {}

def is_obsolete(entry, duration):
    return time.time() - entry['time']> duration

def compute_key(function, args, kw):
    key = pickle.dumps((function.func_name, args, kw))
    return hashlib.sha1(key).hexdigest()

def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)

            if (key in cache and not is_obsolete(cache[key], duration)):
                print 'we got a winner'
                return cache[key]['value']

            result = function(*args, **kw)

            cache[key] = {'value':result, 'time':time.time()}
            return result
        return __memoize
    return _memoize

@memoize()
def very_very_very_complex_stuff(a, b):
    return a + b

print '======================================='
print very_very_very_complex_stuff(2, 2)
print '======================================='
print very_very_very_complex_stuff(2, 2)
print '======================================='

@memoize(1) #1s drop
def very_very_very_complex_stuff1(a, b):
    return a + b

print '======================================='
print very_very_very_complex_stuff1(2, 2)
print '======================================='
print very_very_very_complex_stuff1(2, 2)
print '======================================='
