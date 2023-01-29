with open('file.txt', 'r', encoding='utf-8') as file:
    text = file.read().split()
print(text)
res_text = list(filter(lambda word: 'а' not in word and 'б' not in word and 'в' not in word, text))
print(res_text)