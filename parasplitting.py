import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
a=word_tokenize("bilal is here")
print(a)

file_object  = open('C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python37-32\\fbdocument.txt', 'r')
f=file_object.read()
a=sent_tokenize(f)
b=[]
stop_words = set(stopwords.words('english'))
'''print(len(a))'''
count=0;


class ParaObject(object):
    """__init__() functions as the class constructor"""
    def __init__(para, index=None, text=None, Value=None):
        para.index = index
        para.text = text
        para.Value = Value
paraList = []
for i in range(len(a)):
    word_tokens = word_tokenize(a[i])
    for w in word_tokens: 
        if w in stop_words:
            count=count +1

    f=(len(word_tokens)-count)/len(word_tokens)
    paraList.append(ParaObject(i, a[i], f))
    count=0


paraList.sort(key=lambda x: x.Value,reverse=True)

'''for i in range(len(paraList)):
    print ("paraList",paraList[i].Value)'''
aq=eval(input("how much data u wnat to precise input in %"))
ReqParaPercentage=int((aq/100)* len(a))
'''print(ReqParaPercentage)'''
list1=[]
for i in range(ReqParaPercentage):
    list1.append(paraList[i])

list1.sort(key=lambda y:y.index);
'''for i in range(len(list1)):
    print ("paraList",list1[i].index)'''


file = open('C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python37-32\\testfile.txt','w') 
for i in range(len(list1)):    
    file.write(list1[i].text)

print('summary has been written')
file.close()
file_object.close()
