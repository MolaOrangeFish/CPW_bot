import re
import deepcut
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