#!/usr/bin/env python
import os
from kafka import KafkaConsumer
from pyspark.sql import SparkSession
from pyspark import SparkContext
import json
import Paths
class Consumer():
    def __init__(self):
       self.kafkaConsumer = KafkaConsumer(
           bootstrap_servers=Paths.SERVER,
           auto_offset_reset = 'earliest',
           consumer_timeout_ms = 1000,
           value_deserializer=bytes.decode
          )
    
    def hamData(self):
        self.kafkaConsumer.subscribe([Paths.HAM_TOPIC])
 
        sparkSession = SparkSession.builder.appName("Spamfilter").getOrCreate()
        values = []
        for c in self.kafkaConsumer:
            values.append(c.value)
        rdd = sparkSession.sparkContext.parallelize(values)
        rdd.saveAsTextFile(Paths.HDFS_HAM_DATA_PATH)
        self.kafkaConsumer.close()

    def spamData(self):
        self.kafkaConsumer.subscribe([Paths.SPAM_TOPIC])
        sparkSession = SparkSession.builder.appName("Spamfilter").getOrCreate()
        values = []
        for c in self.kafkaConsumer:
            values.append(c.value)
        rdd = sparkSession.sparkContext.parallelize(values)
        rdd.saveAsTextFile(Paths.HDFS_SPAM_DATA_PATH)
        self.kafkaConsumer.close()
        
   

def main():
        hamConsumer = Consumer()
        hamConsumer.hamData()
        spamConsumer = Consumer()
        spamConsumer.spamData()
    
if __name__ == '__main__':
        main()