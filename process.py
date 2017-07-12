f=open('wiki.output')
dst=open('cluster.vec','w')
for i in range(5):
  items=f.readline().split(' ')
  items[0]=str(i+1)  
  dst.write(' '.join(items))
dst.close()
f.close()

