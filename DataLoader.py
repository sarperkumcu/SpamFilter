import os
import random
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import Paths
class DataLoader:
    def init_lists(self,folder):
        a_list = []
        file_list = os.listdir(folder)
        for a_file in file_list:
            with open(folder + a_file, 'rb') as f:
                a_list.append(f.read())
        f.close()
        return a_list

    def getMails(self):
        spam_emails = [(email,'spam') for email in DataLoader.init_lists(self,Paths.SPAM_DATA)]
        ham_emails = [(email,'ham') for email in DataLoader.init_lists(self,Paths.HAM_DATA)]
        all_emails = spam_emails + ham_emails
        random.shuffle(all_emails)
        return all_emails
    

    def getSpamDataFromHDFS(self):
        self.spark = SparkSession \
            .builder \
            .appName("RDD to DF example") \
            .config(conf=SparkConf()) \
            .getOrCreate()
        self.sc = self.spark.sparkContext
        lines = self.sc.textFile(Paths.HDFS_SPAM_DATA_PATH + "*")
        lines = lines.collect()
        return lines

    def getHamDataFromHDFS(self):
        self.spark = SparkSession \
            .builder \
            .appName("RDD to DF example") \
            .config(conf=SparkConf()) \
            .getOrCreate()
        self.sc = self.spark.sparkContext
        lines = self.sc.textFile(Paths.HDFS_HAM_DATA_PATH + "*")
        lines = lines.collect()
        return lines

