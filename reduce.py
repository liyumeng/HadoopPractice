#!/usr/bin/env python  
# vim: set fileencoding=utf-8  
import sys  
from itertools import groupby  
from operator import itemgetter  
import numpy as np
  
def read_from_mapper(file):  
    for line in file:  
        items=line.strip().split('\t',1)
        if len(items)==1:
            yield items[0],''
        else:
            yield items[0],items[1] 

def main():
    data = read_from_mapper(sys.stdin)
    f_cluster_vec=open('./cluster.vec','w')
    for gid, group in groupby(data, itemgetter(0)):
        words=[]
        aver_vec=np.zeros((100,))
        for word_line in group:
            if len(word_line[1])==0:
                continue
            items=word_line[1].split(' ')
            word=items[0]
            vec=items[1:]
            words.append(word)
            for i in range(100):
                aver_vec[i]+=float(vec[i])
        cnt=len(words)
        for i in range(100):
            aver_vec[i]/=cnt
        print("%s\t%s"%(gid,'\t'.join(words)))
        f_cluster_vec.write('%s %s\n'%(gid,' '.join([str(v) for v in aver_vec])))
    f_cluster_vec.close()
if __name__ == '__main__':  
    main()  
