#!/bin/bash
#关闭非当前操作的所有pts连接

cur=`who am i | awk '{print $2}'`
vpts=`who | grep lf | awk '{print $2}'`

count=0
for pts in ${vpts[@]}
do
	if [ $pts != $cur ]
	then
		cmd="pkill -kill -t $pts"
		$($cmd)
		count=$(($count+1))
	fi
done
printf "Total close pts count:\e[32;40m"$count"\e[0m\n"
