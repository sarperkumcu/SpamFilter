#!/usr/bin/env python
import threading, logging, time
import multiprocessing
import json
from kafka import KafkaProducer
from pyspark import SparkContext, SparkConf
import re
from pyspark.streaming import StreamingContext
import os
import Paths
class Producer():
    def __init__(self):
       self.kafkaProducer = KafkaProducer(
           bootstrap_servers=Paths.SERVER,
           value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def getHam(self):
        file_list = os.listdir(Paths.HAM_DATA)

        for a_file in file_list:
            with open(Paths.HAM_DATA+a_file,errors="ignore") as f:
                texts = f.read()
                self.kafkaProducer.send(Paths.HAM_TOPIC,texts)

    def getSpam(self):
        file_list = os.listdir(Paths.SPAM_DATA)

        for a_file in file_list:
            with open(Paths.SPAM_DATA +a_file,errors="ignore") as f:
                texts = f.read()
                self.kafkaProducer.send(Paths.SPAM_TOPIC,texts)

    


# you may also want to remove whitespace characters like `\n` at the end of each line
     
            
        self.kafkaProducer.close()

def main():
    producer = Producer()
    producer.getHam()
    producer.getSpam()

if __name__ == '__main__':
    main()