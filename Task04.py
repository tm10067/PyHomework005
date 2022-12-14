# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

with open(r'Task04source.txt', 'r') as data:
    text_raw = data.read()
    data.close()

def compress_text(text_raw):
    list_raw = list(text_raw)
    list_compr = []
    counter_c = 0
    for i in range(len(list_raw)):
        if i == 0:
            counter_c += 1
        elif list_raw[i] != list_raw[i - 1]:
            list_compr.append(str(counter_c) + list_raw[i - 1])
            counter_c = 1    
            if i == len(list_raw) - 1:
                list_compr.append(str(counter_c) + list_raw[i])
                counter_c = 0
        else:
            counter_c += 1
            if i == len(list_raw) - 1:
                list_compr.append(str(counter_c) + list_raw[i])
                counter_c = 0
    text_compr = "".join(list_compr)
    return text_compr

with open(r'Task04compressed.txt', 'w') as data:
    data.write(compress_text(text_raw))
    data.close()

def decompress_text(text_compr):
    list_compr = list(text_compr)
    list_raw = []
    counter_d = 0
    for j in range(len(list_compr)):
        if list_compr[len(list_compr) - 1].isdigit() or not list_compr[0].isdigit():
            list_raw = "Ошибка"
            break
        elif j == 0:
            counter_d = int(list_compr[j])
        elif j > 0 and not list_compr[j].isdigit() and not list_compr[j - 1].isdigit():
            list_raw = "Ошибка"
            break
        elif j > 0 and list_compr[j].isdigit() and not list_compr[j - 1].isdigit():
            counter_d = int(list_compr[j])
        elif j > 0 and list_compr[j].isdigit() and list_compr[j - 1].isdigit():
            counter_d = counter_d * 10 + int(list_compr[j])
        elif not list_compr[j].isdigit():
            list_raw.append(list_compr[j] * counter_d)
    text_raw = "".join(list_raw)
    return text_raw
    
with open(r'Task04source1.txt', 'r') as data:
    text_compr = data.read()
    data.close()

with open(r'Task04decompressed.txt', 'w') as data:
    data.write(decompress_text(text_compr))
    data.close()