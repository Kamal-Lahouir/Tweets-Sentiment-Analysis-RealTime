#!/bin/bash

# the default node number is 3
N=${1:-3}


# start hadoop master container
docker rm -f hadoop-master &> /dev/null
echo "start hadoop-master container..."
docker run -itd \   
            -v ~/Documents/hadoop_project/:/shared_volume \
            --net=hadoop \
            --expose 22 \
            -p 50070:50070 \
            -p 8088:8088 \
            -p 8889:8888 \
            -p 7077:7077 \
            -p 8080:8080 \
            -p 16010:16010 \
            --name hadoop-master \
            --hostname hadoop-master \
            hadoop-spark-cluster


# start hadoop slave container
i=1
while [ $i -lt $N ]
do
	docker rm -f hadoop-slave$i &> /dev/null
	echo "start hadoop-slave$i container..."
	docker run -itd \
                --net=hadoop \
                --expose 22 \
                -p 804$i:804$(($i+1)) \
	            --name hadoop-slave$i \
	            --hostname hadoop-slave$i \
	            hadoop-spark-cluster
	i=$(( $i + 1 ))
done 

# get into hadoop master container
docker exec -it hadoop-master bash