import joblib
import numpy as np
from package.nlp_function import *
from bag_of_word import bow_dict,scores,temp_category

question = ["ขอ","เมนู","อาหาร","หน่อย","ค่ะ"]


for each_ques in question: ##get word from question
    for cate_name in bow_dict: ##get type detail from dictonary
        for each_word in bow_dict[cate_name]["words"]:##word matching with ques and bow for each type 
            if(each_ques == each_word):
                print(f"each_ques : {each_ques}")
                print(f"cate_name : {cate_name}")
                print(f"each_word : {each_word}")
                scores[cate_name]+=1
                print(f"{cate_name}+1")

max_score_cate = max(scores,key=scores.get)
if scores[max_score_cate] == 0:  #if category is none (หาประเภทไม่เจอ)
    print("no category")
    print(scores)
else:           #if category not none (หาประเภทเจอ)
    print(max_score_cate)
    print(scores)
    temp_category.append(max_score_cate) 
print(temp_category)

#####clear list make sure its empty#####
temp_category.clear()
scores = dict.fromkeys(scores,0) #empty when sent max score category
#####clear list make sure its empty#####

"""

##Reply text function##
def reply_text(txt):
    print(txt)

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
recived_txt="ทักษะว่ายเปิดสอนกลุ่มเด็กม.ต้นมั้ยครับ"
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

"""


