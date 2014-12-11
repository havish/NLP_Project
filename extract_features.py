from edit_distance import edit_distance

import os


#------------ Creating cell ---------------------------

"""def init():
	global m
	m = {}
	for i in range(0,102):
	    m[str(i)]={}
	    for j in range(0,102):
	        m[str(i)][str(j)]={}
	        m[str(i)][str(j)]["cost"] = 0
        	m[str(i)][str(j)]["parent"] = -1
init()
#-----------------------------------------------------------


def reconstruct_path(s,t,i,j):
    global output
    if(m[i][j]["parent"] == -1):
        return

    if(m[i][j]["parent"] == MATCH):
        reconstruct_path(s,t,str(int(i)-1),str(int(j)-1))
        output += "M "
        return

    if(m[i][j]["parent"] == REPLACE):
        reconstruct_path(s,t,str(int(i)-1),str(int(j)-1))
        output += "R("+s[int(i)]+")("+t[int(j)]+") "
        return

    if(m[i][j]["parent"] == INSERT):
        reconstruct_path(s,t,str(int(i)),str(int(j)-1))
        output += "I("+t[int(j)]+") "
        return

    if(m[i][j]["parent"] == DELETE):
        reconstruct_path(s,t,str(int(i)-1),str(int(j)))
        output += "D("+s[int(i)]+") "
        return



def match(s,t):
    if(s==t):
        return 0
    else:
        return 1


def string_compare(s,t):
    opt=[0,0,0]
    for i in range(1,len(s)):
        for j in range(1,len(t)):
            ms = match(s[i],t[j])
            match_value = m[str(i-1)][str(j-1)]["cost"] + ms
            opt[INSERT] = m[str(i)][str(j-1)]["cost"] + 1
            opt[DELETE] = m[str(i-1)][str(j)]["cost"] + 1

            m[str(i)][str(j)]["cost"] = match_value
            if(ms):
                m[str(i)][str(j)]["parent"] = REPLACE
            else:
                m[str(i)][str(j)]["parent"] = MATCH

            for k in range(INSERT,DELETE+1):
                if(opt[k] < m[str(i)][str(j)]["cost"]):
                    m[str(i)][str(j)]["cost"] = opt[k]
                    m[str(i)][str(j)]["parent"] = k;

    return reconstruct_path(s,t,str(len(s)-1),str(len(t)-1)) """
#print m[str(len(s)-1)][str(len(t)-1)]["cost"]

def class_label(temp):
    temp = temp.split(" ")
    temp1 = ""
    for i in range(len(temp)):
        if(temp[i] != "M"):
            temp1 += temp[i] + str(i) + " "
    if(temp1 != ""):
        return temp1[:-1]
    else:
        return "NA"

def get_morph(tag):
    if(len(tag) == 0):
        return "NA"
    return tag

def morph_tags(temp):
    temp = temp.split("|")
    gender = get_morph(temp[2].split("-")[1])
    number = get_morph(temp[3].split("-")[1])
    person = get_morph(temp[4].split("-")[1])
    case = get_morph(temp[5].split("-")[1])
    vib = get_morph(temp[6].split("-")[1])
    TAM = get_morph(temp[7].split("-")[1] )



    s = ""
    s = gender + "," + number + "," + person + "," + case
    return s

def get_suffix(word,pos):
    temp = word[pos:]
    if( (-pos) > len(word) ):
        return "NA"
    return temp


tokens = 0
label_count = 0


def prepare_testfeatures(test_files):
    for file in test_files:
        temp = test_directory + file
        f = open(temp)
        lines = f.readlines()
        for j in range(len(lines)):
            if(len(lines[j]) > 2):
                features=""
                line_split = lines[j].split("\t")
                ID = line_split[0]
                word = line_split[1]

                suffix_1 = get_suffix(word,-1)
                suffix_2 = get_suffix(word,-2)
                suffix_3 = get_suffix(word,-3)
                suffix_4 = get_suffix(word,-4)

                token_length = len(word)
                POSTAG = line_split[4]

                if(word.isalpha()):
                    type = "ALPHA"
                elif(word.isdigit()):
                    type = "NUM"
                else:
                    type = "ALPHANUM_OR_OTHER"

                if( ID == str(1)):
                    previous_morph = "NA,NA,NA,NA"
                    previous_wordform = "NA"
                else:
                    previous_morph = morph_tags(lines[j-1].split("\t")[5])
                    previous_wordform = lines[j-1].split("\t")[1]

                if(len(lines[j+1]) < 2):
                    next_morph = "NA,NA,NA,NA"
                    next_wordform = "NA"
                else:
                    next_morph = morph_tags(lines[j+1].split("\t")[5])
                    next_wordform = lines[j+1].split("\t")[1]


                f3.write(word + "," + POSTAG + "," + suffix_1 + "," + suffix_2 + "," + suffix_3 + "," + suffix_4 + "," + previous_morph + "," + next_morph + "," + previous_wordform + "," + next_wordform + "," + str(token_length) + "," + type + "\n")


def morph_analysis(training_files,timp):
    for file in training_files:
        if(timp == "train"):
            temp = target_directory + file
        else:
            temp = test_directory + file
        f = open(temp)
        lines = f.readlines()
        for j in range(len(lines)):
            if(len(lines[j]) > 2):
                features=""
                line_split = lines[j].split("\t")
                ID = line_split[0]
                word = line_split[1]

                suffix_1 = get_suffix(word,-1)
                suffix_2 = get_suffix(word,-2)
                suffix_3 = get_suffix(word,-3)
                suffix_4 = get_suffix(word,-4)

                token_length = len(word)
                POSTAG = line_split[4]

                cur_morph = morph_tags(lines[j].split("\t")[5])
                #print lines[j],cur_gen
                if(word.isalpha()):
                    type = "ALPHA"
                elif(word.isdigit()):
                    type = "NUM"
                else:
                    type = "ALPHANUM_OR_OTHER"

                if( ID == str(1)):
                    previous_morph = "NA,NA,NA,NA"
                    previous_wordform = "NA"
                else:
                    previous_morph = morph_tags(lines[j-1].split("\t")[5])
                    previous_wordform = lines[j-1].split("\t")[1]

                if(len(lines[j+1]) < 2):
                    next_morph = "NA,NA,NA,NA"
                    next_wordform = "NA"
                else:
                    next_morph = morph_tags(lines[j+1].split("\t")[5])
                    next_wordform = lines[j+1].split("\t")[1]







                #------------------------ Lemma Module ------------------------------ #
                """word1 = "`"+line_split[1][::-1]
                        lemma = "`"+line_split[2][::-1]
                        global output
                global label_count
                        output = ""
                        string_compare(word1,lemma)
                        cl = class_label(output[:-1])
                        try:
                            dic[cl]
                        except:
                    label_count += 1
                            dic[cl] = str(label_count)
                    f2.write(cl + "\t" + dic[cl] + "\n") """

                if(timp == "train"):
                    f1.write(word + "," + POSTAG + "," + suffix_1 + "," + suffix_2 + "," + suffix_3 + "," + suffix_4 + "," + previous_morph + "," + next_morph + "," + previous_wordform + "," + next_wordform + "," + str(token_length) + "," + type + "," + cur_morph + "\n")
                else:
                    f3.write(word + "," + POSTAG + "," + suffix_1 + "," + suffix_2 + "," + suffix_3 + "," + suffix_4 + "," + previous_morph + "," + next_morph + "," + previous_wordform + "," + next_wordform + "," + str(token_length) + "," + type + "," + cur_morph + "\n")


                    #---------------------------------------------------------------------- #


"""a=edit_distance()
s="`happy"
t="`bappy"
a=edit_distance()
a.string_compare(s,t)
print a.output"""

unique_tokens = {}
dic={}
f1 = open("./features.txt","w")
f3 = open("./test_features.txt","w")


target_directory = "./Inter Chunk/CoNLL/wx/news_articles_and_heritage/Training/"
training_files = os.listdir(target_directory)
morph_analysis(training_files,"train")


test_directory = "./Inter Chunk/CoNLL/wx/news_articles_and_heritage/Testing/"
test_files = os.listdir(test_directory)
#prepare_testfeatures(test_files)
morph_analysis(test_files,"test")

target_directory = "./Inter Chunk/CoNLL/wx/conversation/"
training_files = os.listdir(target_directory)
#morph_analysis(training_files)

target_directory = "./Intra Chunk/CoNLL/wx/news_articles_and_heritage/Training/"
training_files = os.listdir(target_directory)
#morph_analysis(training_files)

target_directory = "./Intra Chunk/CoNLL/wx/conversation/"
training_files = os.listdir(target_directory)
#morph_analysis(training_files)

