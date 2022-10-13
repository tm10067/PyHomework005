# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = """Так говорила в июле 1805 года известная Анна Павловна Шерер, фрейлина и приближенная императрицы Марии Феодоровны, 
встречая важного и чиновного князя Василия, первого приехавшего на ее вечер. Анна Павловна кашляла несколько дней, у нее был грипп, 
как она говорила (грипп был тогда новое слово, употреблявшееся только редкими). В записочках, разосланных утром с красным лакеем, 
было написано без различия во всех: «Si vous n'avez rien de mieux à faire, Monsieur le comte (или mon prince), 
et si la perspective de passer la soirée chez une pauvre malade ne vous effraye pas trop, je serai charmée de vous 
voir chez moi entre 7 et 10 heures. Annette Scherer» 3. — Dieu, quelle virulente sortie! 4 — отвечал, нисколько не смутясь такою встречей, 
вошедший князь, в придворном, шитом мундире, в чулках, башмаках и звездах, с светлым выражением плоского лица. 
Он говорил на том изысканном французском языке, на котором не только говорили, но и думали наши деды, и с теми, тихими, 
покровительственными интонациями, которые свойственны состаревшемуся в свете и при дворе значительному человеку. 
Он подошел к Анне Павловне, поцеловал ее руку, подставив ей свою надушенную и сияющую лысину, и покойно уселся на диване. 
— Avant tout dites-moi, comment vous allez, chère amie? 5 Успокойте меня, — сказал он, не изменяя голоса и тоном, в котором 
из-за приличия и участия просвечивало равнодушие и даже насмешка. — Как можно быть здоровой... когда нравственно страдаешь? 
Разве можно, имея чувство, оставаться спокойною в наше время? — сказала Анна Павловна. — Вы весь вечер у меня, надеюсь? — 
А праздник английского посланника? Нынче середа. Мне надо показаться там, — сказал князь. — Дочь заедет за мной и повезет меня. — 
Я думала, что нынешний праздник отменен, Je vous avoue que toutes ces fêtes et tous ces feux d'artifice commencent à devenir insipides 
6. — Ежели бы знали, что вы этого хотите, праздник бы отменили, — сказал князь по привычке, как заведенные часы, говоря вещи, 
которым он и не хотел, чтобы верили."""

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
print(text_processed)