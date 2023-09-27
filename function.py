import re
import deepcut

# Reply text function
def reply_text(txt):  # พิมพ์ข้อความที่รับเข้ามาผ่านพารามิเตอร์ txt 
    print(txt)        # แสดงข้อความที่รับเข้ามาบนหน้าจอ console ด้วยฟังก์ชัน print

# Text process
def word_split(text):   
    words = re.split(r",",text)  # ใช้ re.split() จากโมดูล re เพื่อแยก (text) โดยใช้ (",") เป็นตัวแบ่ง
    return words                 # คืนค่าลิสต์ที่เก็บคำที่แยกแล้วเป็นผลลัพธ์ของฟังก์ชัน

# Save, ใช้ในการประมวลผลข้อความที่รับเข้ามา โดยลบอักขระที่กำหนด และตัวเลขออกจากข้อความ
# ใช้ re.sub() เพื่อแทนที่อักขระ [, ], ' ด้วยช่องว่าง (" ")
# ใช้ .replace() เพื่อลบช่องว่างทั้งหมดออกจากข้อความ           
def text_process_save_comma(text):  
    text = re.sub("\[|\]|'|"," ",text).replace(" ", "")   
    text = re.sub(r'[0-9]+'," ",text).replace(" ", "")    
    return text

# Text process, ใช้ deepcut.tokenize() เพื่อแบ่งคำใน(text) เป็น(tokens) โดยใช้ตัวตัดคำจาก deepcut
def split_word(text):
    tokens = deepcut.tokenize(text) 
    return tokens


