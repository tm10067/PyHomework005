# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

import codecs

data = codecs.open(r'Task01source.txt', 'r', "utf-8")
text = data.read()
data.close()

def replace_and_split(text):
    list_text = text.replace(",", " ,").replace(".", " .").replace("(", "( ").replace(")", " )").replace(":", " :").replace(";", " ;").replace("!", " !").replace("?", " ?").replace("«", "« ").replace("»", " »").replace("\n", "\n ").split(" ")
    return list_text

list_text = replace_and_split(text)
string_delete = input("введите фрагмент для удаления слов из текста: ")

def delete_words_with_string(list_text, string_delete):
    list_text_processed = []
    counter_del = 0
    for i in list_text:
        if not string_delete in i:
            list_text_processed.append(i)
        else: 
            counter_del += 1
    print(f"{counter_del} слов удалено")
    return list_text_processed
    
list_text_processed = delete_words_with_string(list_text, string_delete)   

def merge_from_list(list_text):
    text = " ".join(list_text).replace(" ,", ",").replace(" .", ".").replace("( ", "(").replace(" )", ")").replace(" :", ":").replace(" ;", ";").replace(" !", "!").replace(" ?", "?").replace("« ", "«").replace(" »", "»").replace("\n ", "\n")
    return text

text_processed = merge_from_list(list_text_processed)

data = codecs.open(r'Task01result.txt', 'w', "utf-8")
data.write(text_processed)
data.close()