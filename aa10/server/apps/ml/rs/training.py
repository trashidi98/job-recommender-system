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

#from ipynb.fs.full.MLDRS_preprocessing import remove_punc, tokenization, remove_stopwords, lemmization, cleanResume, preprocessing, TokenizeLemm
#from ipynb.fs.full.MLDRS_tools import createList, find_optimal_clusters, plot_tsne_pca

    # nltk.download('stopwords')
    # stopwords = nltk.corpus.stopwords.words('english')
    # nltk.download('wordnet')
    # nltk.download('punkt')

    # wordnet_lemmatizer = WordNetLemmatizer()
    # wpt = nltk.WordPunctTokenizer()
    # lemmatizer = nltk.WordNetLemmatizer()

    # ### Loading Data - Point to directories 

    # # Create a SQL connection to our SQLite database
    # con = sqlite3.connect(r'/Users/saimamunir/Desktop/Capstone/backend/Recommender_System/all_jobs.db')

    # # creating cursor
    # cur = con.cursor()

    # sql_query = pd.read_sql_query ('''
    #                                 SELECT *
    #                                     FROM job_descriptions_table
    #                             ''', con)
    # jobs = pd.DataFrame(sql_query, columns = ['job_title', 'category', 'company_name', 'inferred_city', 'inferred_state',
    #     'inferred_country','job_description', 'job_type'])

    # # Close the connection
    # con.close()

    # # Create a SQL connection to our SQLite database
    # con2 = sqlite3.connect(r'/Users/saimamunir/Desktop/Capstone/backend/Recommender_System/resume.db')

    # # creating cursor
    # cur2 = con2.cursor()
    # sql_query2 = pd.read_sql_query ('''
    #                                 SELECT *
    #                                     FROM resume
    #                             ''', con2)
    # resumes = pd.DataFrame(sql_query2, columns = ['user_resume'])

    # # Close the connection
    # con2.close()
    # #jobs = pd.read_csv(r'/Users/saimamunir/Desktop/Capstone/backend/Recommender_System/all_jobs.csv')
    # #resumes = pd.read_csv(r'/Users/saimamunir/Desktop/Capstone/backend/Recommender_System/resume.csv')

    # ### PREPROCESSING

    # def remove_punc(corpus):
    #     punc_free = "".join([i for i in corpus if i not in string.punctuation])
    #     return punc_free

    # def tokenization(corpus):
    #     tokens = wpt.tokenize(corpus)
    #     return tokens

    # def remove_stopwords(corpus):
    #     output = [i for i in corpus if i not in stopwords]
    #     return output

    # def lemmization(corpus):
    #     lemm = [wordnet_lemmatizer.lemmatize(word) for word in corpus]
    #     return lemm

    # def cleanResume(corpus):
    #     corpus = re.sub('httpS+s*', ' ', corpus)  # remove URLs
    #     corpus = re.sub('RT|cc', ' ', corpus)  # remove RT and cc
    #     corpus = re.sub('#S+', '', corpus)  # remove hashtags
    #     corpus = re.sub('@S+', '  ', corpus)  # remove mentions
    #     corpus = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~•’"""), ' ', corpus)  # remove punctuations
    #     return corpus

    # def preprocessing(resumes):
    #     resumes['cleaned'] = resumes.apply(lambda x: cleanResume(x))
    #     print("Cleaned corpus")
    #     resumes['cleaned'] = resumes['cleaned'].apply(lambda x:remove_punc(x))
    #     print("Removed punctuation")
    #     resumes['cleaned'] = resumes['cleaned'].apply(lambda x:x.lower())
    #     print("Lowercase")
    #     resumes['cleaned'] = resumes['cleaned'].apply(lambda x:tokenization(x))
    #     print("Tokenized corpus")
    #     resumes['cleaned'] = resumes['cleaned'].apply(lambda x:remove_stopwords(x))
    #     print("Removed Stopwords")
    #     resumes['cleaned'] = resumes['cleaned'].apply(lambda x:lemmization(x))
    #     print("Lemmatized corpus")
    #     resumes.head()
    #     return resumes

    # def TokenizeLemm(corpus_list):

    #     #Tokenise the corpus
    #     tokenized_corp = [word_tokenize(i) for i in corpus_list]

    #     # Create Dictionary
    #     id2word = corpora.Dictionary(tokenized_corp)

    #     #Remove words that don't feature 20 times and those that feature in over 50% of documents
    #     id2word.filter_extremes(no_below=20, no_above=0.5, keep_n=80000)

    #     texts = tokenized_corp

    #     # Term Document Frequency
    #     corpus_final = [id2word.doc2bow(text) for text in texts]
        
    #     return corpus_final, id2word, texts

    # ### Other Tools
    # def createList(corpus):
    #     corpus_list = []
    #     for i in range (len(corpus)):
    #         temp = []
    #         for word in (corpus[i]):
    #             temp.append(word)
    #         temp = " ".join(temp)
    #         corpus_list.append(temp)
    #     return corpus_list

    # def similarity(resume_topics, job_topics):
        
    #     weights = [0.25, 0.18, 0.15, 0.13, 0.11, 0.09, 0.05, 0.04]
    #     distribution = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
        
    #     accuracy_lst = []
    #     for topic in resume_topics:
    #         if topic not in job_topics:
    #             accuracy_lst.append(0)
    #         else:
    #             current_weight = weights[resume_topics.index(topic)]
    #             job_index = job_topics.index(topic)
    #             resume_index = resume_topics.index(topic)
    #             temp = abs(job_index - resume_index)
    #             distrib_num = distribution[temp]
    #             accuracy_lst.append(distrib_num*current_weight)

    #     return (((round((sum(accuracy_lst)),2)*100)))

    # # How many jobs and resumes
    # print("Number of jobs: " + str(jobs.shape[0]))

    # # We are only running our model based on the job description
    # jobs_desc = jobs['job_description'].copy()
    # corpus = preprocessing(jobs_desc)
    # corpus = jobs_desc['cleaned'].tolist()   

    # corpus_list = createList(corpus)
    # corpus_final, id2word, texts = TokenizeLemm(corpus_list)

    # dataframe = pd.DataFrame(corpus_list)
    # dataframe.columns = ["Description"]

    # tfidf = TfidfVectorizer(
    #     min_df = 5,
    #     max_df = 0.95,
    #     max_features = 2000,
    #     stop_words = 'english'
    # )
    # tfidf.fit(dataframe.Description)
    # text = tfidf.transform(dataframe.Description)

    # # Actual LDA model
    # lda_model = gensim.models.LdaMulticore(corpus=corpus_final,
    #                                     id2word=id2word,
    #                                     num_topics=12, 
    #                                     random_state=100,
    #                                     chunksize=100,
    #                                     passes=10,
    #                                     per_word_topics=True)


    # # Compute Coherence Score
    # coherence_model_lda = CoherenceModel(model=lda_model, texts=texts, dictionary=id2word, coherence='c_v')

    # # Print the Keyword in the 10 topics
    # pprint(lda_model.print_topics())
    # doc_lda = lda_model[corpus_final]

    # topics_list = []
    # count = 0
    # for document in corpus_final:
    #     count = count+1
    #     topics = lda_model[document]
    #     topics_list.append(topics[0])
    #     if(count%1000 == 0):
    #         print("Done: " + str(int(count / len(corpus_final) * 100)) + "%")

    # #resumes = resumes.drop(columns=['Unnamed: 0'])
    # #resumes.head()
    # resume = resumes.iloc[0]

    # resume1 = remove_punc(resume)
    # resume1 = tokenization(resume1)
    # resume1 = remove_stopwords(resume1)
    # resume1 = lemmization(resume1)

    # dct = Dictionary([resume1])
    # resume_updated = dct.doc2bow(resume1)

    # resume_topics = lda_model[resume_updated]
    # print(resume_topics[0])

    def test(s):
        return(s)

    