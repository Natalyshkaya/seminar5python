# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
def encode(s):
    encoding = "" 
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding

with open('file2.txt', 'r') as file2:
    text = file2.read().split()
print(text)
print(encode(text))