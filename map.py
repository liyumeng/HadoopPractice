#!/usr/bin/env python  
# vim: set fileencoding=utf-8  
import sys  
import numpy as np
  
def read_from_input(file):  
    for line in file:
        yield line.rstrip()

def load_config(filename):
    clusters={}
    with open(filename) as f:
        for line in f:
            items=line.strip().split(' ')
            clusters[items[0]]=[float(v) for v in items[1:]]
    return clusters

def distance(vec1,vec2):
    return np.dot(vec1,vec2)/np.sqrt(np.dot(vec1,vec1)*np.dot(vec2,vec2))

def main():  
    data = read_from_input(sys.stdin)
    clusters = load_config('./cluster.vec')
    for line in data:
        items=line.split(' ')
        word=items[0]
        vec=[float(v) for v in items[1:]]
        min_key=''
        min_val=1000000
        for key in clusters:
            d=distance(clusters[key],vec)
            if d < min_val:
                min_val=d
                min_key=key
        print('%s%s%s'%(min_key,'\t',line))

if __name__ == '__main__':
    main()
