if __name__ == '__main__':

    from multiprocessing import freeze_support
    import pandas as pd
    import string
    import nltk
    import re
    import matplotlib.pyplot as plt
    import gensim.corpora as corpora
    import gensim
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from gensim.models import Phrases, CoherenceModel
    from nltk.tokenize import word_tokenize
    from gensim.test.utils import datapath

    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')
    nltk.download('wordnet')
    nltk.download('punkt')

    wordnet_lemmatizer = WordNetLemmatizer()
    wpt = nltk.WordPunctTokenizer()
    lemmatizer = nltk.WordNetLemmatizer()

    # Point to directories 
    jobs = pd.read_csv(r"./all_jobs_train.csv")
    resumes = pd.read_csv(r"./all_resumes.csv")

    # How many jobs and resumes
    print("Number of jobs: " + str(jobs.shape[0]))
    print("Number of resumes: " + str(resumes.shape[0]))

    # We are only running our model based on the job description
    jobs_desc = jobs['job_description'].copy()

    ####### PREPROCESSING #######
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

    def cleanResume(corpus):
        corpus = re.sub('httpS+s*', ' ', corpus)  # remove URLs
        corpus = re.sub('RT|cc', ' ', corpus)  # remove RT and cc
        corpus = re.sub('#S+', '', corpus)  # remove hashtags
        corpus = re.sub('@S+', '  ', corpus)  # remove mentions
        corpus = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""), ' ', corpus)  # remove punctuations
        return corpus

    def preprocessing(resumes):
        resumes['cleaned'] = resumes.apply(lambda x: cleanResume(x))
        print("Cleaned corpus")
        resumes['cleaned'] = resumes['cleaned'].apply(lambda x:remove_punc(x))
        print("Removed punctuation")
        resumes['cleaned'] = resumes['cleaned'].apply(lambda x:x.lower())
        print("Lowercase")
        resumes['cleaned'] = resumes['cleaned'].apply(lambda x:tokenization(x))
        print("Tokenized corpus")
        resumes['cleaned'] = resumes['cleaned'].apply(lambda x:remove_stopwords(x))
        print("Removed Stopwords")
        resumes['cleaned'] = resumes['cleaned'].apply(lambda x:lemmization(x))
        print("Lemmatized corpus")
        resumes.head()
        return resumes

    corpus = preprocessing(jobs_desc)
    corpus = jobs_desc['cleaned'].tolist()   

    

    corpus_list = []
    for i in range (len(corpus)):
        temp = []
        for word in (corpus[i]):
            temp.append(word)
        temp = " ".join(temp)
        corpus_list.append(temp)
        
    #Tokenise the corpus
    tokenized_corp = [word_tokenize(i) for i in corpus_list]

    # Create Dictionary
    id2word = corpora.Dictionary(tokenized_corp)

    #Remove words that don't feature 20 times and those that feature in over 50% of documents
    id2word.filter_extremes(no_below=20, no_above=0.5)

    texts = tokenized_corp

    # Term Document Frequency
    corpus_final = [id2word.doc2bow(text) for text in texts]

    ####### ACTUAL LDA MODEL #######
    def compute_coherence_values(corpus, dictionary, texts, start, end, step):
        coherence_values = []
        model_list = []
        
        for num_topics in range(start, end, step):

            # Build LDA model
            lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                                num_topics=20, 
                                                id2word=dictionary,
                                                chunksize=500,
                                                alpha='symmetric',
                                                random_state=100,
                                                iterations=10,
                                                passes=100, 
                                                workers=None,
                                                per_word_topics=True)
            model_list.append(lda_model)
            
            # Compute Coherence Score
            coherence_model_lda = CoherenceModel(model=lda_model, texts=texts, dictionary=dictionary, coherence='c_v')
            coherence_values.append(coherence_model_lda.get_coherence())

            # Save model to disk.
            temp_file = datapath("./model")
            lda_model.save(temp_file)
        

        return model_list, coherence_values

    ####### TRAINING #######

    model_list, coherence_values = compute_coherence_values(corpus=corpus_final, dictionary = id2word, texts=texts, start=0, end=20, step=1)

    # SSE Plot to determine distinct number of topics
    end=20; start=0; step=1
    x = range(start, end, step)
    ax = plt.subplots(figsize=(8,8))
    plt.plot(x, coherence_values)
    plt.xlabel("Number of Topics", fontsize=14)
    plt.ylabel("Coherence score", fontsize=14)
    plt.title('Coherence Scores for Topic Size', fontsize=18)
    plt.grid()
    plt.show()