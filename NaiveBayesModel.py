from DataLoader import *
from Preprocess import *
import random

from operator import is_not
from nltk import NaiveBayesClassifier, classify
from functools import partial
class NaiveBayesModel:
    def run(self):
        spam = DataLoader.getSpamDataFromHDFS(self)
        ham = DataLoader.getHamDataFromHDFS(self)
        features_spam = [(Preprocess.get_features(self,email,''),'spam') for (email) in spam ]
        features_ham = [(Preprocess.get_features(self,email,''),'ham') for (email) in ham ]
        features = features_ham + features_spam
        random.shuffle(features)
        train_set,test_set,classifier = self.train(features,0.8)
        self.evaluate(train_set, test_set, classifier)

    def train(self,features,samples_proportion):
        train_size = int(len(features) * samples_proportion)
        train_set,test_set = features[:train_size],features[train_size:]
        print('Training set size = ' + str(len(train_set))+ ' emails')
        print('Test set size= ' + str(len(test_set)) + ' emails')
        classifier = NaiveBayesClassifier.train(train_set)
        return train_set,test_set,classifier
        
    def evaluate(self,train_set, test_set, classifier):
        print ('Accuracy on the training set = ' + str(classify.accuracy(classifier, train_set)))
        print ('Accuracy of the test set = ' + str(classify.accuracy(classifier, test_set)))
        classifier.show_most_informative_features(20)

def main():
    nb = NaiveBayesModel()
    nb.run()

if __name__ == '__main__':
    main()
