# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
import sys
from collections import defaultdict
from sklearn.decomposition import PCA
from sklearn import svm

# ---------------------------- Initialization ----------------------------------------------------------------------------

dataset_file = open("./features.txt")
dataset_lines = dataset_file.readlines()

features_dataset_dict = []
features_dataset_class = []

test_file = open("./test_features.txt")
test_lines = test_file.readlines()

b=[]
b1=[]
convert = {"sg":1,"pl":2,"any":3,"NA":4}
invert = {"1":"sg","2":"pl","3":"any","4":"NA"}

#------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------Preparing array for dict Vectorizer function---------------------------------------------------


def prepare_model(lines,timp):
    for i in lines:
        temp=i[:-1]
        temp = temp.split(",")
        if(len(temp) != 22):
            continue
        d = {}

        d['word'] = temp[0]
        d['tag'] = temp[1]
        d['suffix_1'] = temp[2]
        d['suffix_2'] = temp[3]
        d['suffix_3'] = temp[4]
        d['suffix_4'] = temp[5]

        d['prev_gender'] = temp[6]
        d['prev_number'] = temp[7]
        d['prev_person'] = temp[8]
        d['prev_case'] = temp[9]


        d['n_gender'] = temp[10]
        d['n_number'] = temp[11]
        d['n_person'] = temp[12]
        d['n_case'] = temp[13]

        d['prev_word'] = temp[14]
        d['next_word'] = temp[15]

        d['len'] = temp[16]
        d['type'] = temp[17]

        if(timp == "train"):
            features_dataset_dict.append(d)
            features_dataset_class.append(int(convert[temp[19]]))
        else:
            b.append(d)
            b1.append(temp[19])

# ----------------------------------------------------------------------------------------------------------------------


prepare_model(dataset_lines,"train")
prepare_model(test_lines,"test")

vec = DictVectorizer()


features_dataset =  vec.fit_transform(features_dataset_dict).toarray()
feats2=vec.transform(b).toarray()

# Classifiying
clf = svm.SVC()
clf.fit(features_dataset,features_dataset_class)

# Predicting test data

out = clf.predict(feats2)

#--------------------------------------------------- Calculating Accuracy ---------------------------------------------

count1 = 0
count2 = 0
for i in range(len(out)):
    count2 += 1
    if(b1[i] == invert[str(out[i])]):
        count1 +=1
    #print "word",b[i]["word"],"number",invert[str(out[i])]

print "Accuracy",(count1/float(count2) * 1.0) * 100.0
