/usr/local/hadoop/bin/hdfs namenode -format
start-dfs.sh
start-yarn.sh
cd TP_Hadoop/wordcount/
hadoop fs -mkdir -p input
hadoop fs -put dracula input
hadoop fs -ls input
export STREAMINGJAR='/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar'

