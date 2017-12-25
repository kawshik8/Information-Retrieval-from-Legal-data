import os
import enchant
import nltk
from nltk.stem import WordNetLemmatizer
import re
import math
from nltk.corpus import stopwords

# def bow_get():
#     #print(len(bow))

#     f = open("/Users/apple/temp/nltk/task2/bow.txt","r")

#     bow = f.read().splitlines()

#     #print(len(bow))
#     return bow
# bow_get()

# def get_bow1(file):
#     f = open(file,'rb')
#     content = f.read().splitlines()
#     d = enchant.Dict("en_US")
#     bowtemp = []
#     for sentence in content:
#         words = nltk.word_tokenize(str(sentence))
#         for word,pos in nltk.pos_tag(words):
#             if(len(word)>2):
#                 if(pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
#                     word = word.replace('0x96',"")
#                     word = word.replace('.',"")
#                     word = word.replace('0x94',"")
#                     word = WordNetLemmatizer().lemmatize(word.lower())
#                     if(d.check(word)):
#                         if bool(re.search(r'\d', word))==False:
#                             bowtemp.append(word)
    
#     return bowtemp


def read_bow_all():
    f = open("/Users/apple/temp/nltk/task2/verbsbow.txt","r")
    lines = f.read().splitlines()
    bow_set = []
    for line in lines:
        # line = line.split(" ")
        # #print(line)
        # line = " ".join(line)
        line = "\"" + line + "\""
        #print(line)
        bow_set.append(line)
    return bow_set

#bow = read_bow_all()

# def read_bow_files():
#     path = "/Users/apple/temp/nltk/task2/Task_2"
#     content = os.listdir(path)
#     f = open("/Users/apple/temp/nltk/task2/bow_all_files1.txt",'w')             
#     i = 0
#     for direc in content:
#         if direc!=".DS_Store":
#             files = os.listdir(path + "/" + direc)
#             for file in files:
#                 bow = []
#                 print(i)
#                 i=i+1
#                 bow = get_bow1(path + "/" + direc + "/" + file)
#                 #bow = list(set(bow))
#                 for word in bow:
#                     f.write("%s\t" %word)
#                 f.write("\n")
#     print("DONE")
#     f.close()

#read_bow_files()

bow_set = read_bow_all()

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(bow_set)

X = X.toarray()

X = X.tolist()

print(len(X),len(X[0]))
f = open("/Users/apple/temp/nltk/task2/feature_final_verbs.txt","w")
for i in X:
    for j in i:
        f.write("%s " %j)
    f.write("\n")
f.close()
# current = X[0:200]
# prior = X[200:]

# for i in current:
#     for j in prior:

from sklearn.metrics.pairwise import cosine_similarity


fea_set = []
f = open("/Users/apple/temp/nltk/task2/feature_final_verbs.txt","r")
feaset = f.read().splitlines()
for fea in feaset:
    line = fea.split(" ")
    fea_set.append(line[0:-1])

print(len(fea_set),len(fea_set[0]))

current = list(fea_set[0:200])
prior = list(fea_set[200:])

f = open("/Users/apple/temp/nltk/task2/currentfiles.txt","r")
current_files = f.read().splitlines()

# for file in current_files:
#     file = file.replace(".txt","")
#     print(file)

current_files = [file.replace(".txt","") for file in current_files]
#print(current_files[0:2])
    
f = open("/Users/apple/temp/nltk/task2/priorfiles.txt","r")
prior_files  = f.read().splitlines()

# for file in prior_files:
#     file = file.replace(".txt","")

prior_files = [file.replace(".txt","") for file in prior_files]

sim = []
f = open("/Users/apple/temp/nltk/task2/output_final_verbs.txt","w")
for i in range(len(current)):
    sim = []
    for j in range(len(prior)):
        simt = cosine_similarity([current[i]],[prior[j]])
        simt = simt.tolist()
        for x in simt:
            for y in x:
                t = y
        sim.append(t)
    
    files_and_sim = [(x,y) for (x,y) in zip(sim,prior_files)]
    files_and_sim = sorted(files_and_sim, key = lambda x: x[0], reverse = True)

    sorted_files = [y for x,y in files_and_sim]

    similar = [x for x,y in files_and_sim]

    
    no = 0
    for it in range(len(sorted_files)):
        no+=1
        f.write(current_files[i] + " Q0 " + sorted_files[it] + " " + str(no) + " " + str(similar[it]) + " SSN_NLP_2" + "\n")
    print(i)

f.close()

#print(sim)
    #print(cosine_similarity([current[0]],[prior[j]]))
#print(sim)
#print(sorted(sim,reverse = True))
#sim = sorted(sim,reverse = True)



# [(x,y) for (x,y) in zip(sim,prior_files)]

# cntbb = [(c,b) for (c,b) in zip(contours,lstBb)]
#     cntbb = sorted(cntbb, key=lambda x: x[1][0])
#     cntbb = sorted(cntbb, key=lambda x: x[1][1])
# for i in current:
#     for j in prior:
#         tfidf = 



