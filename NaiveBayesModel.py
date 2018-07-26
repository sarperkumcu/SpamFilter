from DataLoader import *
from Preprocess import *
from nltk import NaiveBayesClassifier, classify
class NaiveBayesModel:
    def run(self):
        spam,ham,total = DataLoader.getMails(self)
        features = [(Preprocess.get_features(self,email,''),label) for (email,label) in total]
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
