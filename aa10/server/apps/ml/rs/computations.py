import pandas as pd
import string
import nltk
import matplotlib.pyplot as plt
import gensim.corpora as corpora
import gensim
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from pprint import pprint
import numpy as np
from gensim.models import Phrases, CoherenceModel
from nltk.tokenize import word_tokenize
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.cm as cm
from sklearn.manifold import TSNE
from gensim.corpora import Dictionary
import pickle
from gensim.test.utils import datapath

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
newStopWords = ['u','www','com','ca','xa0','b','age', 'color', 'national', 'origin', 'citizenship', 'physical', 'mental', 'disability', 'race', 'religion', 'creed', 'gender', 'sex', 'sexual', 'orientation', 'gender', 'identity', 'expression', 'genetic', 'marital','veteran']
stopwords.extend(newStopWords)
nltk.download('wordnet')
nltk.download('punkt')

wordnet_lemmatizer = WordNetLemmatizer()
wpt = nltk.WordPunctTokenizer()
lemmatizer = nltk.WordNetLemmatizer()

def similarity(resume_topics, job_topics):
    
    weights = [0.25, 0.18, 0.15, 0.13, 0.11, 0.09, 0.05, 0.04]
    distribution = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
    
    accuracy_lst = []
    for topic in resume_topics:
        if topic not in job_topics:
            accuracy_lst.append(0)
        else:
            if (resume_topics.index(topic)>=0 and resume_topics.index(topic)<8):
                    current_weight = weights[resume_topics.index(topic)]
                    resume_index = resume_topics.index(topic)
            if (job_topics.index(topic)>=0 and job_topics.index(topic)<8):
                    job_index = job_topics.index(topic)
            if (resume_topics.index(topic)>=0 and resume_topics.index(topic)<8 and job_topics.index(topic)>=0 and job_topics.index(topic)<8):
                    temp = abs(job_index - resume_index)

                    if (temp>=0 and temp<8):
                        distrib_num = distribution[temp]
                        accuracy_lst.append(distrib_num*current_weight)

    return (((round((sum(accuracy_lst)),2)*100)))

def TokenizeLemm(corpus_list):

    #Tokenise the corpus
    tokenized_corp = [word_tokenize(i) for i in corpus_list]

    # Create Dictionary
    id2word = corpora.Dictionary(tokenized_corp)

    #Remove words that don't feature 20 times and those that feature in over 50% of documents
    id2word.filter_extremes(no_below=20, no_above=0.5, keep_n=80000)

    texts = tokenized_corp

    # Term Document Frequency
    corpus_final = [id2word.doc2bow(text) for text in texts]
    
    return corpus_final, id2word, texts

def createList(corpus):
    corpus_list = []
    for i in range (len(corpus)):
        temp = []
        for word in (corpus[i]):
            temp.append(word)
        temp = " ".join(temp)
        corpus_list.append(temp)
    return corpus_list

def remove_punc(corpus):
        punc_free = "".join([i for i in corpus if i not in string.punctuation])
        return punc_free

def tokenization(corpus):
    tokens = wpt.tokenize(corpus)
    return tokens

def remove_stopwords(corpus):
    output = [i for i in corpus if i not in stopwords]
    return output

def lemmization(corpus):
    lemm = [wordnet_lemmatizer.lemmatize(word) for word in corpus]
    return lemm

def Sort_Tuple(tup):   
    tup.sort(key = lambda x: x[1], reverse = True) 
    return tup 

def bestjobs_computations(resume, city):

    with open('/home/rasperrylinux/capstone/job-recommender-system/aa10/server/apps/ml/rs/model', 'rb') as f:
        lda_model = pickle.load(f)
        
    with open('/home/rasperrylinux/capstone/job-recommender-system/aa10/server/apps/ml/rs/jobs', 'rb') as f:
        jobs = pickle.load(f)

    resume1 = remove_punc(resume)
    resume1 = tokenization(resume1)
    resume1 = remove_stopwords(resume1)
    resume1 = lemmization(resume1)

    dct = Dictionary([resume1])
    resume_updated = dct.doc2bow(resume1)

    resume_topics = lda_model[resume_updated]

    resume_topics = (Sort_Tuple(resume_topics[0])) 
    
    cityList, citycount = np.unique(list(jobs.loc[:, "inferred_city"]), return_counts = True)

    cities_dict = dict(zip(cityList, citycount))
    
    city_entered = city
    for key,val in cities_dict.items():
        if key.lower() == city_entered.lower():
            new_corpus  = jobs[jobs["inferred_city"] == key]

    if new_corpus.shape[0] < 5:
        print("Not enough data for this location.")
        
    for i in range (len(new_corpus)):
        new_corpus.iloc[i]['Topics'] = Sort_Tuple(new_corpus.iloc[i]['Topics'])
        
    similarity_list = []

    for i in range (len(new_corpus)):
        resume_temp = []
        job_temp = []
        for key, value in resume_topics:
            resume_temp.append(key)
        for key, value in new_corpus.iloc[i]['Topics']:
            job_temp.append(key)

        similarity_val = similarity(resume_temp, job_temp)
        similarity_list.append((similarity_val))

    new_corpus['Similarity'] = similarity_list
    new_corpus = new_corpus.fillna('')
    topNindexes = sorted(range(len(similarity_list)), key=lambda i: similarity_list[i], reverse=True)[:5]
    new_corpus_vals = new_corpus.index[topNindexes]
    topN = new_corpus.loc[new_corpus_vals]
    
    return(topN)