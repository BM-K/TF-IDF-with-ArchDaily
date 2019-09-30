import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def get_recommendations(title, cosine_sim):
    # 선택한 영화의 타이틀로부터 해당되는 인덱스를 받아옵니다. 이제 선택한 영화를 가지고 연산할 수 있습니다.
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

    # 모든 영화에 대해서 해당 영화와의 유사도를 구합니다.
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 영화들을 정렬합니다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 20개의 영화를 받아옵니다.
    sim_scores = sim_scores[1:21]

    # 가장 유사한 10개의 영화의 인덱스를 받아옵니다.
    movie_indices = [i[0] for i in sim_scores]
    num=1
    for i in movie_indices:
        print(num,":",data_Name[i])
        num+=1
    print("------------------------------------------------------")
    # # 가장 유사한 10개의 영화의 제목을 리턴합니다.
    # return data['title'].iloc[movie_indices]

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
        get_recommendations(data_input, cosine_sim)
    elif a == 2:
        word = input("word input : ")
        sentence = []
        get_page_myword(word, sentence)
    elif a == 0:
        exit()
    else:
        print("Error No function try again")