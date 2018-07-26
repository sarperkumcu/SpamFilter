from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
class Preprocess:
    def preprocess(self,sentence):
        tokens = word_tokenize(sentence.decode(errors='replace'))
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(word.lower()) for word in tokens]

    def get_features(self,text,setting):
        stoplist = stopwords.words('english')
        if setting == 'bow':
             return {word: count for word, count in Counter(Preprocess.preprocess(self,text)).items() if not word in stoplist}
        else:
            return {word: True for word in Preprocess.preprocess(self,text) if not word in stoplist}
