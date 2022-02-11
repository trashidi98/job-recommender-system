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
import numpy as np
from nltk.tokenize import word_tokenize
import matplotlib
import matplotlib.pyplot as plt
import gensim.corpora as corpora
import gensim
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')
from gensim.models import CoherenceModel
wordnet_lemmatizer = WordNetLemmatizer()

# Point to directories 

jobs = pd.read_csv(r"C://Users//zesha//Desktop//all_jobs.csv")
resumes = pd.read_csv(r"C://Users//zesha//Desktop//all_resumes.csv")

# How many jobs and resumes

print("Number of jobs: " + str(jobs.shape[0]))
print("Number of resumes: " + str(resumes.shape[0]))

# We are only running our model based on the job description

jobs_desc = jobs[['job_description']].copy()

### PREPROCESSING

def remove_punc(corpus):
    punc_free = "".join([i for i in corpus if i not in string.punctuation])
    return punc_free

def tokenization(corpus):
    tokens = re.split('W+',corpus)
    return tokens

def remove_stopwords(corpus):
    output = [i for i in corpus if i not in stopwords]
    return output

def lemmization(corpus):
    lemm = [wordnet_lemmatizer.lemmatize(word) for word in corpus]
    return lemm

def cleanResume(resumeText):
    resumeText = re.sub('httpS+s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    #resumeText = re.sub(r'[^x00-x7f]',r' ', resumeText) 
    #resumeText = re.sub('s+', ' ', resumeText)  # remove extra whitespace
    return resumeText

def cleanHTML(resumeText):
    resumeText = CLEANR.sub('', resumeText)
    return resumeText


def preprocessing(resumes):
    
    #resumes['cleaned_resume'] = resumes.resumes.apply(lambda x: cleanHTML(x))
    resumes['cleaned_resume'] = resumes.resumes.apply(lambda x: cleanResume(x))

    #del resumes["Category"]
    #del resumes["Resume"]

    resumes['cleaned_resume'] = resumes['cleaned_resume'].apply(lambda x:remove_punc(x))
    resumes['cleaned_resume'] = resumes['cleaned_resume'].apply(lambda x:x.lower())
    resumes['cleaned_resume'] = resumes['cleaned_resume'].apply(lambda x:tokenization(x))
    resumes['cleaned_resume'] = resumes['cleaned_resume'].apply(lambda x:remove_stopwords(x))
    resumes['cleaned_resume'] = resumes['cleaned_resume'].apply(lambda x:lemmization(x))
    resumes.head()
    return resumes
    
resumes = preprocessing(resumes)
del resumes['Unnamed: 0']
corpus = jobs['job_description']

# This is someone elses's preprocessing, we need to perform ours and link to LDA model

import nltk 

wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')
lemmatizer = nltk.WordNetLemmatizer()

#Function to pre-process the text information

def normalize_document(doc):
    
    # lower case and remove special characters\whitespaces
    doc = re.sub(r'[^a-zA-Z\s]', '', doc, re.I|re.A) #re.I (ignore case), re.A (ASCII-only matching)
    doc = doc.lower()
    doc = doc.strip()
    
    # tokenize document
    tokens = wpt.tokenize(doc)
    
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatise document from filtered tokens
    lem_text = [lemmatizer.lemmatize(i) for i in filtered_tokens]
    
    # Remove words that are only one character.
    lem_text = [token for token in lem_text if len(token) > 1]
    
    # Remove numbers, but not words that contain numbers.
    lem_text = [token for token in lem_text if not token.isnumeric()]
    
    doc = ' '.join(lem_text)
    return doc

normalize_corpus = np.vectorize(normalize_document)

norm_corpus = normalize_corpus(corpus)

from nltk.tokenize import word_tokenize
import gensim.corpora as corpora

#Tokenise the corpus
tokenized_corp = [word_tokenize(i) for i in norm_corpus]

# Create Dictionary
id2word = corpora.Dictionary(tokenized_corp)

#Remove words that don't feature 20 times and those that feature in over 50% of documents
id2word.filter_extremes(no_below=20, no_above=0.5)

texts = tokenized_corp

# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]

# Actual LDA model

def compute_coherence_values(corpus, dictionary, texts, end, start=2, step=3):
    coherence_values = []
    model_list = []
    
    for num_topics in range(start, end, step):
    
        # Build LDA model
        lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                               id2word=dictionary,
                                               num_topics=num_topics, 
                                               random_state=123,
                                               chunksize=100,
                                               passes=500, #number of passes was investigated. At 500 the coherence score will remain relatively similar
                                               #with any further increase. As the document is quite small this number of passes makes sense.
                                               per_word_topics=True)
        model_list.append(lda_model)
        
        # Compute Coherence Score
        coherence_model_lda = CoherenceModel(model=lda_model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherence_model_lda.get_coherence())

    return model_list, coherence_values
    
model_list, coherence_values = compute_coherence_values(corpus=corpus, dictionary = id2word, texts=texts, start=8, end=16, step=1)

# SSE Plot to determine distinct number of topics

end=16; start=8; step=1;
x = range(start, end, step)
ax = plt.subplots(figsize=(8,8))
plt.plot(x, coherence_values)
plt.xlabel("Number of Topics", fontsize=14)
plt.ylabel("Coherence score", fontsize=14)
plt.title('Coherence Scores for Topic Size', fontsize=18)
plt.grid()
plt.show();
