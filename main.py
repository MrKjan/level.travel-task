import re
import csv

with open('./palata.txt', 'r', encoding='utf-8') as infile:
    test_string = infile.read()

words = re.findall(r'[\w|-]+', test_string)

word_count = {}

for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Дополнительное задание
# Работает для python версии 3.7+
word_count = {k: v for k, v in sorted(word_count.items(), key=lambda item: item[1], reverse=True)}

with open('out.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter=',')
    for line in word_count:
        writer.writerow((line, word_count[line]))
