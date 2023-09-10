import joblib
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer, TfidfTransformer
import numpy as np
import pandas as pd
import re
import string
import deepcut
from pythainlp import word_tokenize
from pythainlp.corpus import thai_stopwords
from pythainlp.corpus import thai_stopwords
from pythainlp.util import normalize

##Reply text function##
def reply_text(txt):
    print(txt)

##text process##
def word_split(text):
    words = re.split(r",",text)
    return words

def text_process_save_comma(text): ##save ,
    text = re.sub("\[|\]|'|"," ",text).replace(" ", "")
    text = re.sub(r'[0-9]+'," ",text).replace(" ", "")
    return text
##text process##
def split_word(text):
    tokens = deepcut.tokenize(text)
    return tokens

####LOAD SEGMENTATION MODEL####
# 0:Negative 1:Positive 2:Question
segment_type = "model\segment_classify\check_type.sav"
segment_vectorizer = "model\segment_classify\count_vectorizer.sav"
segment_model = joblib.load(open(segment_type,"rb"))
vectorizer_segment = joblib.load(open(segment_vectorizer,"rb"))

####LOAD QEUSTION MODEL####
# 0:ค่าเทอม 1:Other
question_type = "model\question_classify\check_question_type.sav"
question_vectorizer = "model\question_classify\question_vectorizer_word.sav"
question_model = joblib.load(open(question_type,"rb"))
vectorizer_question = joblib.load(open(question_vectorizer,"rb"))

###GET TEXT FROM CHAT AND CONVERT IT TO ARR###
recived_txt="ขอตารางเรียน ป6 หน่อยค่ะ"
text = [recived_txt]

####VECTORIZER AND PREDICT SEGMENTATION####
text_list = vectorizer_segment.extract_bowtfidf(text).toarray()
predictions = segment_model.predict(np.asarray(text_list)) 

if(predictions[0]==0): # 0:Negative 1:Positive 2:Question
    print('Negative Group')
    reply_text('โรงเรียนชลประทานวิทยาจะนำคำแนะนำที่ได้รับมาไปปรับปรุงค่ะ')
elif (predictions[0]==1):
    print('Positive Group')
    reply_text('ขอขอบคุณที่ให้การชื่นชมโรงเรียนชลประทานวิทยานะคะ')
else:
    print('Question Group')
    split_text = split_word(recived_txt)
    split_text_ai = str(split_word(recived_txt))
    split_text_ai=text_process_save_comma(split_text_ai)
    text_list = vectorizer_question.transform([split_text_ai]).reshape(1,-1).todense()
    question_predictions = question_model.predict(np.asarray(text_list))
    question_type = predictions[0]# 0:ค่าเทอม 1:Other
    if(question_type == 0):
        reply_text("นี่ไงค่าเทอม")
    else:
        period = ['ตาราง','ตา']
        store_ques_type = {"period":False}
        for word_match in period:   ##matching period
            for data in split_text:
                if(word_match in data):
                    store_ques_type["period"] = True
        if(store_ques_type["period"] is True):
            reply_text("นี่ไงตารางเรียน")
        else:
            reply_text("นี่ไม่เกี่ยวไปถาม รร นู่น")




