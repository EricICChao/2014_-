__author__ = 'Eric'

import os, re
"""
符合搜尋關鍵字的所有檔案的內容，全部讀取到同一頁面或是造出一份新檔案，將所有內容儲存在這份檔案上。

執行流程:
指定關鍵字
指定要開啟的資料夾
將資料夾內的檔案名稱擺入list中
指定存放符合的資料的新檔案名稱
迴圈(list):
    開啟目錄內的檔案(list中有的名單)
    比對檔案內容的關鍵字
    迴圈(檔案寫入):
        符合者，檔案內容寫入新的檔案理
    開啟新檔案看結果
"""
key_word = input("請輸入要查詢的關鍵字:")
#指定查詢資特定料夾內目錄list
folder_path = input("指定要搜尋的資料夾位址，目錄的路徑表示方法:  C://Users//Eric//Desktop//information literacy相關//，請輸入:")
file_names_list = os.listdir(folder_path)
new_file_name = input("請輸入要儲存搜尋到的資料檔案的檔案格式與名稱: ")
with open("C://Users//Eric//PycharmProjects//untitled//test_text//"+new_file_name, 'xt', encoding= "utf8") as f:
    for x in file_names_list:
    #with open("C://Users//Eric//PycharmProjects//test_text//"+x, encoding= "utf8") as f2:
        with open(folder_path + x,'rt', encoding="utf8") as f2:
            text_data = f2.read()
            #比對英文
            search_english_key_word = re.search(r"\b + key_word + \b", text_data)
            #比對中文.
            search_chinese_key_word = re.search(r"(?u)\b + key_word + \b", text_data)
            #只要統計到的關鍵字數目不為0，就執行
            #text_data.count(key_word)
            if search_english_key_word is not None or text_data.count(key_word) != 0:
                #符合者，將資料一筆一筆寫入檔案裡
                #with open("C://Users//Eric//PycharmProjects//data searching//test_text//"+new_file_name, 'at', encoding= "utf8") as f:
                f.write(text_data)
            elif search_chinese_key_word is not None or text_data.count(key_word) != 0:
                f.write(text_data)

#C://Users//Eric//PycharmProjects//untitled//test_text//
#如果直接改用count()就直接運算，也不要比對了的話........
#請參考 C:\Users\Eric\PycharmProjects\untitled\文字搜尋比對.py


