import re

s = input()
s = s.lower()
text = re.sub(r"[^A-Za-z ]+", '', s)
for match in re.finditer(text):
    word = match.group(0)
    if prev_word is not None:
        print(prev_word, word)
    prev_word = word