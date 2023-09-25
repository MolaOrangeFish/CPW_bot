from bag_of_word import *
question = ["ชั้น","เมนู","อาหาร","หน่อย","ตึก"]

for each_ques in question:
        for cate_name in bow_dict:
            for each_word in bow_dict[cate_name]["words"]:
                if(each_ques==each_word):
                    print(each_ques)
                    scores[cate_name]+=1
                    print(f"{cate_name}+1")
max_score_cate = max(scores,key=scores.get)

if scores[max_score_cate] == 0:  #if category is none
    print("no category")
    print(scores)
else:                                                       #if category not none
    print(max_score_cate)
    print(scores)
    temp_category.append(max_score_cate) 
print(temp_category)

#####clear list make sure its empty#####
temp_category.clear()
scores = dict.fromkeys(scores,0) #empty when sent max score category
#####clear list make sure its empty#####