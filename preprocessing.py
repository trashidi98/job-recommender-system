import pandas as pd
import string
import nltk
import re
import unidecode
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

from gensim.models import Phrases

resumes = pd.read_csv(r"C:\Users\zesha\Desktop\UpdatedResumeDataSet.csv", encoding = "ISO-8859-1")

def remove_punc(corpus):
    punc_free = "".join([i for i in corpus if i not in string.punctuation])
    return punc_free

def tokenization(corpus):
    tokens = re.split('W+',corpus)
    return tokens

def remove_stopwords(corpus):
    output = [i for i in corpus if i not in stopwords]
    return output

wordnet_lemmatizer = WordNetLemmatizer()

def lemmization(corpus):
    lemm = [wordnet_lemmatizer.lemmatize(word) for word in corpus]
    return lemm

def cleanResume(resumeText):
    resumeText = re.sub('httpS+s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^x00-x7f]',r' ', resumeText) 
    resumeText = re.sub('s+', ' ', resumeText)  # remove extra whitespace
    return resumeText

resumes['cleaned_resume'] = resumes.Resume.apply(lambda x: cleanResume(x))

del resumes["Category"]
del resumes["Resume"]

resumes['cleaned_resume'] = resumes['cleaned_resume'].apply(lambda x:remove_punc(x))
resumes['cleaned_resume'] = resumes['cleaned_resume'].apply(lambda x:x.lower())
resumes['cleaned_resume'] = resumes['cleaned_resume'].apply(lambda x:tokenization(x))
resumes['cleaned_resume'] = resumes['cleaned_resume'].apply(lambda x:remove_stopwords(x))
resumes['cleaned_resume'] = resumes['cleaned_resume'].apply(lambda x:lemmization(x))
resumes.head()
