import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def get_TFIDF_Result(title, cosine_sim):
    while True:
        try:
            idx = indices[title]
            break
        except KeyError:
            print("------No page name. Maybe I don't update recent page------")
            print("\n")
            return
    idx = indices[title]
    idx = int(idx)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    data_indices = [i[0] for i in sim_scores]
    num=1
    for i in data_indices:
        print(num,":",data_Name[i])
        num += 1
    print("------------------------------------------------------")


def get_page_myword(word, sentence):
    for i in range(len(data_Des)):
        count = 0
        a = data_Des[i].lower()
        b = a.split(' ')
        for j in b:
            if word == j:
                count+=1
            else:
                continue
        sentence.append(count)
    Max_index = []
    for i in range(20):
        Max = max(sentence)
        Max_index.append(sentence.index(Max))
        sentence[Max_index[i]] = 0
    #
    num=1
    for j in Max_index:
        print(num,":",data_Name[j])
        num+=1
    print("------------------------------------------------------")

data_num = []
data_Name = []
data_Des = []
f = open('ArchDaily.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
k = 0
for line in rdr:
    data_num.append(k)
    data_Name.append(line[1])
    data_Des.append(line[2])
    k += 1
f.close()

pd_data_des = pd.Series(data_Des, index=data_num)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(pd_data_des)

from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(data_num, index=data_Name)

print("--Running--")
while(1):
    print("------------------------------------------------------")
    print("What do you want to use functions?")
    print("1 : search similar page (compare each description)")
    print("2 : search word (compare each description)")
    print("0 : exit")
    a = int(input("input number: "))
    if a == 1:
        data_input = input("data input :")
        get_TFIDF_Result(data_input, cosine_sim)
    elif a == 2:
        word = input("word input : ")
        sentence = []
        get_page_myword(word, sentence)
    elif a == 0:
        exit()
    else:
        print("Error No function try again")