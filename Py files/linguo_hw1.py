import pymorphy2
from pymorphy2 import tokenizers
morph = pymorphy2.MorphAnalyzer()
print("------------------------------")


word_predicts = morph.parse('этой')
for i in word_predicts:
    print(i)
print("------------------------------")



file = open("E:\Study\etalon.txt", "r")
example = file.read()
arr = pymorphy2.tokenizers.simple_word_tokenize(example)
print(arr)
predloj = str('моя окна').split()
for word in arr:
    word_predicts = morph.parse(word)
    tags = word_predicts[0].tag
    print(word_predicts[0].word, "\t", word_predicts[0].normal_form, "\t", tags)
print("------------------------------")
print(type(word_predicts[0].tag))

word_predicts = morph.parse('умница')
for i in word_predicts:
    print(i)
print("------------------------------")

word_predicts = morph.parse('Дистальнее')
for i in word_predicts:
    print(i)
print("------------------------------")


word_predicts = morph.parse('молодец')
for i in word_predicts:
    print(i)
print("------------------------------")

example = 'Этой горе нужно много подношений!'
arr = pymorphy2.tokenizers.simple_word_tokenize(example)
print(arr)
predloj = str('моя окна').split()
for word in arr:
    word_predicts = morph.parse(word)
    print(word_predicts[0])
print("------------------------------")

word_predicts = morph.parse('горе')
for i in word_predicts:
    print(i)
print("------------------------------")

word_predicts = morph.parse('пускай')
for i in word_predicts:
    print(i)
print("------------------------------")

word_predicts = morph.parse('что')
for i in word_predicts:
    print(i)
print("------------------------------")

word_predicts = morph.parse('Дистальнее')
for i in word_predicts:
    print(i)
print("------------------------------")

word_predicts = morph.parse('убийце')
for i in word_predicts:
    print(i)
print("------------------------------")
