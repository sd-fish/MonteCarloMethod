#!/usr/bin/env python
#!ecoding=utf8

from random import uniform

def get_hypotenuse():
    x = uniform(0, 1)
    y = uniform(0, 1)
    z = x ** 2 + y ** 2
    return z

def get_pai(samples):
    count = 0
    for i in xrange(samples):
        if get_hypotenuse() <= 1:
            count += 1
        if i % (samples / 100) == 0:
            print "calculating %f%%:" %(i * 100.0 / samples)
    pai = count * 4.0 / samples
    return pai

if __name__ == "__main__":
    #print get_pai(1000)
    #print get_pai(10000)
    #print get_pai(100000)
    #print get_pai(1000000)
    print get_pai(10000000)
