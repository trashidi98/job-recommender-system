import pandas as pd
import sqlite3
import string
import nltk
import re
import matplotlib.pyplot as plt
import gensim.corpora as corpora
import gensim
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from pprint import pprint
import numpy as np
from gensim.models import Phrases, CoherenceModel
from nltk.tokenize import word_tokenize
from gensim.test.utils import datapath
from sklearn.cluster import MiniBatchKMeans, KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.cm as cm
from sklearn.manifold import TSNE
from gensim.corpora import Dictionary
import pickle
from gensim.test.utils import datapath

class RecommenderSystem:

    def test(s):
        return(s)

    def bestjobs_computations(resume):

        nltk.download('stopwords')
        stopwords = nltk.corpus.stopwords.words('english')
        nltk.download('wordnet')
        nltk.download('punkt')

        wordnet_lemmatizer = WordNetLemmatizer()
        wpt = nltk.WordPunctTokenizer()
        lemmatizer = nltk.WordNetLemmatizer()

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
            # key is set to sort using second element of sublist lambda has been used 
            tup.sort(key = lambda x: x[1], reverse = True) 
            return tup 

        def similarity(resume_topics, job_topics):
    
            weights = [0.25, 0.18, 0.15, 0.13, 0.11, 0.09, 0.05, 0.04]
            distribution = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
            
            accuracy_lst = []
            for topic in resume_topics:
                if topic not in job_topics:
                    accuracy_lst.append(0)
                else:
                    current_weight = weights[resume_topics.index(topic)]
                    job_index = job_topics.index(topic)
                    resume_index = resume_topics.index(topic)
                    temp = abs(job_index - resume_index)
                    distrib_num = distribution[temp]
                    accuracy_lst.append(distrib_num*current_weight)

            return (((round((sum(accuracy_lst)),2)*100)))

        with open('./model', 'rb') as f:
            lda_model = pickle.load(f)

        with open('C://Users//zesha//Desktop//jobs', 'rb') as f:
            corpus = pickle.load(f)

        resume = resume

        resume1 = remove_punc(resume)
        resume1 = tokenization(resume1)
        resume1 = remove_stopwords(resume1)
        resume1 = lemmization(resume1)

        dct = Dictionary([resume1])
        resume_updated = dct.doc2bow(resume1)
        resume_topics = lda_model[resume_updated]
        resume_topics = (Sort_Tuple(resume_topics[0])) 

        # corpus reduction script

        similarity_list = []

        for i in range (len(corpus)):
            resume_temp = []
            job_temp = []
            for key, value in resume_topics:
                resume_temp.append(key)
            for key, value in corpus.iloc[i]['Topics']:
                job_temp.append(key)
                
            similarity_val = similarity(resume_temp, job_temp)
            similarity_list.append((similarity_val))
            
        corpus['Similarity'] = similarity_list

        topNindexes = sorted(range(len(similarity_list)), key=lambda i: similarity_list[i], reverse=True)[:5]
        top_5_idx = np.argsort(similarity_list)[-5:]
        top_5_values = [similarity_list[i] for i in top_5_idx]
        new_corpus_vals = corpus.index[topNindexes]
        topN = corpus.loc[new_corpus_vals]

        return(topN)
    
