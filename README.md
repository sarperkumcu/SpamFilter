## SpamFilter

This project created to cover fundamentals of spark, hadoop and ML.

## Installation
```
git clone https://github.com/sarperkumcu/SpamFilter.git
```

## Installation

-Kafka was used as a pipeline between local file system and hadoop file system. 
-NLTK was used for preprocess and train model.

## Prerequirements

Check out requirements.txt. Also, you will need running hadoop, zookeeper and kafka.

You may check this [topic](https://stackoverflow.com/questions/7225900/how-to-install-packages-using-pip-according-to-the-requirements-txt-file-from-a?answertab=active#tab-top) for download dependencies.


## How to use?

1. Clone this repository to your local file system.
2. Make sure hadoop, kafka and zookeeper is running!

```
python producer.py
```
This command will read txt files from your local system and send as message via kafka.

So, you are able to receive texts via KafkaConsumer and write to HDFS file system.

```
python consumer.py
```

At last, execute below command to train your model.

```
python NaiveBayesModel.py
```

You may need to change Paths.py according to your configurations.


