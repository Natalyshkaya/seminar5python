text = input().split()
res_text = list(filter(lambda word: 'а' not in word and 'б' not in word and 'в' not in word, text))
print(res_text)