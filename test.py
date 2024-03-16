import zipfile
import sys
from copy import deepcopy

import gensim, logging
import wget
import pprint
import array
import copy
from copy import deepcopy

stream = 'C:/Projects/models/ml/model.bin'
# print(stream)
model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)
# print(model.similarity('человек_NOUN', 'обезьяна_NOUN'))
words1 = ['книга_NOUN', 'аист_NOUN', 'нож_NOUN', 'планета_NOUN', 'дорога_NOUN',
         'справедливость_NOUN', 'море_NOUN', 'монета_NOUN', 'смерть_NOUN', 'баскетбол_NOUN']
words2 = words1.copy()

paras = []
sum = 0
sum1 = 0
n = 0
m= 0
for i in range(10):
    for w2 in words2:
        mod = round(model.similarity(words1[i], w2),5)
        mod1 = round((1-mod)*100,3)
        para = [i, words1[i], i+words2.index(w2), w2, mod, mod1]
        paras.append(para)
        if w2 in words2[1:]:
            n += 1
            sum += mod
            sum1 +=mod1
            m = sum/n
            m1 = sum1/n
    del words2[0]


result = []
str1 = []
en_result = []
str2 = []
for w in words1:
    for el in paras:
        if words1.index(w) == el[0]:
           # t = (el[2], el[3], el[4])
            str1.insert(0, el[4])
            str2.insert(0, el[5])
    w = w[:w.rfind("_")]
    str1.insert(0, w)
    str2.insert(0, w)
    result.append(str1)
    en_result.append(str2)
    str1=[]
    str2=[]
result_rev = result[::-1]
en_result_rev = en_result[::-1]
words3 = [w[:w.rfind("_")] for w in words1]

words_rev = words3[::-1]
words_rev.insert(0," ")
#pprint.pprint(en_result_rev)
#print(words_rev)



def create(datalist, en_datalist):
    csv = 'До пересчета\n'
    for d in datalist:
        csv += '{}\n'.format(','.join(str(el) for el in d))
    csv +='{}\n'.format(','.join(str(word) for word in words_rev))
    csv += '{}\n'.format(round(m,5))

    csv += '\n'
    csv += 'После пересчета\n'
    for d in en_datalist:
        csv += '{}\n'.format(','.join(str(el) for el in d))
    csv +='{}\n'.format(','.join(str(word) for word in words_rev))
    csv += '{}\n'.format(round(m1,3))
    print(csv)

    with open('C:/Projects/result.csv','w', encoding="utf-8") as page:
        page.write(csv)
    return csv

create(result_rev, en_result_rev)


