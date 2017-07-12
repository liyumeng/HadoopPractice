#!/bin/bash  
  
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input wiki.output cluster.vec -output cluster.txt -file map.py -file reduce.py \
 -mapper "python map.py" -reducer "python reduce.py" -jobconf mapred.reduce.tasks=1 -jobconf mapred.job.name="kmeans_test" 
