# Напишите программу, удаляющую из текста все слова, содержащие "абв".


user_text = input("Введите текст: ")
del_text = input("Введите фрагмент текста для удаления: ")
user_text = user_text.split(" ")
for word in user_text:
    if del_text in word:
        user_text.remove(word)
    sentence = " ".join(user_text)
print(sentence)